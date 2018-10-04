#readme file to expand on the user sign-up project to include db functions to accept login data and query db to qualify
    a sign-in function. 
    
    1. we already have a sign-up validation. need to add function to add the user input data into a sql db. 
        from flask import Flask, request, redirect, render_template
        from flask_sqlalchemy import SQLAlchemy 

        app = Flask(__name__)
        app.config['DEBUG'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://get-it-done:get-it-done@localhost:8889/get-it-done'
        app.config['SQLALCHEMY_ECHO'] = True

        db = SQLAlchemy(app)

        class login_data(db.Model): 

            id = db.Column(db.Integer, primary_key = True)
            username = db.Column(db.String(120))
            password = db.Column(db.String(120))
            email = db.Column(db.String(120))
            

            def __init__(self, name):
                self.name = name
                
        @app.route('/', methods=['POST', 'GET'])
        def index():

            if request.method == 'POST':
                login_name = request.form['username']
                new_name = login_data(login_name)
                login_password = request.form['password']
                new_password = login_data(login_password)
                login_email = requst.form['email']
                new_email = login_data(login_email)
                db.session.add(new_name, new_password, new_email)
                db.session.commit()

            return render_template('login.html, title="Login")
        
        @app.route('/login', methods=['POST', 'GET'])
        def login_verification():
            username = ''
            password = ''
            if request.method == 'POST': 
                login_name = request.form['username']
                login_password = request.form['password']
                validate = login_data.query.where(username==login_name AND password==login_password).all()
                if validate == True: 
                    return redirect('greeting.html?username={0}'.format(username))
                else: 
                    return render_template('/login', username='', password='', login_error=login_error)
            
                

           # .............working on completing db set up and query for validation. 
           
           
           
           
           
           #tasks = Task.query.all()
            #tasks = Task.query.filter_by(completed=False).all()
            #completed_tasks = Task.query.filter_by(completed=True).all()
            #return render_template('todos.html',title="Get It Done!", 
            #    tasks=tasks, completed_tasks=completed_tasks) 
