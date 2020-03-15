def reverse_words(text):

    words = text.split()
    

    #letter.append(text[])

    return words

def recorre_letras(words):
    
    letters = []
    for letter in words:
        yield letter
        letters.append(letter)

    return list(letters)
print (list(recorre_letras(reverse_words("test"))))