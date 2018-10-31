from flask import Flask, request, render_template, redirect
import cgi
import string

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template("signup.html")

@app.route("/", methods=['POST'])
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
    if username == "":
        username_error = "You MUST enter a User Name"
    
    if " " in username:
        username_error = "ERROR: No spaces allowed"
    
    if len(username) < 3 or len(username) > 20:
        username_error = "ERROR: User Name length incorrect. Must be > 3 and < 20 Characters"

        return render_template("signup.html", username=username, name_error=name_error)

# password validation - password (no spaces, >3 and <20 characters) & must match password verify
    if " " in password:
        pass_error = "ERROR: Passwords cannot contain spaces"
        # password = ""
        return render_template("signup.html", username=username, name_error=name_error, pass_error)
    
    if len(password) < 3 or len(password) > 20:
        pass_error = "ERROR: Password length must be > 3 and < 20 characters"
        # password = ""
        return render_template("signup.html", username=username, name_error=name_error, pass_error)
        

# password re-entry MUST match password!
    if passwordv != password:
        passv_error = "Password entries do not match, please re-enter"
        passwordv = ""
    
    if " " in password:
        passv_error = "ERROR: Passwords cannot contain spaces"
        passwordv = ""
        return render_template("signup.html", username=username, name_error=name_error, pass_error, passv_error)

# email entry validation, optional, entry must have one '@' and a single '.'
    if ' ' in email:
        email_error = "ERROR: Not a valid email, No spaces allowed"
    if '@' not in email:
        email_error = "ERROR: Not a valid email"
    if '.' not in email:
        email_error = "ERROR: Not a valid email"
    if len(email) > 0 and (len(email) < 3 or len(email) > 20):
        email_error = "ERROR: Email Length Incorrect, must be > 3 characters and < 20 characters"
        return render_template("signup.html", username=username, name_error=name_error, pass_error, passv_error, email_error)

# if all the above tests are passed and there are no errors, this directs the user to the Welcome page    
    if len(username_error)== 0 and len(pass_error)== 0 and len(email_error)== 0:
        return render_template("welcome.html", username=username)
    else:
        return render_template("signup.html", username=username, username_error=username_error, pass_error=pass_error, email=email, email_error=email_error)

app.run()