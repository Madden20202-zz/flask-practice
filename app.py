from flask import Flask

# Let's make a hello world app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def welcome():
    return "Hello World!"

if __name__ == '__main__':
    app.run(host='localhost', debug=True)