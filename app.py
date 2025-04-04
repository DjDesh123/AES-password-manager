from flask import Flask, render_template,redirect,url_for

#constructer for the flask app and it sets up the application
app = Flask(__name__)

# this is to create the url that the function underneath will respond to
@app.route('/', methods=['GET', 'POST'])
def index():
    #this is to link to the LogIn.html file
    return render_template("LogIn.html")


#this will be handling the signup page which we need to create
@app.route('/SignUp', methods=['GET', 'POST'])
def signUp():
    return render_template("SignUp.html")


# makes the flask app run when this file is executed directly not when imported
if __name__ == '__main__':
    app.run(debug=True)
