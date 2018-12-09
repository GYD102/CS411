import requests
import config


class AzureFace:

    @staticmethod
    def get_face_sentiment(url):
        """
        :param url: string
        :return: emotions : e.g. {'anger': 0.0, 'contempt': 0.0, 'disgust': 0.0, 'fear': 0.0, 'happiness': 1.0, 'neutral': 0.0, 'sadness': 0.0, 'surprise': 0.0}
        """
        face_api_url = 'https://eastus.api.cognitive.microsoft.com/face/v1.0/detect'
        data = {'url': url}
        r = requests.post(face_api_url, params=config.AZURE_FACE_PARAMS,
                          headers=config.AZURE_FACE_HEADER, json=data)
        assert r.status_code == 200

        emotions = r.json()[0]['faceAttributes']['emotion']
        return emotions


def test():
    image_url = 'http://airbnboverlast.nl/wp-content/uploads/2016/06/happy-man-768x402.jpg'
    print(AzureFace.get_face_sentiment(image_url))


debug = True
if debug:
    test()
