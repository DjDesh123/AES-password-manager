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


# makes the flask app run when this file is executed directly not when imported
if __name__ == '__main__':
    app.run(debug=True)





# need to first make a jinja2 template for both login and sign up as we are basically reusing the same code, and we don't want repetition on the code at all times
# write a getter class basically to get certain attributes if needed but thats more later down the design and implementation route
# need to create a database with sqlAlchemy .db for a slower storage but stores without needing an I/O file
# need to use a quick local storage to then be able to access anywhere in the project like in the car program
