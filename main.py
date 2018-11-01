# from flask import Flask, request, redirect, render_template, session
# from flask_sqlalchemy import SQLAlchemy 

# app = Flask(__name__)
# app.config['DEBUG'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://blog:blog@localhost:8889/blog'
# app.config['SQLALCHEMY_TRACK_MONDIFICATIONS'] = True
# app.secret_key = 'as8d7f98a!@qw546era#$#@$'
# db = SQLAlchemy(app)

# class Blog(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(120))
#     body = db.Column(db.Text)
#     owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#     def __init__(self, title, body, owner):
#         self.title = title
#         self.body = body
#         self.owner = owner



# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(120), unique=True)

#     blogs = db.relationship('Blog', backref='owner')

#     def __init__(self, username, password):
#         self.username = username
#         self.password = password 



# @app.before_request
# def require_login():
#     allowed_routes = ['login', 'signup', 'blog', 'index']
#     if request.endpoint not in allowed_routes and 'username' not in session:
#         return redirect('/login')

# @app.route('/')
# def index():
#     users = User.query.all()
#     return render_template('index.html', users=users)

# @app.route('/login', methods=['POST', "GET"])
# def login():
#     username_error = ""
#     password_error = ""

#     if request.method == 'POST':
#         password = request.form['password']
#         username = request.form['username']
#         user = User.query.filter_by(username=username).first()


#         if not user:
#             return render_template('login.html', password_error="You username or password was incorrect.")
#         else:
#             return render_template('login.html', password_error="Your username or password was incorrect.")

#     return render_template('login.html')

# @app.route("/signup", methods=['POST', 'GET'])
# def signup():
#     if request.method =='POST':
#         username = request.form['username']
#         password = request.form['password']
#         verify = request.form['verify']
#         exist = User.query.filter_by(username=username).first()

#         username_error = ""
#         password_error = ""
#         verify_error = ""

#         if username == "":
#             username_error = "Enter username"
#         elif len(username) <= 3 or len(username) > 20:
#             username_error = "Username must between 3 and 20 chareaters long"
#         elif " " in username:
#             username_error = "Username cannot contain any spaces"
#         if password == "":
#             password_error = "Please enter a password"
#         elif len(password) <= 3:
#             password_error = "Password must be greater than 3 characters long"
#         elif " " in password:
#             password_error = "Password cannot contain any spaces"
#         if password != verify or verify == "":
#             verify_error = "Passwords do not match"
#         if exist:
#             username_error = "Username already taken"

#         if len(username) > 3 and len(password) > 3 and password == verify and not exist:
#             new_user = User(username, password)
#             db.session.add(new_user)
#             db.session.commit()
#             session['username'] = username
#             return redirect('/single_post')
#         else:
#             return render_template('signup.html',
#             username=username,
#             username_error=username_error,
#             password_error=password_error,
#             verify_error=verify_error
#             )

#     return render_template('signup.html')


# @app.route('/blog', methods=['POST', 'GET'])
# def blog():
#     blog_id = request.args.get('id')
#     user_id = request.args.get('userid')
#     post = request.args.get('post')

#     if blog_id:
#         post = Blog.query.filter_by(id=blog_id).first()
#         return render_template("post.html", title=post.title, body=post.body, user=post.owner.username, user_id=post.owner_id)
#     if user_id:
#         entries = Blog.query.filter_by(owner_id=user_id).all()
#         return render_template('user.html', entries=entries)
        
#     return render_template('blog.html', post=post)

# @app.route('/single_post')
# def post():
#     return render_template('single_post.html', title="New Post")

# @app.route('/single_post')
# def single_post():
#     title = request.form['title']
#     body = request.form["body"]
#     owner = User.query.filter_by(username=session['username']).first()

#     title_error = ""
#     body_error = ""

#     if title == "":
#         title_error = "Title required"
#     if body == "":
#         body_error = "Content required"

#     if not title_error and not body_error:
#         new_post = Blog(title, body, owner)
#         db.session.add(new_post)
#         db.session.commit()
#         page_id = new_post.id
#         return redirect("/blog?id={0}".format(page_id))
#     else:
#         return render_template("single_post.html",
#             title = title,
#             body = body,
#             title_error = title_error,
#             body_error = body_error
#             )


# @app.route('/logout')
# def logout():
#     del session['username']
#     return redirect('/')

# if __name__ == '__main__':
#     app.run()
















# from flask import Flask, request, redirect, render_template, session
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['DEBUG'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://blogz:blogz@localhost:8889/blogz'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.secret_key = 'as8d7f98a!@qw546era#$#@$'
# db = SQLAlchemy(app)

# class Blog(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(120))
#     body = db.Column(db.Text)
#     owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    
#     def __init__(self, title, body, owner):
#         self.title = title
#         self.body = body
#         self.owner = owner
        


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(120), unique=True)
    
#     blogs = db.relationship('Blog', backref='owner')

#     def __init__(self, username, password):
#         self.username = username
#         self.password = password


