from flask import Flask

# Now these last ones were incredibly basic building blocks
# lets add functionality and the ability to communicate
# most information is sent as a JSON output which 
# then can be used in multiple ways, usually to wrap 
# needed information, learn more at
# https://www.w3schools.com/js/js_json_intro.asp

app = Flask(__name__)

@app.route('/')
def hello_user(name):
    return "Hello " + name

if __name__ == '__main__':
    # Runs the Flask app

    # host specifies where the app runs
    # default values are 127.0.0.1 and localhost
    app.run(host='localhost', debug=True)