from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect, request
from .generate_sample import generate_with_seed
from keras.models import Sequential, load_model
from keras.layers import Dense, Activation, LSTM, TimeDistributed
from keras import optimizers
import numpy as np
import h5py
import pickle


session={}

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/generate', methods = ['POST', 'GET'])
def generate():

    if request.method == 'POST':
        seed = request.form.get('seed')
        modelType = request.form.get('modelType')
        seqLen = request.form.get('len')

        seqLen = int(seqLen)
        modelType = int(modelType)
        model = None
        pickle = None
        if modelType == 1:
                model = load_model("./app/models/char_recipe_model190.h5")
                pickle = "./app/pickles/char_recipe_parsed_pickle.p"
        elif modelType == 2:
                model = load_model("./app/models/final_model_word_recipes.h5")
                pickle = "./app/pickles/word_mappings.p"
        elif modelType == 3:
                model = load_model("./app/models/poemmodel100.h5")
                pickle = "./app/pickles/poem_pickev2.p"
        elif modelType == 4:
                model = load_model("./app/models/tolkienmodel230.h5")
                pickle = "./app/pickles/lotr_pickle.p"

        output = generate_with_seed(seed, model, pickle, seqLen)
        session['output'] = output

        if seed!=None:
            return redirect('/output')

    return render_template('webapp.html', title="Generate")

@app.route('/output', methods = ['POST', 'GET'])
def output():
    output = session.get('output', None)
    if request.method == 'POST':
        return redirect('/generate')
    return render_template('results.html', source=output, generated=output)







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
