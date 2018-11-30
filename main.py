import json

data = json.load(open("Resources/data.json"))

def checkDef(word):
    word = word.lower()
    if word in data:
        return(data[word])
    else:
        return("There is no such word in database")
userWord = ""
while userWord.lower()!="N":
    userWord = input("Which word you search for? : ")
    print(checkDef(userWord))
    userWord = input("Do you wish to continue? [Y/N]: ")
    if(userWord.lower()=="y"):
        continue
    elif(userWord.lower()=="n"):
        break
    else:
        while userWord.lower() != "y" and userWord.lower() != "n":
            userWord = input("There is no such option, choose [Y/N]: ")


print("Thanks for using this dictionary")

