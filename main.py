from flask import Flask, request, redirect, render_template, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://blogz:blogz@localhost:8889/blogz'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = "b'\xd3\xea?\x7f>\xfdV\xb5\xbb\x87N$\xdc\x032\x06"


class Blog (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    blog = db.Column(db.String(1120))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


    def __init__(self, title, blog_post, user):
        self.title = title
        self.blog_post = blog_post
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
def bef_request():
    allowed_routes = ['login', 'signUp', 'blog', 'index']
    if request.endpoint not in allowed_routes and 'username' not in session:
        return redirect('/login')

@app.route('/blog', methods=['GET', 'POST'])
def index():
    blogs = Blog.query.all()
    return render_template('blog.html', title="BLOG!", blogs=blogs)
    

@app.route('/new_post', methods=['POST', 'GET'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        blog_post = request.form['blog']
        title_error = ""
        body_error = ""
        user_id = User.query.filter_by(username=session['username']).first()
        #new_entry = Blog(blog_post, blog_post, user_id)

        if len(title) <1:
            title_error = "No Title"

        if len(blog_post) <1:
            body_error = "No Body"

        if len(title) >1 and len(blog_post) >1:

            #new_entry = (Blog(title, blog_post, user_id))
            new_entry = Blog(title, blog_post, user_id)
            db.session.add(new_entry) 
            db.session.commit()
            blog_post = Blog.query.order_by('-id').first()
           # queryparameter ="/single_post?id=" + str(blog_post.id)

           # return redirect(queryparameter)
            return render_template('single_post.html', blog_post=blog_post)
        else:
            return render_template('new_post.html', title_error=title_error, body_error=body_error)

    if request.method == 'GET':
        return render_template('new_post.html')



@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method =='POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            session['username'] = username
            return redirect('/newpost')
        else:
            username_error = "please reenter username"
            password_error = "pleae reenter password"
    if request.method == 'GET':
        return render_template('login.html')

@app.route('/signup', methods=['POST', 'GET'])
def signUp():
    if request.method == 'POST':
            #signUp = request.args.get("id")

            password = request.form['password']
            username = request.form['username']
            verify = request.form['verify']
            email = request.form['email']
           # error = request.form['error']

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
                #  return redirect('/welcome?username={0}'.format(username))
                new_user =(User(username, password))
                db.session.add(new_user)
                db.session.commit()
                session['username'] = username
                return redirect('/new_post')
            else:
                return render_template('signUp.html', username_error=username_error, username=username, password_error=password_error, password=password, email_error=email_error, email=email, verify=verify,password_check_error=password_check_error)
    else:
        return render_template('signUp.html')

@app.route('/logout')
def logout():
    del session['username']
    return redirect('/') 


if __name__ == '__main__':
    app.run()