from data import letters

def letters2symbols(word):
    symbols = []
    for letter in word:
        if letter in letters:
            symbols.append(letters[letter])

    return symbols