# @app.before_request
# def require_login():
#     allowed_routes = ['login', 'signup', 'blog', 'index', 'static']
#     if request.endpoint not in allowed_routes and 'username' not in session:
#         return redirect('/login')


# @app.route('/')
# def index():
#     users = User.query.all()
#     return render_template('index.html', users=users)


# @app.route('/login', methods=['POST','GET'])
# def login():
#     username_error = ""
#     password_error = ""

#     if request.method == 'POST':
#         password = request.form['password']
#         username = request.form['username']
#         user = User.query.filter_by(username=username).first()

       
#         if not user:
#             return render_template('login.html', username_error="Username does not exist.")
#         else:
#             return render_template('login.html', password_error="Your username or password was incorrect.")

#     return render_template('login.html')


# @app.route("/signup", methods=['POST', 'GET'])
# def signup():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         verify = request.form['verify']
#         exist = User.query.filter_by(username=username).first()

#         username_error = ""
#         password_error = ""
#         verify_error = ""

#         if username == "":
#             username_error = "Please enter a username."
#         elif len(username) <= 3 or len(username) > 20:
#             username_error = "Username must be between 3 and 20 characters long."
#         elif " " in username:
#             username_error = "Username cannot contain any spaces."
#         if password == "":
#             password_error = "Please enter a password."
#         elif len(password) <= 3:
#             password_error = "Password must be greater than 3 characters long."
#         elif " " in password:
#             password_error = "Password cannot contain any spaces."
#         if password != verify or verify == "":
#             verify_error = "Passwords do not match."
#         if exist:
#             username_error = "Username already taken."
        
#         if len(username) > 3 and len(password) > 3 and password == verify and not exist:
#             new_user = User(username, password)
#             db.session.add(new_user)
#             db.session.commit()
#             session['username'] = username
#             return redirect('/newpost')
#         else:
#             return render_template('signup.html',
#             username=username,
#             username_error=username_error,
#             password_error=password_error,
#             verify_error=verify_error
#             )

#     return render_template('signup.html')


# @app.route('/blog', methods=['POST', 'GET'])
# def blog():
#     blog_id = request.args.get('id')
#     user_id = request.args.get('userid')

#     #posts = Blog.query.order_by(Blog.pub_date.desc())

#     if blog_id:
#         post = Blog.query.filter_by(id=blog_id).first()

#     return render_template("post.html"), (title=post.title, body=post.body, user=post.owner.username, user_id=post.owner_id)
#     if user_id:
#         entries = Blog.query.filter_by(owner_id=user_id).all()
#         return render_template('user.html', entries=entries)

#     return render_template('blog.html', posts=posts)

# @app.route('/newpost')
# def post():
#     return render_template('newpost.html', title="New Post")

# @app.route('/newpost', methods=['POST', 'GET'])
# def newpost():
#     title = request.form['title']
#     body = request.form["body"]
#     owner = User.query.filter_by(username=session['username']).first()

#     title_error = ""
#     body_error = ""

#     if title == "":
#         title_error = "Title required."
#     if body == "":
#         body_error = "Content required."

#     if not title_error and not body_error:
#         new_post = Blog(title, body, owner)
#         db.session.add(new_post)
#         db.session.commit()
#         page_id = new_post.id
#         return redirect("/blog?id={0}".format(page_id))
#     else:
#         return render_template("newpost.html",
#             title = title,
#             body = body,
#             title_error = title_error,
#             body_error = body_error
#         )

# @app.route('/logout')
# def logout():
#     del session['username']
#     return redirect('/')

# if __name__ == '__main__':
#     app.run()















from flask import Flask, request, redirect, render_template, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://blogz:blogz@localhost:8889/blogz'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = "b'\xd3\xea?\x7f>\xfdV\xb5\xbb\x87N$\xdc\x032\x06"
#db = SQLAlchemy(app)

class Blog (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    blog = db.Column(db.String(1120))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


    def __init__(self, title, blog_post, user):
        self.title = title
        self.blog = blog_post
        self.user = user



class User (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120))
    password = db.Column(db.String(1120))
    blogs = db.relationship('Blog', backref='user')

    def __init__(self, username, password):
        self.username = username
        self.password = password 

@app.before_request
def require_login():
    allowed_routes = ['login', 'signUp', 'index']
    if request.endpoint not in allowed_routes and 'username' not in session:
        return redirect('/login')

@app.route('/blog', methods=['GET', 'POST'])
def index():

    #if there is an id in the querey get the blog by that id and render a single post
    if request.args.get("id"):
        post_id = request.args.get("id")
        blog_post = Blog.query.get(post_id)
        return render_template("single_post.html", blog_post=blog_post)
    
    elif request.args.get("user"):
        user_id = request.args.get("user")
        user = User.query.get(user_id)
        blogs = Blog.query.filter_by(user=user).all()
        return render_template("single_user.html", blogs=blogs)


    #if there is not an id in the query parameter get all blogs
    users = User.query.all()
    blogs = Blog.query.all()
    return render_template('blog.html', title="BLOG!", users=users, blogs=blogs)
    
