nested_numbers = [[10, 15, 21], [33, 40, 45], [50, 60, 75]]
matrix = [[4, 3, 8], [5, 6, 7], [9, 11, 13]]
words_list = [["madam", "level", "python"], ["racecar", "wow", "data"]]
numbers_list = [[10, 20, 30], [1, 2, 3], [5, 15, 25]]
sentence_list = [["Python", "is", "fun"], ["AI", "rocks", "comprehension"]]
grid = [[(x, y) for y in range(3)] for x in range(3)]

# Challenges:

#  Extract all odd numbers from a nested list and square them.

square = [j**2 for i in nested_numbers for j in i if j % 2 != 0]
print(square)

#  Flatten a matrix and keep only the prime numbers.

#  Find all words that are palindromes inside a nested word list.
pali = [j for i in words_list for j in i if j[::-1] == j]
print(pali)

#  Filter out words with less than 4 letters and return a flattened list.
len = [j for i in words_list for j in i if j.__len__() <= 4]
print(len)

#  Generate a new list containing the sum of corresponding elements in two nested lists.  Extract unique vowels from all words in a nested list.

#  Find all numbers in a nested list that are divisible by both 3 and 5.
divi = [j for i in nested_numbers for j in i if j % 3 == 0 and j % 5 == 0]
print(divi)

# Convert a nested list of words into their lengths but only for words longer than 3 letters.  
word = [j for i in sentence_list for j in i if j.__len__() > 3]
print(word)

# Create a list of coordinate pairs from a 3x3 grid representation.
grid = [[(x, y) for y in range(3)] for x in range(3)]
print(grid)

# 🔟 Reverse each word in a nested list, but only if it starts with a vowel.
vowels = 'A','E','I','O','U','a','e','i','o','u'
contains_vowel = [j for i in sentence_list for j in i if j.startswith(vowels)]
print(contains_vowel)