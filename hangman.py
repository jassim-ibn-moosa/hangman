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
    wrong_data = ""
    correct_data = ""
    pos_max = -1
    count = 0
    for i in secret_word_letters:
        display_word += "*"
        pos_max += 1
        count += 1
#    print secret_word
    print "break the word"
    print display_word
    wrong_try  = 0
#    print pos_max
 #   print count
    while wrong_try < 10 and count > -1:
        for l in raw_input('>'):
            if l not in secret_word and l not in wrong_data:
                wrong_data += l
                wrong_try += 1
                #print wrong_try
                if wrong_try == 10:
                    print "Game over!!!"
                    print "the correct word is: %r "% secret_word
                    return
            elif l in secret_word and l not in correct_data:
                correct_data += l
                pos = secret_word.index(l)
                display_word = list(display_word)
                display_word[pos] = l 
                count -= 1
          #      print pos_max
           #     print count
                pos = pos + 1
                while pos <= pos_max:
                    if l == secret_word[pos]:
                        display_word[pos] = l
                        count -= 1
                    pos = pos + 1
                display_word = "".join(display_word)
                print display_word
                if count == 0:
                    print "You win !!!"
                    return
            else:
                print "'%s' has been enterd earlier plz try other charecter" %l
            

wordlist = get_wordlist()
secret = select_word(wordlist)
play_hangman(secret)
