from flask import Flask
from flask import request
import main

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST', 'DELETE'])
def user():
    if request.method == 'GET':
        """return the information for <user_id>"""
        return "You must send a POST request to this endpoint"
    if request.method == 'POST':
        """modify/update the information for <user_id>"""
        # you can use <user_id>, which is a str but could
        # changed to be int or whatever you want, along
        # with your lxml knowledge to make the required
        # changes
        data = request.form# a multidict containing POST data
        for i in data:
            main.run_nlp(i)
            break
        return "DONE"
    if request.method == 'DELETE':
        """delete user with ID <user_id>"""
        return "You must send a POST request to this endpoint"
    else:
        return "You must send a POST request to this endpoint"


app.run(host='0.0.0.0', port=8080)