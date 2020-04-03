# Perform all API requests
# Parses album info and posts to MOngoDB database
import requests
from Album import Album


class Request():
    def __init__(self):
        pass

    # Retrieve album info with lastFM api
    def getAblumInfo(self, url):

        try:
            response = requests.get(url).json()

            albumObj = Album()
            albumObj.setAlbumName(response["album"]["name"])
            albumObj.setArtistName(response["album"]["artist"])
            albumObj.setPublishDate(response["album"]["wiki"]["published"])
            for x in response["album"]["image"]:
                if(x["size"] == "large"):
                    albumObj.setImageUrl(x["#text"])
                    break

            return albumObj
        except requests.exceptions.RequestException as e:
            print("Error.")
            print(e)

    # Post album info to MongoDB
    def postAlbumInfo(self, url):

        try:
            requests.post(url)
        except requests.exceptions.RequestException as e:
            print("Error.")
            print(e)

    # Retrieve list of albums from specified Artist
    def getAlbumList(self, url):
        tempList = []

        try:
            response = requests.get(url).json()

            for x in response["topalbums"]["album"]:
                tempList.append(x["name"])

        except requests.exceptions.RequestException as e:
            print("Error.")
            print(e)

        return tempList

    def checkAlbumAdded(self, albumName, artistName):
        f = open("albumHistory.txt")
        for line in f:
            album = line.strip("\n").split("BY")

            print(albumName)
            print(album[0])
            print(artistName)
            print(album[1])
            if(albumName == album[0] and artistName == album[1]):
                return True

        return False