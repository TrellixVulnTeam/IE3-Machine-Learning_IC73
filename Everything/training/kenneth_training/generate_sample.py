#!/usr/bin/env python
# -*- coding: utf-8 -*-

from keras.models import Sequential, load_model
from keras.layers import Dense, Activation, LSTM, TimeDistributed
from keras import optimizers
import numpy as np
import h5py
import pickle
from generate_with_seed import *


pickle_file = "word_mappings.p"
with open(pickle_file, "rb") as picked :
    ix_to_char,char_to_ix = pickle.load(picked)

def generate_text(model, length):
    ix = [np.random.randint(VOCAB_SIZE)]
    y_char = [ix_to_char[ix[-1]]]
    X = np.zeros((1, length, VOCAB_SIZE))
    for i in range(length):
        X[0, i, :][ix[-1]] = 1
        print(ix_to_char[ix[-1]], end=" ")
        ix = np.argmax(model.predict(X[:, :i+1, :])[0], 1)
        y_char.append(ix_to_char[ix[-1]])
    return ('').join(y_char)
f = open("half.txt", 'r', encoding="utf-8")

all_words = map(lambda l: l.split(" "), f.readlines())
# vocab = {}
more_words = []

for line in all_words :
    #value = unicode(value, "utf-8", errors="ignore")
    temp = line[:-1]
    for word in temp :
        word = word.lower()
        length = len(word)
        while length > 0 and (word[length-1] == "." or word[length-1] == ")" or word[length-1] == '\n' or word[length-1] == ";" or word[length-1] == ":" or word[length-1] == ","):
            word = word[0:length-1]
            length = len(word)
        while length > 0 and word[0] == "("  :
            word = word[1:length]
            length = len(word)
    #    if not(hash(word) in vocab) :
            # vocab.append(word)
        more_words.append(word)


data = []
for key in more_words :
    word = key
    length = len(word)
    if length > 0:
        data.append(word)

chars = list(set(data))
VOCAB_SIZE = len(chars)
HIDDEN_DIM = 200
LAYER_NUM  = 2
BATCH_SIZE = 10
GENERATE_LENGTH = 100

model = Sequential()

model.add(LSTM(HIDDEN_DIM, input_shape=(None, VOCAB_SIZE), return_sequences=True))
for i in range(LAYER_NUM - 1):
    model.add(LSTM(HIDDEN_DIM, return_sequences=True))
model.add(TimeDistributed(Dense(VOCAB_SIZE)))
model.add(Activation('softmax'))
#adam = optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False) # Adam optimizer Jared told us to use
model.compile(loss="categorical_crossentropy", optimizer="adam")

nb_epoch = 0
#load weights in future runs
model.load_weights("checkpoint_200_epoch_140.hdf5")
print("\n")
generate_with_seed(model, 'word_mappings.p', 1000)
print("\n")
