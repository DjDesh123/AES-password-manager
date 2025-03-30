from flask import Flask

#constructer for the flask app and it sets up the application
app = Flask(__name__)

# this is to create the url that the function underneath will respond to
@app.route('/')
def hello_world():
    return 'Hello World!'

# makes the flask app run when this file is executed directly not when imported
if __name__ == '__main__':
    app.run()
