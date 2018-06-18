# /usr/bin/env python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
phonebook = {"+16504556853": 'Christine', "+16037140727": 'Zach'}

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    number = request.form['From']
    resp = MessagingResponse()

    try:
        friend = phonebook[number]
        resp.message('Hello {f}! :D'.format(f=friend))
    except:
        resp.message("Hello friend! :)")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
