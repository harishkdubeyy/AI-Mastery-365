def reverse_string(text):
    s= ""
    for char in text:
        s = char + s
    return s
    
print(reverse_string("Python Programming"))    

def second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    if len(unique_numbers) < 2:
        return None
    else:
        return unique_numbers[-2]
    
print(second_largest([10, 20, 4, 45, 99]))

def second_smallest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    if len(unique_numbers) < 2:
        return None
    else:
        return unique_numbers[1]
    
print(second_smallest([10, 20, 4, 45, 99]))

def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]       

print(is_palindrome("Racecar"))

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Hello, World!"))

def count_consonants(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char.isalpha() and char not in vowels:
            count += 1
    return count    

print(count_consonants("Hello, World!"))    

def count_total_words(file_path):
    total_words = 0
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.split() # Splits by any whitespace
                total_words += len(words)
        return total_words
    except FileNotFoundError:
        return "File not found."
            
# Example Usage:
print(count_total_words("sample.txt"))    


def remove_duplicates(input_list):
    seen = set()
    result = []
    
    for item in input_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
            
    return result

data = [3, 1, 2, 1, 3, 4, 2]
print(remove_duplicates(data))


squares = [x**2 for x in range(1, 21)]

print(squares)

def sqno(x):
    return x**2

#numbers = [1, 2, 3, 4, 5]

numbers = 5

print(sqno(numbers))

def sqnolst(lst):
    for item in lst:
        print(item**2)

print(sqnolst([1, 2, 3, 4, 5]))       



