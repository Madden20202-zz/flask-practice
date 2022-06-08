from flask import Flask

# Let's make a hello world app
aoo = Flask(__name__)

@app.route('/hello/', methods=['GET', 'POST'])

def welcome():
    return "Hello World!"

