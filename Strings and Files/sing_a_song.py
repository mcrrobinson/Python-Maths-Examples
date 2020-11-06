# Write a singASong function which outputs a “song” based on a single word. The user
# should be asked for the song’s word, how many lines long the song should be, and
# how many times the word should be repeated on each line. For example, if the user
# enters the word “dum” and the numbers 2 and 4, the function should then output the
# following song (note that the spaces are important):
# dum dum dum dum
# dum dum dum dum

def singASong(word, y, x):
    stringStream = ""
    for i in range(y):
        string += (word+" ")*x+"\n"
    return stringStream

print(singASong("This is dumb",2,4))
