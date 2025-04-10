from flask import Flask, render_template,redirect,url_for

#constructer for the flask app and it sets up the application
app = Flask(__name__)

# this is to create the url that the function underneath will respond to
@app.route('/', methods=['GET', 'POST'])
def index():
    #this is to link to the LogIn.html file
    return render_template("LogIn.html")


#this will be handling the signup page which we need to create
@app.route('/signUp', methods=['GET', 'POST'])
def signUp():
    return render_template("SignUp.html")

#this is the actual main page for seeing the use of the password manager
@app.route('/managerDashboard', methods=['GET', 'POST'])
def managerDashboard():
    return render_template("managerDashboard.html")

# makes the flask app run when this file is executed directly not when imported
if __name__ == '__main__':
    app.run(debug=True)



# now we have the managerDashbaord created - it needs to be accessed if either the user creates an account OR if the user enters the correct credentials
# this can only happen after the AES encryption is functioning to encrypt and decrypt the password to check between the Master password
# need to also set up the encryption with an enternal library to do the aes encryption


# need to use a quick local storage to then be able to access anywhere in the project like in the car program
