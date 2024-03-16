#Searches for a word in a string
#input: String and word
#output: True or False

def word_check(sentence, word):
    return (' ' + word.lower() + ' ') in (' ' + sentence.lower() + ' ')

