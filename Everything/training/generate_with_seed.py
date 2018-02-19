# This is the generate_text file that works with seed text.
# This function assumes that the model of choice has already been selected, and is being passed in as an argument.

from keras.models import Sequential, load_model
from keras.layers import Dense, Activation, LSTM, TimeDistributed
from keras import optimizers
import numpy as np
import h5py
import pickle
import sys
import random

def sample(preds, temperature=1.0):
    # helper function to sample an index from a probability array
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

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

	# ix = [np.random.randint(VOCAB_SIZE)]
	# y_char = [ix_to_char[ix[-1]]]
	# X = np.zeros((1, length, VOCAB_SIZE))
	# for i in range(length):
	# 	X[0, i, :][ix[-1]] = 1
	# 	print(ix_to_char[ix[-1]], end="")
	# 	ix = np.argmax(model.predict(X[:, :i+1, :])[0], 1)
	# 	y_char.append(ix_to_char[ix[-1]])
	# return ('').join(y_char)


	# start_index = random.randint(0, VOCAB_SIZE - 1)
	# for diversity in [0.2, 0.5, 1.0, 1.2]:
	# 	print('----- diversity:', diversity)
	# 	generated = ''
	# 	sentence = seed
	# 	generated += sentence
	# 	print('----- Generating with seed: "' + sentence + '"')
	# 	sys.stdout.write(generated)

	# 	for i in range(length):
	# 		x_pred = np.zeros((1, length, VOCAB_SIZE))
	# 		for t, char in enumerate(sentence):
	# 			x_pred[0, t, char_to_ix[char]] = 1.

	# 		pred = np.argmax(model.predict(x_pred, verbose=0)[0], 1)
	# 		next_char = ix_to_char[pred[-1]]

	# 		generated += next_char
	# 		sentence = sentence[1:] + next_char

	# 		sys.stdout.write(next_char)
	# 		sys.stdout.flush()
	# 	print()
