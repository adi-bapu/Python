veggies = [
    "Bitter Gourd (Karela)",
    "Bottle Gourd (Lauki)",
    "Ridge Gourd (Turai)",
    "Snake Gourd (Galka)",
    "Pointed Gourd (Parwal)",
    "Drumstick (Moringa)",
    "Taro Root (Arbi)",
    "Elephant Foot Yam (Suran)",
    "Ash Gourd (Petha)",
    "Ivy Gourd (Tindora)",
    "Fenugreek Leaves (Methi)",
    "Amaranth Leaves (Patra)",
    "Colocasia Leaves (Arbi ke Patte)",
    "Beet Greens (Chukandar ke Patte)",
    "Mustard Greens (Sarson)",
    "Radish Greens (Mooli ke Patte)",
    "Spinach (Palak)",
    "Fenugreek Seeds Sprouts (Methi Dana)",
    "Cluster Beans (Gawar Phali)",
    "French Beans",
    "Yardlong Beans (Bora)",
    "Broad Beans (Sem)",
    "Green Peas (Matar)",
    "Corn (Makai)",
    "Bamboo Shoots (Karil)",
    "Jackfruit (Kathal)",
    "Raw Banana (Kachcha Kela)",
    "Green Papaya (Kachcha Papita)",
    "Indian Gooseberry (Amla)",
    "Curry Leaves (Kadi Patta)",
    "Raw Mango (Keri)",
    "Sponge Gourd (Nenua)",
    "Brinjal (Baingan)",
    "Lady Finger (Bhindi)",
    "Cabbage (Patta Gobi)",
    "Cauliflower (Phool Gobi)",
    "Radish (Mooli)",
    "Turnip (Shalgam)",
    "Carrot (Gajar)",
    "Tomato (Tamatar)"
]

# 1. Sort by Hindi Names
# Sort the veggies list based on the Hindi names while keeping the original structure intact.

# for i in veggies:
#     print(i[i.find('(')+1:i.find(')')])

# 2. Extract Only Hindi Names
# Create a new list that contains only the Hindi names of the vegetables.

# hindNameList = []
# for i in veggies:
#     hindi_word = i[i.find('(')+1:i.find(')')]
#     hindNameList.append(hindi_word)
# print(hindNameList)

# # 3. Extract Only English Names
# Create a new list that contains only the English names of the vegetables.

# engName_veg = []
# for i in veggies:
#    eng_word = i[:i.find('(')-1]
#    engName_veg.append(eng_word)
# print(engName_veg)

# 4. Find the Longest and Shortest Vegetable Names
# Identify and print the longest and shortest vegetable names (English and Hindi separately).

# longest engword
# engName_veg = []
# long_eng = 0
# for i in veggies:
#     eng_word = i[:i.find('(')-1]
#     if (eng_word.__len__() > long_eng):
#         long_eng = eng_word.__len__()
#     engName_veg.append(eng_word)

# print(long_eng)
# print(engName_veg)

# longest hindiword
# hindi_veg = []
# long_hindi = 0
# for i in veggies:
#     hindi_word = i[i.find('(')+1:i.find(')')]
#     if (hindi_word.__len__() > long_hindi):
#         long_hindi = hindi_word.__len__()
#     hindi_veg.append(hindi_word)

# print(long_hindi)
# print(hindi_veg)

# short_eng = 0
# for i in engName_veg:
#     short_eng = engName_veg.__len__()
#     if eng_word.__len__() < short_eng:
#         short_eng = eng_word.__len__()
# print(short_eng)
# print(engName_veg)

# short_hindi = 0
#    if (hindi_word.__len__() < short_hindi):
#     short_hindi = hindi_word.__len__()

# print(long_hindi)
# print(hindi_veg)

# 5. Reverse Each Vegetable Name
# Print a new list where each vegetable name (both English and Hindi) is reversed.

# engName_vegrev = []
# for i in veggies:
#    eng_wordrev = i[:i.find('(')-1]
#    engName_vegrev.append(eng_wordrev[::-1])
# print(engName_vegrev)

# print("\n")

# hindName_vegrev = []
# for i in veggies:
#     hindi_wordrev = i[i.find('(')+1:i.find(')')]
#     hindName_vegrev.append(hindi_wordrev[::-1])
# print(hindName_vegrev)

# Medium
# 6. Find Vegetables Containing a Given Letter
# Write a function that takes a letter as input and returns all vegetable names (English and Hindi) containing that letter.

# print(veggies)
# letter = input("Enter the letter: ")

# for i in veggies:
#     if i.__contains__(letter):
#         print(i)
#         print(i.__len__())

# 7. Count the Occurrences of Each Letter
# Create a dictionary where each letter (a-z) maps to the number of times it appears across all vegetable names.
# 8. Create an Abbreviation List
# Generate a list of abbreviations where each abbreviation consists of the first letter of each word in the vegetable name.
# 9. Extract Vegetables with More than 10 Characters
# Find and print all vegetable names (either English or Hindi) that contain more than 10 characters.

# hindNameList = []
# for i in veggies:
#     hindi_word = i[i.find('(')+1:i.find(')')]
#     hindNameList.append(len(hindi_word) > 10)
# print(hindNameList)

# engName_veg = []
# for i in veggies:
#    eng_word = i[:i.find('(')-1]
#    engName_veg.append(len(eng_word) > 10)
# print(engName_veg)


# 10. Split and Reformat Names
# Transform the veggies list so that each item is stored as a dictionary with keys English and Hindi.


# Hard
# 11. Find the Most Common Letter
# Determine which letter appears most frequently in all vegetable names.


# 12. Sort the List Based on the Length of Hindi Names
# Sort the list based on the length of Hindi names while maintaining the original English names.
# 13. Implement a Custom Search Function
# Write a function that takes a search term and returns all matching vegetables where the term is a substring of either the English or Hindi name.
# 14. Find Anagrams in the List
# Check if any vegetable names (English or Hindi) are anagrams of each other and print the pairs.
# 15. Generate All Possible Slices
# For each vegetable name, generate and print all possible contiguous substrings (slices).