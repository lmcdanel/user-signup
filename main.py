from flask import Flask, request, redirect, render_template
import cgi
import os



app = Flask(__name__) # app will be the object created by the constructor
app.config['DEBUG'] = True #is a variable controlled by Python that tells code what module it's in.


@app.route("/")
def user_signup():
    return render_template('signup.html')


def blank(input):
    if input:
        return True
    else:
        return False

def length(input):
    if len(input) > 2 and len(input) < 21:
        return True
    else:
        return False

def email_symbol_verify(input):
    if input.find('@') != -1:
        return True
    else:
        return False

def email_period_verify(input):
    if input.find('.') != -1:
        return True
    else:
        return False

@app.route("/", methods=['POST'])
def user_signup_complete():


    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']



    username_error = ""
    password_error = ""
    verify_password_error = ""
    email_error = ""


    blank_user_error = "Please enter a Username"
    blank_password_error = "Please enter a password"
    blank_email_error = "Please enter an email address"
    reenter_password = "Please re-enter password"
    count_error = "must be 3-20 characters"
    spaces_error = "cannot contain spaces"

    # THIS IS THE PASSWORD VALIDATION

    if not blank(password):
        password_error = blank_password_error
        password = ''
        verify_password = ''
    elif not length(password):
        password_error = "Password " + count_error
        password = ''
        verify_password = ''
        verify_password_error = ''
    else:
        if " " in password:
            password_error = "Password " + spaces_error
            password = ''
            verify_password = ''
            verify_password_error = ''

    if password != verify_password:
        verify_password_error = "Passwords do not match"
        password = ''
        verify_password = ''
        password_error = 'Passwords do not match'




    if not blank(username):
        username_error = blank_user_error
        password = ''
        verify_password = ''
        #password_error = reenter_password
        #verify_password_error = reenter_password
    elif not length(username):
        username_error = "Username " + count_error
        password = ''
        verify_password = ''
        #password_error = reenter_password
        #verify_password_error = reenter_password
    else:
        if " " in username:
            username_error = "Username " + spaces_error
            password = ''
            verify_password = ''
            #password_error = reenter_password
            #verify_password_error = reenter_password



    if not blank(email):
        password = ''
        verify_password = ''
    else:
        if not email_symbol_verify(email):
            email_error = "Email should contain the @ symbol and a period"
            password = ''
            verify_password = ''

        elif not email_period_verify(email):
            email_error = "Email must contain a period"
            password = ''
            verify_password = ''

        else:
            if " " in email:
                email_error = "Email " + spaces_error
                password = ''
                verify_password = ''



    if not username_error and not password_error and not verify_password_error and not email_error:
        username = username
        return redirect('/greeting?username={0}'.format(username))
    else:
        return render_template('signup.html', username_error=username_error, username=username,
        password_error=password_error, password=password, verify_password_error=verify_password_error,
        verify_password=verify_password, email_error=email_error, email=email)



@app.route('/greeting')
def valid_signup():
    username = request.args.get('username')
    return render_template('greeting.html', username=username)

app.run()
