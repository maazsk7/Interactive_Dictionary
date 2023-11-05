import json
from difflib import get_close_matches

# help(json.load)
data =json.load(open("data.json"))
def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        yn=input("did you mean %s instead ? Enter Y if yes, or N if no : " % get_close_matches(word,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it"
        else:
            return "We didn't understand your query"
            
    else:
        return("The word doesn't exist, Please double check it")
word =input("Enter Word: ")
print(translate(word))