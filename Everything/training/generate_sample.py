#!/usr/bin/env python
# -*- coding: utf-8 -*-

from keras.models import Sequential, load_model
from keras.layers import Dense, Activation, LSTM, TimeDistributed
from keras import optimizers
import numpy as np
import h5py
import pickle
from generate_with_seed import *

num = input('Which model would you like to use? (1 for lotr, 2 for char recipe, 3 for word recipe, 4 for poetry)')

if (num == 1): # Lord of the Rings
    model = load_model('../Weights/tolkienmodel140.h5')
    file_name = "../Source_text/TolkiensMiddleEarth.txt"
    pickl = '../char_recipe_parsed_pickle.p'
elif (num == 2):
    model = load_model('../char_recipe_model190')
    file_name = "../Source_text/dont_D3L3T3_m3.txt"
    pickl = '../char_recipe_parsed_pickle.p'
elif (num == 3):
    model = load_model('./checkpoint_200_epoch_140.')
    file_name = "../Source_text/dont_D3L3T3_m3.txt"
    pickl = './word_mappings.p'
elif (num == 4):
    model = load_model('../char_recipe_model190')
    file_name = "../Source_text/dont_D3L3T3_m3.txt"
    pickl = 'Josh\'s Pickle'

data = open(file_name, 'r').read()
data = data.lower()
data = list(data.rstrip())
chars = list(set(data))

# Arguments: (model, name of pickle file, length of sample)
def generate_with_seed(model, picklename, length):
    # LOAD THE PICKLE
    with open(picklename, 'rb') as handle:
        [ix_to_char, char_to_ix] = pickle.load(handle)

    VOCAB_SIZE = len(ix_to_char)
    seed = input("Enter seed text: ")
    print("\n")

    ix = [char_to_ix[seed[-1]]]
    y_char = [ix_to_char[ix[-1]]]
    X = np.zeros((1, length, VOCAB_SIZE))
    for t, char in enumerate(seed):
        X[0, t, :][char_to_ix[char]] = 1

    for i in range(length):
        X[0, i, :][ix[-1]] = 1
        print(ix_to_char[ix[-1]], end="")
        ix = np.argmax(model.predict(X[:, :i+1, :])[0], 1)
        y_char.append(ix_to_char[ix[-1]])
    return ('').join(y_char)

print("\n")
generate_with_seed(model, pickl, 500)
print("\n")
