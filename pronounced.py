
import requests
import re

def get_definition(word):
    headers = {'X-Mashape-Key': 'YOUR_KEY',
               'Accept': 'application/json'}

    r = requests.get('https://wordsapiv1.p.mashape.com/words/%s' % word, headers=headers)
    return r.json()

def get_definition2(word):
    r = requests.get('http://dictionary.reference.com/browse/%s' % word)
    res = re.search('spellpron">\[([^\]]+)\]', r.text)
    if res:
        return res.group(1)
    raise Exception("error")

def process():
    gees = 0
    jays = 0

    with open("out", "r") as f:
        words = f.read()
        for group in words.split("\n"):
            parts = group.split(" ", 1)
            if len(parts) == 2:
                pronounced = re.sub("<[^>]+>", "", parts[1])
                if pronounced[0] == "g":
                    gees += 1
                elif pronounced[0] == "j":
                    jays += 1

    print("g: %s" % gees)
    print("j: %s" % jays)

def get_pronunciations():
    with open("words", "r") as f:
        words = f.read()
        for word in words.split("\n"):
            word = word.strip()
            try:
                print("%s %s" % (word, get_definition2(word)))
            except:
                print("%s error" % word)

if __name__ == "__main__":
    #get_pronunciations()
    process()
