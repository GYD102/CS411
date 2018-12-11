class VersusResult:

    def __init__(self, res_id, senator_id_1, senator_id_2, winner_id, is_tie, user_id):
        """
        :param res_id: int
        :param senator_id_1: str
        :param senator_id_2: str
        :param winner_id: str
        :param is_tie: bool
        :param user_id: string
        """

        self.res_id = res_id
        self.senator_id_1 = senator_id_1
        self.senator_id_2 = senator_id_2
        self.winner_id = winner_id
        self.is_tie = is_tie
        self.user_id = user_id

    def get_loser(self):
        """
        :return: loser : senator_id : string
        """
        if self.senator_id_1 == self.winner_id:
            return self.senator_id_2

        return self.senator_id_1
