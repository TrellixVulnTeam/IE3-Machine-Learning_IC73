from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect, request



@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/generate', methods = ['POST', 'GET'])
def generate():
    if request.method == 'POST':
        seed = request.form.get('seed')
        if seed!="None":
            flash(seed)
            """DO THINGS HERE"""
            return redirect('/generate')
    return render_template('webapp.html', title="Generate")





"""
@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(
            form.username.data))
        return redirect('/')
    return render_template('seed.html', title='Sign In', form=form)
"""
