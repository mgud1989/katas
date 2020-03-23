def reverse(words):
    new_words = " "

    i = len(words) -1

    while i > -1:
        
        new_words = new_words + words[i]
        
        i = i-1

    return new_words


print (reverse ("test1"))
print (reverse ("test dos"))
print (reverse ("test  three  3"))