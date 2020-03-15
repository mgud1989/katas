def reverse_words(text):

    words = text.split()

    return words

def recorre_letras(words):
    
    letters = []
    for w in words:
        letters.append("letter")

    return list(letters)

def reverse (palabra):

    #p_reverse = []
    s_reverse = ""
    i=(len(palabra) -1)

    while i > -1:

        #p_reverse.append(palabra[i])
        s_reverse += palabra[i]
        i-=1

    return s_reverse

print (list(recorre_letras(reverse_words("test test test"))))

print (reverse("probando"))
