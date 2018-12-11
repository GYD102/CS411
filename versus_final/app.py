from flask import Flask, redirect, url_for, session, render_template, request
from flask_dance.contrib.github import make_github_blueprint, github
import requests
import os
import operator
from model.azure_face import AzureFace
import config
from model.mock_db import MockDB
from model.db import SQLiteUtil
from controller.quiz_result_processor import QuizResultProcessor

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__)
app.config['SECRET_KEY'] = config.SECRET_KEY
app.url_map.strict_slashes = False

blueprint = make_github_blueprint(client_id=config.GITHUB_CLIENT_ID, client_secret=config.GITHUB_CLIENT_SECRET)
app.register_blueprint(blueprint, url_prefix='/github_login')


@app.route('/')
def welcome():
    if not github.authorized:
        return render_template('login_prompt.html')

    user = github.get('/user').json()

    # insert user into db if not exists
    SQLiteUtil.create_connection()
    user_id, user_name = user['id'], user['name']
    SQLiteUtil.insert_user_info(user_id, user_name)
    SQLiteUtil.close_connection()

    return render_template('homepage.html', user=user)


@app.route('/github')
def github_login():
    if not github.authorized:
        return redirect(url_for('github.login'))

    return redirect(url_for('welcome'))


@app.route('/logout')
def logout():
    if github.authorized:
        access_token = blueprint.token["access_token"]
        resp = requests.delete(
            f'https://api.github.com/applications/{config.GITHUB_CLIENT_ID}/grants/{access_token}',
            auth=(config.GITHUB_CLIENT_ID, config.GITHUB_CLIENT_SECRET)
        )

        session.clear()

    return redirect(url_for('welcome'))


@app.route('/quiz', methods=['GET'])
@app.route('/quiz/pick_senators', methods=['GET'])
def pick_senators():
    if github.authorized:
        # senators : dict[senator_name] = senator_id
        senators = MockDB.get_mock_senators()
        return render_template('quiz_pick_senators.html', senators=senators)

    return redirect(url_for('welcome'))


@app.route('/quiz/start', methods=['POST'])
def start_quiz():
    if github.authorized:
        questions = MockDB.get_mock_questions()[:3]

        # grab the value attribute associated with the options selected
        senator_1 = request.form.get('senator_1')
        senator_2 = request.form.get('senator_2')
        question_num = int(request.form.get('question_num'))
        answers = request.form.get('answers')

        print(senator_1, senator_2, question_num, answers)
        if question_num < len(questions):
            question = questions[question_num]
            return render_template('quiz_start.html', senator_1=senator_1, senator_2=senator_2,
                                   question_num=question_num, question=question, answers=answers)

        # if we reach here, the quiz is finished
        # save result to db
        winner_id = QuizResultProcessor.process_results(senator_1, senator_2, answers)
        loser_id = senator_1 if senator_2 == winner_id else senator_2
        is_tie = winner_id is not None
        user_id = github.get('/user').json()['id']

        SQLiteUtil.create_connection()
        SQLiteUtil.insert_versus_result(is_tie, senator_1, senator_2, winner_id, user_id)
        SQLiteUtil.close_connection()

        session['senator_result'] = winner_id
        return redirect(url_for('quiz_result'))

    return redirect(url_for('welcome'))


@app.route('/quiz/result', methods=['GET'])
def quiz_result():
    if github.authorized:
        if 'senator_result' in session:
            senator_id = session['senator_result']
            senator = MockDB.get_senator(senator_id)

            return render_template('quiz_result.html', senator=senator)

    return redirect(url_for('welcome'))


@app.route('/history', methods=['GET'])
def history():
    if github.authorized:
        return 'HISTORY'

    return redirect(url_for('welcome'))


@app.route('/photo', methods=['POST'])
def photo_post():
    if 'PostImage' in request.files:
        file = request.files['PostImage']
        blob = file.read()
        sentiment_dict = AzureFace.get_face_sentiment_bytes(blob)

        if sentiment_dict:
            majority_sentiment = max(sentiment_dict.items(), key=operator.itemgetter(1))[0]
            score = AzureFace.get_score(majority_sentiment)
            return str(score)

        return 'E: Face not found - please try again'

    return 'E: Please take picture'


if __name__ == "__main__":
    app.run(port=3000, debug=True, ssl_context='adhoc')
