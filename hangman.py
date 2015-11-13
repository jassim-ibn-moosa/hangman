import random

def get_wordlist():
    f = open("/usr/share/dict/words")
    clean_words = []
    for i in f:
        i = i.strip()
        if i.isalpha() and len(i) > 5:
            clean_words.append(i.lower())
    return clean_words

def select_word(wordlist):
    return random.sample(wordlist, 1)[0]

#def play_hangman(secret_world):
    # homework!!

wordlist = get_wordlist()
secret = select_word(wordlist)
print wordlist
#play_hangman(secret)
