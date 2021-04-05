import sys

def text_analyzer(text=None):
    if len(sys.argv) > 2:
        print("ERROR")
        exit()
    if text:
        up = 0
        low = 0
        punc = 0
        sp = 0
        t_len = len(text)
        if t_len > 0:
            for i in range(t_len):
                if text[i].islower():
                    low += 1
                elif text[i].isupper():
                    up += 1
                elif text[i] in ".:;?!,-_'\"":
                    punc += 1
                elif text[i] == " ":
                    sp += 1
            print("The text contains " + str(i+1) + " characters:")
        if up > 0:
            print("- " + str(up) + " upper letters")
        if low > 0:
            print("- " + str(low) + " lower letters")
        if punc > 0:
            print("- " + str(punc) + " punctuation marks")
        if sp > 0:
            print("- " + str(sp) + " spaces")
    elif text == None:
        print("What is the text to analyse?")
        text = input()
        text_analyzer(text)
    else:
        print("ERROR")
        exit()
