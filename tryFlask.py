#flask:http://flask.pocoo.org/docs/1.0/
#set exporting the FLASK_APP="this file name" in your terminal environment.
#then command "flask run". A server starts.
from flask import Flask
from scraping import getInfo
import os

app = Flask(__name__) #__name__ is a name of this file(module) when you declare it in another module.

@app.route("/")
def hello_world():
    apple = "https://markets.ft.com/data/equities/tearsheet/summary?s=AAPL%3ANSQ"
    amazon = "https://markets.ft.com/data/equities/tearsheet/summary?s=AMZN:NSQ"
    urlList = []
    urlList.append(apple)
    urlList.append(amazon)
    text = ""
    for url in urlList:
        info = getInfo(url)
        text += f"Company: {info[0]}\nPrice: {info[1]}\n, Compared: {info[2]}\n"
    subject = appendInText("draft.txt", text)
    return subject

def appendInText(filePath, text):
    with open(filePath, 'w+') as f:
        for row in f:
            row = ""
        f.write(text)
    return text
