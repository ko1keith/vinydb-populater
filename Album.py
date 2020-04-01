

class Album():
    def __init__(self):
        self.albumName = ""
        self.artistName = ""
        self.publishDate = ""
        self.imageUrl = ""



    def getAlbumName(self):
        return self.albumName

    def setAlbumName(self, albumName):
        self.albumName = albumName

    def getArtistName(self):
        return self.artistName

    def setArtistName(self, artistName):
        self.artistName = artistName

    def getPublishDate(self):
        return self.publishDate

    def setPublishDate(self, publishDate):
        self.publishDate = publishDate

    def getImageUrl(self):
        return self.imageUrl

    def setImageUrl(self, imageUrl):
        self.imageUrl = imageUrl


    def toString(self):
        str = ""
        str = str + "Album: " + self.albumName + "\n"
        str = str + "Artist: " + self.artistName + "\n"
        str = str + "Publish Date: " + self.publishDate + "\n"
        str = str + "Image URL: " + self.imageUrl + "\n"

        return str
