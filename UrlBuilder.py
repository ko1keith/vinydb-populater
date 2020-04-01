# Build URL search queries based on information given from user input
from Album import Album

class UrlBuilder():
    def __init__(self):
        self.urlLastFM = "http://ws.audioscrobbler.com/2.0/"
        self.urlMongoDB = "http://localhost:8080/vinyl"

    # Build query for one album using API syntax for LastFM
    # Params: String -> strAblum
    #         String -> strArtist
    # Return: String -> urlQuery
    def getUrlAlbum(self, strAlbum, strArtist):
        url = self.urlLastFM + "?method=album.getinfo&api_key=4f59be03f16c37082901e7e0fc64fc5a&artist=" + strArtist + "&album=" + strAlbum + "&format=json"
        return url

    # Build query for list of Albums from one Artist
    def getUrlArtist(self, strArtist):
        pass

    # Build list of querys for multiple albums
    def getUrls(self, dictAlbumArtist):
        pass

    def postUrlCreate(self, objAlbum):
        obj = objAlbum
        url = self.urlMongoDB + "/create?albumName=" + obj.getAlbumName() + "&artistName=" + obj.getArtistName() + "&year=" + obj.getPublishDate() + "&imageUrl=" + obj.getImageUrl()
        return url
