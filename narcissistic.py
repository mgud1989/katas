def narcissistic( value ):
    splitted = list(map(int, str (value)))
    raised = list(map(lambda x : x**len(splitted), splitted))
    result = 0
    for i in raised:
        result = result + i
    
    if (value == result):
        return True
    
    return False 

print (narcissistic(153))
print (narcissistic(1634))
print (narcissistic(16))