#@app.route('/new_post')
#def post():
 #   return render_template('new_post.html', title="New Post")

@app.route('/new_post', methods=['POST', 'GET'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        blog_body = request.form['body']

        title_error = ""
        body_error = ""

        user_id = User.query.filter_by(username=session['username']).first()
        #new_entry = Blog(title, blog_post, user_id)

        if len(title) <1:
            title_error = "No Title"

        if len(blog_body) <1:
            body_error = "No Body"

        if not title_error and not body_error:

            #new_entry = (Blog(title, blog_post, user_id))
            new_entry = Blog(title, blog_body, user_id)
            db.session.add(new_entry) 
            db.session.commit()
            blog_post = Blog.query.order_by('-id').first()
            queryparameter ="/blog?id=" + str(blog_post.id)

            return redirect(queryparameter)
            #return render_template('single_post.html', blog_post=blog_post)
        else:
            return render_template('new_post.html', title_error=title_error, body_error=body_error)

    if request.method == 'GET':
        return render_template('new_post.html')


@app.route('/login', methods=['POST','GET'])
def login():

    if request.method == 'POST':
        password = request.form['password']
        username = request.form['username']
        user = User.query.filter_by(username=username).first()

        username_error = ""
        password_error = ""


        if len(username) < 1: 
            username_error ="Enter username"

        if len(password) < 1:
            password_error = "Enter Password"

        if len(username_error)> 1 or len(password_error) > 1: 
            return render_template('login.html', password_error=password_error, username_error=username_error)
        elif not user and user.password:
            return render_template('login.html', username_error="Username does not exist")
        elif user and user.password != password:
            return render_template('login.html', password_error="password is not correct")
        else:
            session['username'] = username
            return redirect('/new_post')

    if request.method =='GET':
        return render_template('login.html')




# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     if request.method =='POST':
#         username = request.form['username']
#         password = request.form['password']
#         user = User.query.filter_by(username=username).first()
#         if user and user.password == password:
#             session['username'] = username
#             return redirect('/newpost')
#         else:
#             username_error = "please reenter username"
#             password_error = "pleae reenter password"
#     if request.method == 'GET':
#         return render_template('login.html')

@app.route('/signup', methods=['POST', 'GET'])
def signUp():
    if request.method == 'POST':
            #signUp = request.args.get("id")

            password = request.form['password']
            username = request.form['username']
            verify = request.form['verify']
            email = request.form['email']
            #error = request.form['error']

            username_error = ''
            password_error = ''
            password_check_error = ''
            email_error = ''

            error_required = "Required field"
            error_re_enter_password = "Please re-enter password"
            error_chara_count = "must be between 3 and 20 characters"
            error_no_spaces = "must not contain spaces"


            if len(password) < 1:
                password_error = error_required
                password = ''
                password_check = ''
            if not len(password) > 2 and len(password) < 21:
                password_error = "Password " + error_chara_count
                password = ''
                password_check = ''
                password_check_error = error_re_enter_password
            
            if " " in password:
                password_error = "Password " + error_no_spaces
                password = ''
                password_check = ''
                password_check_error = error_re_enter_password


            if verify != password:
                password_check_error = "Passwords must match"
                password = ''
                password_check = ''
                password_error = 'Passwords must match'
                    

            if len(username) < 1:
                username_error = error_required
            if not len(username) > 2 and len(username) < 21:
                username_error = "Username " + error_chara_count

            if " " in username:
                username_error = "Username " + error_no_spaces



            if not len(email) < 1:
                
                if not len(email) < 1:
                    email_error = "Email " + error_chara_count
                
                elif "@" not in email:
                    email_error = "Email must contain the @ symbol"
                
                elif "." not in email:
                    email_error = "Email must contain ."
                
                elif " " in email:
                    email_error = "Email " + error_re_enter_password
                


            if not username_error and not password_error and not password_check_error and not email_error:
                new_user =(User(username, password))
                db.session.add(new_user)
                db.session.commit()
                session['username'] = username
                return redirect('/new_post')
            else:
                return render_template('signUp.html', username_error=username_error, username=username, password_error=password_error, password=password, email_error=email_error, email=email, verify=verify,password_check_error=password_check_error)
    else:
        return render_template('signUp.html')


# @app.route('/blog', methods=['POST', 'GET'])
# def blog():
#     blog_id = request.args.get('id')
#     user_id = request.args.get('userid')
#     post = request.args.get('post')

#     if blog_id:
#         post = Blog.query.filter_by(id=blog_id).first()
#         return render_template("post.html", title=post.title, body=post.body, user=post.owner.username, user_id=post.owner_id)
#     if user_id:
#         entries = Blog.query.filter_by(owner_id=user_id).all()
#         return render_template('user.html', entries=entries)
        
#     return render_template('blog.html', post=post)


@app.route('/all_users')
def all_users():
    all_users=User.query.all()

    return render_template('all_users.html', all_users=all_users)

@app.route('/logout')
def logout():
    del session['username']
    return render_template("logout.html") 


if __name__ == '__main__':
    app.run()