from datetime import datetime
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

@app.route('/')
def home():
    return "Hello, this is your home page!"

@app.route('/posts', methods=['GET', 'POST'])
def posts():
    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        post = Post(title=post_title, content=post_content)
        db.session.add(post)
        db.session.commit()
        return jsonify({"message": "Post created"}), 201
    if request.method == 'GET':
        posts = Post.query.all()
        data = []
        for post in posts:
            data.append({
                'id': post.id,
                'title': post.title,
                'content': post.content,
                'date_posted': post.date_posted
            })
        return jsonify(data)

if __name__ == '__main__':
    db.create_all()
    app.run()