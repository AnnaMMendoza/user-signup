from flask import Flask, request, render_template, redirect
import cgi
import string

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template("signup.html")

@app.route("/signup.html", methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    passwordv = request.form['passwordv']
    email = request.form['email']

    username_error = ""
    pass_error = ""
    passv_error = ""
    email_error = ""
    
# field validation tests - username (no spaces, >3 and <20 characters)
    if not username:
        username_error = "Please enter a User Name"

    if " " in username:
        username_error = "No spaces allowed in User Name"

    if len(username) < 3 or len(username) > 20:
        username_error = "User Name length incorrect. Must be > 3 and < 20 characters"

# password validation - password (no spaces, >3 and <20 characters) & must match password verify
    if password == "":
        pass_error = "Please enter a password"

    if " " in password:
        pass_error = "Passwords may not contain spaces"

    if len(password) < 3 or len(password) > 20:
        pass_error = "Password length must be > 3 and < 20 characters"
        
# password re-entry MUST match password!
    if passwordv != password:
        passv_error = "Password entries do not match, please re-enter"
        passwordv = ""

    if " " in password:
        passv_error = "Passwords may not contain spaces"
        passwordv = ""

# email entry validation, optional, entry must have one '@' and a single '.'
    if email == "":
        email_error = ""
        if len(username_error)== 0 and len(pass_error)== 0 and len(email_error)== 0:
            return render_template("welcome.html", username=username)
    else:
        if ' ' in email:
            email_error = "Invalid Email"
        if '@' not in email:
            email_error = "Invalid Email"
        if '.' not in email:
            email_error = "Invalid Email"
        if len(email) > 0 and (len(email) < 3 or len(email) > 20):
            email_error = "Email Length Incorrect, must be > 3 characters and < 20 characters"
           
# if all the above tests are passed and there are no errors, this directs the user to the Welcome page    
    if len(username_error)== 0 and len(pass_error)== 0 and len(email_error)== 0:
        return render_template("welcome.html", username=username)
    else:
        return render_template("signup.html", username=username, username_error=username_error, pass_error=pass_error, passv_error=passv_error,  email=email, email_error=email_error)

app.run()