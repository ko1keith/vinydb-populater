# Perform all API requests
# Parses album info and posts to MOngoDB database

import requests


class Request():
    def __init__(self):
        pass

    # Retrieve album info with lastFM api
    def getAblumInfo(self, url):
        try:
            url = url
            headers = {}

            response = requests.get(url, header = headers)
            return response.json()
        except requests.exceptions.RequestException as e:
            print("Error.")
            print(e)

    # Post album info to MongoDB
    def postAlbumInfo(self, url):
        pass