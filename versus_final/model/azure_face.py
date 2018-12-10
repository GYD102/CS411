import requests
import config


class AzureFace:
    face_api_url = 'https://eastus.api.cognitive.microsoft.com/face/v1.0/detect'

    @staticmethod
    def get_face_sentiment_url(url):
        """
        :param url: string
        :return: emotions : dict e.g. {'anger': 0.0, 'contempt': 0.0, 'disgust': 0.0, 'fear': 0.0, 'happiness': 1.0, 'neutral': 0.0, 'sadness': 0.0, 'surprise': 0.0}
        """

        r = requests.post(AzureFace.face_api_url, params=config.AZURE_FACE_PARAMS,
                          headers=config.AZURE_FACE_URL_HEADER, json={'url': url})
        assert r.status_code == 200

        # if a face was detected
        if r.json():
            emotions = r.json()[0]['faceAttributes']['emotion']
            return emotions

        return None

    @staticmethod
    def get_face_sentiment_bytes(data):
        """
        :param data: bytes
        :return: emotions : dict e.g. {'anger': 0.0, 'contempt': 0.0, 'disgust': 0.0, 'fear': 0.0, 'happiness': 1.0, 'neutral': 0.0, 'sadness': 0.0, 'surprise': 0.0}
        """
        r = requests.post(AzureFace.face_api_url, params=config.AZURE_FACE_PARAMS,
                          headers=config.AZURE_FACE_BYTES_HEADER, data=data)
        assert r.status_code == 200

        # if a face was detected
        if r.json():
            emotions = r.json()[0]['faceAttributes']['emotion']
            return emotions

        return None

    @staticmethod
    def get_score(sentiment_key):
        """
        :param sentiment_key: string
        :return: score : int
        """
        keys = {'anger', 'contempt', 'disgust', 'fear', 'happiness', 'neutral', 'sadness', 'surprise'}
        assert sentiment_key in keys

        negative = {'anger', 'contempt', 'disgust', 'fear', 'surprise', 'sadness'}
        neutral = {'neutral'}
        positive = {'happiness'}

        if sentiment_key in negative: return -1
        if sentiment_key in neutral: return 0
        return 1


def test():
    image_url = 'http://airbnboverlast.nl/wp-content/uploads/2016/06/happy-man-768x402.jpg'
    print(AzureFace.get_face_sentiment_url(image_url))


if __name__ == "__main__":
    test()
