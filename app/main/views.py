from app.models import Post
from flask import render_template, request, redirect, url_for
from . import main
from .. import db
from datetime import datetime


@main.route('/')
def index():
  
    posts = Post.query.order_by(Post.date_posted.desc()).all()

    return render_template('index.html', posts=posts)

@main.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.filter_by(id=post_id).one()

    return render_template('post.html', post=post)

@main.route('/add')
def add():
    return render_template('add.html')

@main.route('/addpost', methods=['POST'])
def addpost():
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']

    post = Post(title=title, subtitle=subtitle, author=author, content=content, date_posted=datetime.now())

    db.session.add(post)
    db.session.commit()

    return redirect(url_for('.index'))

if __name__ == '__main__':
    app.run(debug=True)