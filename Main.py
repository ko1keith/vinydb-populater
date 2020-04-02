from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from Album import Album
import sys
from Request import Request
from UrlBuilder import UrlBuilder

# Variables
objApi = Request()
session = PromptSession()

lstPath = ["album", "artist", "list", "exit"]
strPath = ""
strAlbum = ""
strArtist = ""

# Get user input for path
def case_1():
    print("inside case 1")

    global lstPath
    global strPath
    strPrompt = "Choose Path >"

    completer = WordCompleter(lstPath)
    strInput = session.prompt(strPrompt, completer = completer)

    if(strInput in lstPath):
        strPath = strInput
    elif(strInput == "exit"):
        print("Goodbye")
        sys.exit(1)


# User chooses to input single album
def case_2():
    print("inside case 2")

    global strAlbum
    global strArtist
    completer = WordCompleter(["run", "exit", "album=", "artist="])
    strPrompt = ">>>"
    lstInput = session.prompt(strPrompt,completer = completer).split()

    if(lstInput[0] == "exit"):
        print("Goodbye")
        sys.exit(1)
    elif(lstInput[0] == "album="):
        print("inside: album=")
        s = " "
        strAlbum = s.join(lstInput[1:])
    elif(lstInput[0] == "artist="):
        s = " "
        strArtist = s.join(lstInput[1:])
    elif(lstInput[0] == "run"):
        print("building Query...")
        urlObj = UrlBuilder()
        reqObj = Request()

        strQuery = urlObj.getUrlAlbum(strAlbum, strArtist)
        print("Query: " + strQuery)

        albumObj = reqObj.getAblumInfo(strQuery)
        postUrl = urlObj.postUrlCreate(albumObj)

        reqObj.postAlbumInfo(postUrl)



# User chooses to input artist, return list of possible albums to choose from
def case_3():
    print("inside case 3")
    global strArtist
    completer = WordCompleter(["run", "exit", "artist="])
    strPrompt = ">>>"
    lstInput = session.prompt(strPrompt, completer = completer).split()

    if(lstInput[0] == "exit"):
        print("Goodbye.")
        sys.exit(1)
    elif(lstInput[0] == "artist="):
        s = " "
        strArtist = s.join(lstInput[1:])
    elif(lstInput[0] == "run"):
        urlObj = UrlBuilder()
        reqObj = Request()

        url = urlObj.getUrlArtist(strArtist)
        lstAlbums = reqObj.getAlbumList(url)

        completer = WordCompleter (lstAlbums)
        strPrompt = "Choose Album ('finish' to exit) >>> "
        boolFinish = False
        albumChoices = []
        while(boolFinish == False):
            strAlbum = session.prompt(strPrompt, completer = completer)

            if(strAlbum =="finish"):
                boolFinish = True
            else:
                albumChoices.append(strAlbum)
                lstAlbums.remove(strAlbum)

        lstUrls = []
        for x in albumChoices:
            tempUrl = urlObj.getUrlAlbum(x, strArtist) # create LastFM api call
            albumObj = reqObj.getAblumInfo(tempUrl)    # make LastFM api call
            postUrl = urlObj.postUrlCreate(albumObj)   # create MongoDB api call
            reqObj.postAlbumInfo(postUrl)              # make MongoDB api Call
            print(x + " By " + strArtist + " posted to MongoDB.")







# User chooses to input a text file, read line by line album and artist name
def case_4():
    pass


# Switch logic. Determines which case to enter into
def switch():
    global strPath

    if(strPath == "" ):
        return switcher.get(1)()
    elif(strPath == "album"):
        return switcher.get(2)()
    elif(strPath == "artist"):
        return switcher.get(3)()
    elif(strPath == "list"):
        return switcher.get(4)()


# Dictionary outlining the possible cases to switch to
switcher = {
    1: case_1,
    2: case_2,
    3: case_3,
    4: case_4
}


def main():
    #os.system('cls')

    while True:
        switch()

if __name__ == '__main__':
    main()