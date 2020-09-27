from flask import render_template
from app import app
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    print(posts)
    for post in posts:
        print(post["author"]["username"])
        print(post["body"])
    return render_template('index.html', title='Home', user=user, posts=posts)