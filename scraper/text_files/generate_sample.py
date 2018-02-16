#!/usr/bin/env python
# -*- coding: utf-8 -*-

from keras.models import Sequential, load_model
from keras.layers import Dense, Activation, LSTM, TimeDistributed
from keras import optimizers
import numpy as np
import h5py
import pickle

file_name = "TolkiensMiddleEarth.txt"
data = open(file_name, 'r').read()
data = data.lower()
data = list(data.rstrip())
chars = list(set(data))
VOCAB_SIZE = len(chars)
SEQ_LENGTH = 1000
length = int(len(data)/SEQ_LENGTH)

# LOAD THE PICKLE
with open('lotr_pickle.p', 'rb') as handle:
	[ix_to_char, char_to_ix] = pickle.load(handle)

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


model = load_model('tolkienmodel40.h5')
print("\n")
generate_text(model, 300)
print("\n")
