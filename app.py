from flask import Flask

app = Flask(__name__)

@app.route('/home/')

def home_page():
    return "This is the Home Page"


if __name__ == '__main__':
    # Runs the Flask app

    # host specifies where the app runs
    # default values are 127.0.0.1 and localhost
    app.run(host='localhost', debug=True)