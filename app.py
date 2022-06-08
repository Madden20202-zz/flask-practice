from flask import Flask

# Let's make a hello world app

# Creates an instance of the class
app = Flask(__name__)

# route allows the app to know what 
# URL triggers the functions that 
# are defined

# methods specifies what HTTP methods are allowed
# the default value is ['GET']
@app.route('/', methods=['GET', 'POST'])

def welcome():
    return "Hello World!"

# This is a special variable in Python where
# the value of a script name is taken and 
# ensures that the app is only ran on the main file
if __name__ == '__main__':
    # Runs the Flask app

    # host specifies where the app runs
    # default values are 127.0.0.1 and localhost
    app.run(host='localhost', debug=True)