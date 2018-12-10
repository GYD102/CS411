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

        # todo: actual compare results to senator stances and return sen_id with greatest overlap
        return sen_id_1
