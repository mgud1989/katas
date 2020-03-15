def reverse_words(text):

    words = text.split()
    new_words = []
    
    for w in words:
        
        new_words.append(reverse(w))

    return new_words


def reverse (palabra):

    s_reverse = ""
    i=(len(palabra) -1)

    while i > -1:

        s_reverse += palabra[i]
        i-=1

    return s_reverse

print (reverse_words("test python hola"))

print (reverse("probando palabras"))
