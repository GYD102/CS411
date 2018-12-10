from flask import Flask, redirect, url_for, session, render_template, request
from flask_dance.contrib.github import make_github_blueprint, github
import requests
import os
import operator
from model.azure_face import AzureFace
import config
from model.mock_db import MockDB

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
    # user_id = user['id']

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
        # grab the value attribute associated with the options selected
        senator_1 = request.form.get('senator_1')
        senator_2 = request.form.get('senator_2')

        return f'quiz start page for {senator_1} and {senator_2}'

    return redirect(url_for('welcome'))


@app.route('/photo', methods=['GET'])
def photo():
    if not github.authorized:
        return redirect(url_for('welcome'))

    return render_template('take_photo.html')


@app.route('/photo', methods=['POST'])
def photo_post():
    if 'PostImage' in request.files:
        file = request.files['PostImage']
        blob = file.read()
        sentiment_dict = AzureFace.get_face_sentiment_bytes(blob)

        if sentiment_dict:
            majority_sentiment = max(sentiment_dict.items(), key=operator.itemgetter(1))[0]
            return majority_sentiment

        return 'Face not found - please try again'

    return 'Please take picture'


if __name__ == "__main__":
    app.run(port=3000, debug=True, ssl_context='adhoc')
