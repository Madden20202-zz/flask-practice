from flask import Flask

app = Flask(__name__)

# everything that has been done so far has 
# been a request, something that has been 
# read from the code in order to fulfill 
# some task, which lately has just been
# to display some data

# lets have it perform something before the request is filfilled

@app.before_request
def before():
    print("This could be code executed before each request!")

@app.route('/home/')
def greeting():
    return "Hello, Welcome to the tutorial!"

if __name__ == '__main__':
    # Runs the Flask app

    # host specifies where the app runs
    # default values are 127.0.0.1 and localhost
    app.run(host='localhost', debug=True)