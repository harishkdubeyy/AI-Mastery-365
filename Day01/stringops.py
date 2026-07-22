def reverse_string(text):
    s= ""
    for char in text:
        s = char + s
    return s
    
print(reverse_string("Python Programming"))    