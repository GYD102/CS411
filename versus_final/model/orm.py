from model.popos.senator import Senator
from model.popos.versus_result import VersusResult
from model.popos.user_info import UserInfo


class ORM:

    @staticmethod
    def map_senator(tup):
        """
        :param tup: (senator_id, image_url, senator_name, bio)
        :return: Senator
        """
        senator_id, image_url, senator_name, bio = tup
        return Senator(id=senator_id, name=senator_name, biography=bio, image_url=image_url)

    @staticmethod
    def map_user_info(tup):
        """
        :param tup: (user_id, user_name)
        :return: UserInfo
        """
        user_id, user_name = tup
        return UserInfo(user_id=user_id, user_name=user_name)

    @staticmethod
    def map_versus_result(tup):
        """
        :param tup: (result_id, is_tie, senator_id_1, senator_id_2, winner_id, user_id)
        :return: VersusResult
        """
        result_id, is_tie, senator_id_1, senator_id_2, winner_id, user_id = tup
        return VersusResult(senator_id_1=senator_id_1, senator_id_2=senator_id_2,
                            winner_id=winner_id, user_id=user_id, res_id=result_id, is_tie=is_tie)
