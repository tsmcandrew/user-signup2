from flask import Flask, request, redirect, render_template
import cgi
import os 


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/validate-signup")
def index():
    
    return render_template('index.html')

@app.route("/validate-signup", methods=["GET", "POST"])
def validate_signup():

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if username == '' or ' ' in username or len(username) < 3 or len(username) > 20: 
        username_error = "That's not a valid username"
        #username = ''
    
    if password == '' or ' ' in password or len(password) < 3 or len(password) > 20: 
        password_error = "That's not a valid password"
        password = ''

    if verify == '' or verify != password: 
        verify_error = "Passwords don't match"
        verify = '' 

    a = {}
   
    for b in email:
        if b not in a:
            a[b] = 1
        else:
            a[b] += 1

    if a['@'] > 1 or a['.'] > 1 or ' ' in email or len(email) < 3 or len(email) > 20: 
        email_error = "That's not a valid email"
        #email = ''       
    
    if password_error and verify_error and not username_error and not email_error: 
        username = request.form['username']
        email = request.form['email']
        password = ''
        verify = '' 

    if not username_error and not password_error and not verify_error and not email_error:
        username = request.form['username']
        return redirect('greeting.html?username={0}'.format(username))
    else: 
        return render_template("/index.html", username=username, 
        password='', verify='', email=email, username_error=username_error, 
        password_error=password_error, verify_error=verify_error, 
        email_error=email_error)


@app.route("/greeting.html", methods=['GET', 'POST'])
def hello():

    username = request.args.get('username')
    return '<h1>Welcome, {0}.'.format(username)


app.run()
