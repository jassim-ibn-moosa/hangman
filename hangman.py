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

def play_hangman(secret_word):
    display_word = " --> "
    for i in secret_word_letters:
        display_word += "*"
    print secret_word
    print "break the word"
    wrong_try  = 0
    while wrong_try < 10:
        for l in raw_input('>'):#'abcdefghijklmnopqrstuvwxyz':
            if l not in secret_word:
                wrong_try += 1
                print wrong_try
            else:
                display_word = "-"
        if wrong_try > 10:
                    print "Game over!!!"
                    return
    print display_word
    print "in while loop"
    print secret_word_letters 

wordlist = get_wordlist()
secret = select_word(wordlist)
play_hangman(secret)
