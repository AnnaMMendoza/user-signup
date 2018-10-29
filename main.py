from flask import Flask, request, redirect, render_template
import cgi
import os
import string

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/signup.html')
def display_signup_form():
    username = request.form['username']
    password = request.form['password']
    passwordv = request.form['passwordv']
    email = request.form['email']
    
# field validation tests - username (no spaces, >3 and <20 characters)
    for char in username:
        if char == " ":
            username_error = "ERROR: NO Spaces Allowed"
        else:
            username_error = ""
    if len(username) < 3 or len(username) > 20:
        username_error = "ERROR: User Name length incorrect. Must be > 3 and < 20 Characters"

# password validation - password (no spaces, >3 and <20 characters)
    for char in password:
        if char == " ":
            pass_error = "ERROR: You MUST enter a password, please enter a password"
        else:
            pass_error = ""
    if len(password) < 3 or len(password) > 20:
        pass_error = "ERROR: Password length must be > 3 and < 20 characters"

# password verify validation - passwordv MUST match password
    if passwordv != password:
        passverify_error = "ERROR: Password entries do not match, please re-enter"
    else:
        passverify_error = ""

# email entry validation, optional, blank allowed, entry must have one '@' and a single '.'




    return render_template("signup.html")

@app.route("/")
def index():
    return render_template("signup.html")


app.run()