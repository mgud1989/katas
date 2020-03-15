def reverse_words(text):

    words = text.split()
    

    #letter.append(text[])

    return words

def recorre_letras(words):
    
<<<<<<< HEAD
    letters = []
    for w in words:
        letters.append("letter")

    return list(letters)

def reverse (palabra):

    p_reverse = []
    s_reverse = ""
    i=(len(palabra) -1)

    while i > -1:

        p_reverse.append(palabra[i])
        s_reverse += palabra[i]
        i-=1

    return s_reverse

print (list(recorre_letras(reverse_words("test test test"))))

print (reverse("probando"))
=======
    new_words = []
    
    for w in words:
        for l in w:
            yield new_words.append("letter")
    
        

    return list(new_words)


print (list(recorre_letras(reverse_words("test test test"))))
>>>>>>> 92a891955f5107eedaa3d0e27f47dce167f00864
