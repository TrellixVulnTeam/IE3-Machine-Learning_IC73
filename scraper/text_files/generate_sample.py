#!/usr/bin/env python
# -*- coding: utf-8 -*-

from keras.models import Sequential, load_model
from keras.layers import Dense, Activation, LSTM, TimeDistributed
from keras import optimizers
import numpy as np
import h5py

file_name = "all_files.txt"
data = open(file_name, 'r').read()
data = data.lower()
data = list(data.rstrip())
chars = list(set(data))
VOCAB_SIZE = len(chars)
SEQ_LENGTH = 1000
length = int(len(data)/SEQ_LENGTH)

# Creates the mapping between the characters and orders the characters by least to most frequent I think
ix_to_char = {ix:char for ix, char in enumerate(chars)}
char_to_ix = {char:ix for ix, char in enumerate(chars)}

print(ix_to_char)

def generate_text(model, length):
    ix = [np.random.randint(VOCAB_SIZE)]
    y_char = [ix_to_char[ix[-1]]]
    X = np.zeros((1, length, VOCAB_SIZE))
    for i in range(length):
        X[0, i, :][ix[-1]] = 1
        print(ix_to_char[ix[-1]], end="")
        ix = np.argmax(model.predict(X[:, :i+1, :])[0], 1)
        y_char.append(ix_to_char[ix[-1]])
    return ('').join(y_char)


model = load_model('my_model20.h5')
#generate_text(model, 300)
