from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup_form.html', title="Signup")

@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)


@app.route("/", methods=['post'])
def validate_stuff():
    username = request.form['username']
    password = request.form['password']
    verify= request.form['verify']
    email = request.form['email']

    username_error= ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if username == '':
        username_error = "That is not a valid username"
    elif ' ' in username:
        username_error = 'that is not a valid username'
    
    if password == '':
        password_error = 'That is not a valid password'
    elif ' ' in password:
        password_error = 'That is not a valid password'
    elif len(password) <= 3 or len(password) > 30:
        password_error = 'that is not a valid password'
    
    if verify != password:
        verify_error = 'those passwords do not match'

    if '@' not in email:
        email_error = 'that is not a valid email address'
    elif '.' not in email:
        email_error = 'that is not a valid email address'
    elif len(email) <= 3:
        email_error = 'your email length is too short'
    elif len(email) > 20:
        email_error = 'your email length is too long'

    if not username_error and not password_error and not verify_error and not email_error:
        return redirect('/welcome?username={0}'.format(username))

    else:
        return render_template('signup_form.html', username=username, username_error=username_error,
                                password_error=password_error,
                                verify_error=verify_error,
                                email_error=email_error)

# if no errors, then reroute them to the welcome page 

app.run()