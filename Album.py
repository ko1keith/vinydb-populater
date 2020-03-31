

class Album():
    def __init__(self):
        self.albumName = ""
        self.artistName = ""
        self.publishYear = ""
        self.lstTracks = []



    def getAlbumName(self):
        return self.albumName

    def setAlbumName(self, albumName):
        self.albumName = albumName

    def getArtistName(self):
        return self.artistName

    def setArtistName(self, artistName):
        self.artistName = artistName

    def getPublishYear(self):
        return self.publishYear

    def setPublishYear(self, publishYear):
        self.publishYear = publishYear

    def getLstTracks(self):
        return self.lstTracks

    def setLstTracks(self, lstTracks):
        self.lstTracks = lstTracks