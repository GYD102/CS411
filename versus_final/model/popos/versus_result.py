from model.mock_db import MockDB


class VersusResult:

    def __init__(self, senator_id_1, senator_id_2, winner_id, is_tie):
        """
        :param senator_id_1: str
        :param senator_id_2: str
        :param winner_id: str
        :param is_tie: bool
        """
        self.senator_id_1 = senator_id_1
        self.senator_id_2 = senator_id_2
        self.winner_id = winner_id
        self.is_tie = is_tie

    def get_winner(self):
        """
        :return: winner : Senator
        """
        return MockDB.get_senator(self.winner_id)

    def get_loser(self):
        """
        :return: loser : Senator
        """
        if self.senator_id_1 == self.winner_id:
            return MockDB.get_senator(self.senator_id_2)

        return MockDB.get_senator(self.senator_id_1)
