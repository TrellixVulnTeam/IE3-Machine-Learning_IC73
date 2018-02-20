from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect


"""
@app.route('/index')
def index():
    user = {'username': 'User'}
    posts = [
    {
        'author':{'username': 'Jared'},
        'body':'Yo yo yo'
    },
    {
        'author':{'username' : 'Kenneth'},
        'body':'Hey what\'s up'
    }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


"""


@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(
            form.username.data))
        return redirect('/')
    return render_template('seed.html', title='Sign In', form=form)
