from keras.models import Sequential
from keras.layers import Dense, Activation, LSTM, TimeDistributed
from keras import optimizers
import h5py
import numpy as np
import pickle



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




# Some constraints that weren't explained in the tutorial so I just made up some numbers
HIDDEN_DIM = 200
LAYER_NUM  = 2
BATCH_SIZE = 10
GENERATE_LENGTH = 100
SEQ_LENGTH = 180

length = int(len(data)/SEQ_LENGTH)

# Creates the mapping between the characters and orders the characters by least to most frequent
# only need to run once. later, just load it from pickle file

# ix_to_char = {ix:char for ix, char in enumerate(chars)}
# char_to_ix = {char:ix for ix, char in enumerate(chars)}

#print(ix_to_char)
# Used to save a mapping to keep it consistent between runs

pickle_file = "word_mappings.p"
# combined_dict = [ix_to_char, char_to_ix]
# with open(pickle_file, "wb") as picked :
#     pickle.dump(combined_dict, picked)


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



# Creates 3 dimensional array for training
# (number_of_sequences, length_of_sequence, number_of_features)
#
# number_of_sequences - length of data divided by length of sequence
#                       Variable: length
#
# length_of_sequence - Sequence length, "how long you want your model to learn at a time"
#                       Variable: SEQ_LENGTH
#
# number_of_features - All the different outputs our model could have, in this case, characters
#                      Variable: VOCAB_SIZE
#
X = np.zeros((length, SEQ_LENGTH, VOCAB_SIZE))
y = np.zeros((length, SEQ_LENGTH, VOCAB_SIZE))
print(int(len(data)))
print(length)
print(SEQ_LENGTH)
print(VOCAB_SIZE)
#
#
#
# Create a training array for *length* number of sequences

for i in range(0, length):
    X_sequence = data[i*SEQ_LENGTH:(i+1)*SEQ_LENGTH]
    X_sequence_ix = [char_to_ix[value] for value in X_sequence]
    input_sequence = np.zeros((SEQ_LENGTH, VOCAB_SIZE))
    for j in range(SEQ_LENGTH):
        input_sequence[j][X_sequence_ix[j]] = 1.
    X[i] = input_sequence

    y_sequence = data[i*SEQ_LENGTH+1:(i+1)*SEQ_LENGTH+1]
    y_sequence_ix = [char_to_ix[value] for value in y_sequence]
    target_sequence = np.zeros((SEQ_LENGTH, VOCAB_SIZE))
    for j in range(SEQ_LENGTH):
        target_sequence[j][y_sequence_ix[j]] = 1.
    y[i] = target_sequence
print(X)
print(y)
#
#
# Sequential is just a stack of layers
# each layer added with model.add(...)
#
# First layer:
# model.add(LSTM(HIDDEN_DIM, input_shape=(None, VOCAB_SIZE), return_sequences=True))
# LSTM(...) - Says we're using a Long Short Term Memory Layer
# HIDDEN_DIM - not sure yet, right now using random number
# input_shape - The dimensions of the input to the layer, in this situation, it's the number of unique characters
# return_sequences - also not sure what this does
#
#
# Second to third to last Layer:
# model.add(LSTM(HIDDEN_DIM, return_sequences=True))
# Same as first layer, but doesn't have to define the input shape
#
# Second to last layer:
# model.add(TimeDistributed(Dense(VOCAB_SIZE)))
# TimeDistributed - "This wrapper applies a layer of temporal slice of an input"




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
model.load_weights("checkpoint_200_epoch_+++120.hdf5")
model.save("final_model_word_recipes.h5")
# generate_text(model, GENERATE_LENGTH)
# while True:
#     print('\n\n')
#     model.fit(X, y, batch_size=BATCH_SIZE, verbose=1, epochs=1)
#     nb_epoch += 1
#     generate_text(model, GENERATE_LENGTH)
#     if nb_epoch % 10 == 0:
#         model.save_weights('checkpoint_{}_epoch_{}.hdf5'.format(HIDDEN_DIM, nb_epoch))
