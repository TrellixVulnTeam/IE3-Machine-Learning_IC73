
#file_name = str(input("Input File Name: "))
f = open("all_files.txt", 'r')

all_words = map(lambda l: l.split(" "), f.readlines())
vocab = {}


for line in all_words :
    temp = line[:-1]
    for word in temp :
        length = len(word)
        while length > 0 and (word[length-1] == "." or word[length-1] == ")" or word[length-1] == '\n' or word[length-1] == ";" or word[length-1] == ":" or word[length-1] == ","):
            word = word[0:length-1]
            length = len(word)
        while length > 0 and word[0] == "("  :
            word = word[1:length]
            length = len(word)
        if not(hash(word) in vocab) :
            vocab[hash(word)] = word

f.close()

with open("vocab_list.txt", 'a') as out :
    for key in vocab :
        word = vocab[key]
        length = len(word)
        if length > 0:
            out.write(word + ",")
