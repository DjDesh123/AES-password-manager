from flask import Flask, render_template

#constructer for the flask app and it sets up the application
app = Flask(__name__)

# this is to create the url that the function underneath will respond to
@app.route('/')
def index():
    #this is to link to the LogIn.html file
    return render_template("LogIn.html")

# makes the flask app run when this file is executed directly not when imported
if __name__ == '__main__':
    app.run(debug=True)
