import json

keywords = json.load(open("keywords.json", encoding="utf8"))["keywords"]

def check_keywords(txt: str):
    for word in keywords:
        if word.lower() in txt.lower():
            return True
    return False