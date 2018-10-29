from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:Password@localhost:3306/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Blog (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    blog_post = db.Column(db.String(1120))

    def __init__(self, title, blog_post):
        self.title = title
        self.blog_post = blog_post


@app.route('/blog')
def index():
    #it has key blog_id == ''
    #     return individual new_post
    #     return render_template

    # if request has key blog_id
        # retrieve individual blog post
        # render template with individual blog post
        
    blogs = Blog.query.all()

    return render_template('blog.html', title="BLOG!", blogs=blogs)
    

@app.route('/new_post', methods=['POST', 'GET'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        blog_post = request.form['blog']
        title_error = ""
        body_error = ""

        if len(title) <1:
            title_error = "No Title"

        if len(blog_post) <1:
            body_error = "No Body"

        if len(title) >1 and len(blog_post) >1:

            new_entry = (Blog(title, blog_post))
            db.session.add(new_entry) 
            db.session.commit()
            queryparameter ="/single_post?id=" + str(new_entry.id)

            return redirect(queryparameter)
        return render_template('new_post.html', title_error=title_error, body_error=body_error)

    if request.method == 'GET':
        return render_template('new_post.html')

@app.route('/single_post', methods=['GET'])
def single_post():
    #find a blog by id and display that blog
    blogid = request.args.get("id")
    blog_post = Blog.query.get(blogid)


    
    return render_template('single_post.html', blog_post=blog_post)


if __name__ == '__main__':
    app.run()