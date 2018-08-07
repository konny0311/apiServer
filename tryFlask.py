#flask:http://flask.pocoo.org/docs/1.0/
#set exporting the FLASK_APP="this file name" in your terminal environment.
#then command "flask run". A server starts.
from flask import Flask
app = Flask(__name__) #__name__ is a name of this file(module) when you declare it in another module.

@app.route("/")
def hello_world():
    return "hello world"
