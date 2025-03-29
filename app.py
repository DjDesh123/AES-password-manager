from flask import Flask

# this is the Flask constructer
# basucally works as by setting up the entire program with all the routes and requests and run the server
#
app = Flask(__name__)

#defines the url that the function underneath will respond to
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


#this basically says that the flask app will run when the  file is excuted directly and not imported 
if __name__ == '__main__':
    app.run(debug=True)
