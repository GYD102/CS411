from model.db import DbUtil
from model.compare import WinnerComputer


class QuizResultProcessor:

    @staticmethod
    def process_results(sen_id_1, sen_id_2, results):
        """
        :param sen_id_1: str
        :param sen_id_2: str
        :param results: str
        :return: winning_senator_id : str
        """

        def results_to_list(results):
            arr = []
            i = 0
            while i < len(results):
                if results[i] == '-':
                    arr.append(-1)
                    i += 2
                elif results[i] == '0':
                    arr.append(0)
                    i += 1
                else:
                    arr.append(1)
                    i += 1

            return arr

        results = results_to_list(results)
        print(results)

        def results_to_score(results, score_map):
            score = []
            for i, v in enumerate(results):
                if v == 0:
                    score.append(0)
                elif v == 1:
                    score.append(score_map[i])
                else:
                    score.append(-(score_map[i]))

            return score

        _, score_map, topics = DbUtil.get_questions_scores_topics()
        score = results_to_score(results, score_map)

        users_stances_dict = {topic: val for topic, val in zip(topics, score)}
        winning_senator_id = WinnerComputer.compute_winner(sen_id_1, sen_id_2, users_stances_dict)

        return winning_senator_id
