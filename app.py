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



"""
the plan is fairly simple for these next steps of the program 
- create a js file for sign up page 
- to use fetch syntax to send both login and signup.js to the argon2.py file
- then pass the information to AES encryption 
- put inside the LogInDatabase.py file
- then check if the credentials in the database is correct for what the user enters 
- to then redirect the dashboard html file
"""