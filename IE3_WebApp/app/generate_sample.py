#!/usr/bin/env python
# -*- coding: utf-8 -*-

from keras.models import Sequential, load_model
from keras.layers import Dense, Activation, LSTM, TimeDistributed
from keras import optimizers
import numpy as np
import h5py
import pickle
"""
num = input('Which model would you like to use? (1 for lotr, 2 for char recipe, 3 for word recipe, 4 for poetry): ')
model = None
pickl = None
file_name = None

print(num)

# file_name is included at this point just in case... you know?
if num == 1:
    model = load_model('./models/tolkienmodel230.h5')
    file_name = './corpi/TolkiensMiddleEarth.txt'
    pickl = './pickles/lotr_pickle.p'
elif num == 2:
    model = load_model('./models/char_recipe_model190.h5')
    file_name = './corpi/parsed_text.txt'
    pickl = './pickles/char_recipe_parsed_pickle.p'
elif num == 3:
    model = load_model('./models/KENNETHSMODEL')
    file_name = './corpi/all_files.txt'
    pickl = './pickles/word_mappings.p'
elif num == 4:
    model = load_model('./models/poemmodel100.h5')
    file_name = './corpi/poem_corpusv2.txt'
    pickl = './pickles/poem_pickev2.p'

# data = open(file_name, 'r').read() --> Don't need this (yet?)
# data = data.lower()
# data = list(data.rstrip())
# chars = list(set(data))
"""
# Arguments: (model, name of pickle file, length of sample)
def generate_with_seed(seed, model, picklename, length):
    # LOAD THE PICKLE
    with open(picklename, 'rb') as handle:
        [ix_to_char, char_to_ix] = pickle.load(handle)

    VOCAB_SIZE = len(ix_to_char)

    print("\n")

    ix = [char_to_ix[seed[-1]]]
    y_char = [ix_to_char[ix[-1]]]
    X = np.zeros((1, length, VOCAB_SIZE))
    for t, char in enumerate(seed):
        X[0, t, :][char_to_ix[char]] = 1

    for i in range(length):
        X[0, i, :][ix[-1]] = 1
        print(ix_to_char[ix[-1]], end="")
        import pdb; pdb.set_trace()
        ix = np.argmax(model.predict(X[:, :i+1, :])[0], 1)
        y_char.append(ix_to_char[ix[-1]])
    return ('').join(y_char)
"""
print("\n")
generate_with_seed(model, pickl, 500)
print("\n")
"""

def generate_with_seed_word(seed, model, picklename, length):
    # with open(picklename, 'rb') as handle:
    #     [ix_to_char, char_to_ix] = pickle.load(handle)
    #
    # VOCAB_SIZE = len(ix_to_char)
    # # seed = input("enter seed text: ")
    # # print("\n")
    #
    # ix = [char_to_ix[seed[-1]]]
    # y_char = [ix_to_char[ix[-1]]]
    # X = np.zeros((1, length, VOCAB_SIZE))
    #
    # # for t, char in enumerate(seed):
    # #     X[0, t, :][char_to_ix[char]] = 1
    # X[0][char_to_ix[seed]] = 1
    #
    # for i in range(length):
    #     X[0,i,:][ix[-1]] = 1
    #     print(ix_to_char[ix[-1]], end=" ")
    #     ix = np.argmax(model.predict(X[:, :i+1, :])[0], 1)
    #     y_char.append(ix_to_char[ix[-1]])
    # return ('').join(y_char)


    with open(picklename, 'rb') as handle:
        [ix_to_char, char_to_ix] = pickle.load(handle)

    VOCAB_SIZE = len(ix_to_char)
    #seed = input("enter seed text: ")
    print("\n")

    ix = [np.random.randint(VOCAB_SIZE)]
    y_char = [ix_to_char[ix[-1]]]
    X = np.zeros((1, length, VOCAB_SIZE))

    for i in range(length):
        X[0,i,:][ix[-1]] = 1
        print(ix_to_char[ix[-1]], end=" ")
        import pdb; pdb.set_trace()
        ix = np.argmax(model.predict(X[:, :i+1, :])[0], 1)
        y_char.append(ix_to_char[ix[-1]])
    return ('').join(y_char)


# def generate_text_word(model, length):
#     ix = [np.random.randint(VOCAB_SIZE)]
#     y_char = [ix_to_char[ix[-1]]]
#     X = np.zeros((1, length, VOCAB_SIZE))
#     for i in range(length):
#         X[0, i, :][ix[-1]] = 1
#         print(ix_to_char[ix[-1]], end=" ")
#         ix = np.argmax(model.predict(X[:, :i+1, :])[0], 1)
#         y_char.append(ix_to_char[ix[-1]])
#     return ('').join(y_char)
