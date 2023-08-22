def reverse(string):
    if string == "":
        return string
    
    return string[-1] + reverse(string[:-1])
    

print(reverse('hello'))