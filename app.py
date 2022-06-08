from flask import Flask

# Let's make a more complex app 
# Increment counting app with a name app within it

app = Flask(__name__)

# the route now becomes http://localhost:5000/<number here>
# now multiple functions can be defined 
# and called when the url is input
@app.route('/<int:number>')

def incrimenter(number):
    # this will take the number in the URL and add 1
    return "We are at " + str(number+1)

if __name__ == '__main__':
    # Runs the Flask app

    # host specifies where the app runs
    # default values are 127.0.0.1 and localhost
    app.run(host='localhost', debug=True)