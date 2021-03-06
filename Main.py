from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from Album import Album
import sys
from Request import Request
from UrlBuilder import UrlBuilder

# Variables
objApi = Request()
session = PromptSession()

strPath = ""
strAlbum = ""
strArtist = ""

# Get user input for path
def case_1():
    lstPath = ["album", "artist", "list", "exit"]
    global strPath
    strPrompt = "Choose Path >"

    completer = WordCompleter(lstPath)
    strInput = session.prompt(strPrompt, completer = completer)

    if(strInput in lstPath):
        strPath = strInput
    elif(strInput == "exit"):
        print("Goodbye")
        sys.exit(1)


# Input a single album, input album title, and artist name
def case_2():
    global strAlbum
    global strArtist
    completer = WordCompleter(["run", "exit", "album=", "artist="])
    strPrompt = ">>>"
    lstInput = session.prompt(strPrompt,completer = completer).split()

    if(lstInput[0] == "exit"):
        print("Goodbye")
        sys.exit(1)
    elif(lstInput[0] == "album="):

        s = " "
        strAlbum = s.join(lstInput[1:])
    elif(lstInput[0] == "artist="):
        s = " "
        strArtist = s.join(lstInput[1:])
    elif(lstInput[0] == "run"):
        print("building Query...")
        urlObj = UrlBuilder()
        reqObj = Request()

        boolResponse = reqObj.checkAlbumAdded(strAlbum, strArtist)
        if(boolResponse == True):
            print("Error: Album already added.")
            sys.exit(1)

        strQuery = urlObj.getUrlAlbum(strAlbum, strArtist)
        print("Query: " + strQuery)

        albumObj = reqObj.getAblumInfo(strQuery)
        postUrl = urlObj.postUrlCreate(albumObj)

        reqObj.postAlbumInfo(postUrl)



# User chooses to input artist, return list of possible albums to choose from
def case_3():
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

            boolResponse = reqObj.checkAlbumAdded(x, strArtist)
            if(boolResponse == True):
                print("Error: " + x + " already exists in database")
                continue
            tempUrl = urlObj.getUrlAlbum(x, strArtist) # create LastFM api call
            albumObj = reqObj.getAblumInfo(tempUrl)    # perform LastFM api call
            postUrl = urlObj.postUrlCreate(albumObj)   # create MongoDB api call
            reqObj.postAlbumInfo(postUrl)              # perform MongoDB api Call
            print(x + " By " + strArtist + " posted to MongoDB.")


# User chooses to input a text file, read line by line album and artist name
def case_4():
    global strPath

    f = open("ListOfAlbums.txt")
    for line in f:
        lineSplit = line.strip("\n").split("BY")

        urlObj = UrlBuilder()
        reqObj = Request()

        boolResponse = reqObj.checkAlbumAdded(lineSplit[0], lineSplit[1])
        if (boolResponse == True):
            print("Error: " + lineSplit[0] + " already exists in database")
            continue

        strQuery = urlObj.getUrlAlbum(lineSplit[0], lineSplit[1]) # create LstFM api call
        albumObj = reqObj.getAblumInfo(strQuery)                  # perform LastFM api call
        postUrl = urlObj.postUrlCreate(albumObj)                  # create MongoDB api call
        reqObj.postAlbumInfo(postUrl)                             # perform MongoDB api call
        print(lineSplit[0] + " By " + lineSplit[1] + " posted to MongoDB.")

    strPath = ""


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
    elif(strPath == "exit"):
        sys.exit(1)


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