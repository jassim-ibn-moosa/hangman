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
    secret_word_letters = list (secret_word)
    display_word = ""
    pos_max = -1
    for i in secret_word_letters:
        display_word += "*"
        pos_max += 1
    print secret_word
    print "break the word"
    print display_word
    wrong_try  = 0
    while wrong_try < 10:
        for l in raw_input('>'):
            if l not in secret_word:
                wrong_try += 1
                print wrong_try
                if wrong_try == 10:
                    print "Game over!!!"
                    return
            else:
                pos = secret_word.index(l)
                display_word = list(display_word)
                display_word[pos] = l #display_word.replace('*',l)
                pos = pos + 1
                while pos <= pos_max:
                    if l == secret_word[pos]:
                        display_word[pos] = l
                    pos = pos + 1
                display_word = "".join(display_word)
                print display_word
    print secret_word_letters 

wordlist = get_wordlist()
secret = select_word(wordlist)
play_hangman(secret)
