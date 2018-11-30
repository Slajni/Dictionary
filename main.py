import json
from difflib import get_close_matches

data = json.load(open("Resources/data.json"))

def checkDef(word):
    word = word.lower()
    if word in data:
        return(data[word])
    elif len(get_close_matches(word,data.keys(),3,0.8)) >= 0:
        matches = get_close_matches(word,data.keys(),3,0.8)
        yn = input("Did you mean %s instead? [Y/N]: " % matches[0])
        if yn.lower() == "y":
            return data[matches[0]]
        elif yn.lower()=="n":
            return "There is no such word in database"
        else:
            while yn.lower() != "y" and yn.lower() != "n":
                yn = input("There is no such option, choose [Y/N]: ")
                if yn.lower() == "y":
                    return matches[0]
                elif yn.lower() == "n":
                    return "There is no such word in database"

    else:
        return "There is no such word in database"


userWord = ""

while userWord.lower()!="N":
    userWord = input("Which word you search for? : ")
    print(checkDef(userWord))
    userWord = input("Do you wish to continue? [Y/N]: ")
    if userWord.lower()=="y":
        continue
    elif userWord.lower()=="n":
        break
    else:
        while userWord.lower() != "y" and userWord.lower() != "n":
            userWord = input("There is no such option, choose [Y/N]: ")


print("Thanks for using this dictionary")

