from flask import render_template
from app import app

@app.route('/')

@app.route('/index')
def index():
    user = {'username':'Ren'}
    posts = [
                {
                    'author':{'username':'susan'},
                    'body':'The avengers movie was so cool!'
                },
                {
                    'author':{'username':'john'},
                    'body':'Beautiful day in Portland!'
                }
            ]
    return render_template('index.html',title='Home',user=user,posts=posts)

