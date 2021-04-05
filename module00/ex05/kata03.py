phrase = "The right format"

if len(phrase) > 42:
    print(phrase)
else:
    print("-" * (42 - len(phrase)) + phrase, end='')
