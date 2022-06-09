from flask import Flask

app = Flask(__name__)

# Now apps will always redirect when something
# is done, a login page is the best example of this

@app.route('/home/')

def home_page():
    return "This is the Home Page"


if __name__ == '__main__':
    # Runs the Flask app

    # host specifies where the app runs
    # default values are 127.0.0.1 and localhost
    app.run(host='localhost', debug=True)