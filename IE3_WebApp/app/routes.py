from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect, request
from .generate_sample import generate_with_seed, generate_with_seed_word
from .get_text import text_query
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
        corpus = None
        if modelType == 1:
                model = load_model("./app/models/char_recipe_model190.h5")
                pickle = "./app/pickles/char_recipe_parsed_pickle.p"
                corpus = "./app/corpi/parsed_text.txt"
                output = generate_with_seed(seed, model, pickle, seqLen)
        elif modelType == 2:
                model = load_model("./app/models/final_model_word_recipes.h5")
                pickle = "./app/pickles/word_mappings.p"
                corpus = "./app/corpi/parsed_text.txt"
                output = generate_with_seed_word(seed, model, pickle, seqLen)
        elif modelType == 3:
                model = load_model("./app/models/poemmodel100.h5")
                pickle = "./app/pickles/poem_pickev2.p"
                corpus = "./app/corpi/poem_corpusv2.txt"
                output = generate_with_seed(seed, model, pickle, seqLen)
        elif modelType == 4:
                model = load_model("./app/models/tolkienmodel230.h5")
                pickle = "./app/pickles/lotr_pickle.p"
                corpus = "./app/corpi/TolkiensMiddleEarth.txt"
                output = generate_with_seed(seed, model, pickle, seqLen)


        found_text = text_query(corpus, seed, seqLen)
        session['output'] = output
        session['source'] = found_text

        if seed!=None:
            return redirect('/output')

    return render_template('webapp.html', title="Generate")

@app.route('/output', methods = ['POST', 'GET'])
def output():

    if request.method == 'POST':
        return redirect('/generate')

    output = session.get('output', None)
    source = session.get('source', None)

    return render_template('results.html', source=source, generated=output)







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
