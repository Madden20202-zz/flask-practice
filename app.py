from flask import Flask

# Let's make a more complex app 
# Increment counting app 

app = Flask(__name__)

@app.route('/<int:number>')

def welcome():
    return "Hello World!"

if __name__ == '__main__':
    # Runs the Flask app

    # host specifies where the app runs
    # default values are 127.0.0.1 and localhost
    app.run(host='localhost', debug=True)