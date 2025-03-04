# Paragraph:
text =  "Indian cuisine offers a rich and diverse array of vegetarian dishes, reflecting the country's cultural and regional variations. Staples like lentils, rice, and a variety of fresh vegetables form the foundation of many meals. Dishes such as dal (lentil stew), sabzi (vegetable curry), and roti (unleavened bread) are commonplace. Spices play a crucial role, with ingredients like turmeric, cumin, coriander, and garam masala imparting unique flavors. South Indian cuisine features dishes like dosa (fermented crepe), idli (steamed rice cakes), and sambar (spicy lentil soup). North Indian cuisine is famous for dishes like paneer tikka (grilled cheese), chole (chickpea curry), and aloo gobi (potato and cauliflower curry). Street foods such as samosas, bhel puri, and pav bhaji are popular across the country. Many Indian sweets, including gulab jamun, jalebi, and barfi, are also vegetarian. Each region offers its own specialties, ensuring a vast and exciting culinary landscape for vegetarians to explore."

print(len(text))

# > 56-Bhog Tasks:
# Extract the first sentence without using the split method.
# print(text[0:text.find('.')+1])
# Extract the phrase "rich and diverse" from the first sentence.
# print(text[text.find('rich'):text.find('se')+2])
# Extract the last sentence without using the split method.
# print(text[text.find('Each'):-1])
# Extract the phrase "lentil stew" without using the find method.
# print(text[text.find('('):text.find(')')+1])
# Extract the word "lentils" in reverse order.
# text2 = text[text.find('lentils'):text.find('lentils')+7]
# print(text2[::-1])
# Extract every second word in the paragraph.
# print(text.split()[::2])
# Extract the first word of each sentence in the paragraph.
splited_words = text.split(' ')
# print(splited_words)
# for i in splited_words:
#     print(i, end="\n")
# Extract the last word of each sentence in the paragraph.
# Extract the paragraph in reverse order.
# print(text[::-1])
# Extract every third character from the paragraph.
# print(text[::3])
# Extract the first and last word of the paragraph.
# Extract all words containing the letter 'e'.
for i in splited_words:
    e_con = i.find('e')
    if(i.find('e')):
        print(e_con)
# Extract the paragraph without the first and last word.
# Extract all occurrences of the word "Indian" and reverse them.
# Extract the phrase "dal (lentil stew), sabzi (vegetable curry), and roti" without using the split or find method.
# Extract the names of dishes that contain the letter 'a'.
# Extract the first and last sentence, and join them into a new string.
# Extract the words "fresh vegetables form" and reverse the order of these words.
# Extract every word that starts with a consonant.
# Extract all the capital letters in the paragraph.

# ----------------------------------------------------------------------------------------

# s = "Artificial_Intelligence"

# print(s[:10])
# print(s[4:10])
# print(s[:4])
# print(s[:5])

# word = "0_1_2_3_4_5_6_7_8_9"

# print(word[::2])
# print(word[4::4])
# print(word[2::2])

# my_string = "The quick brown fox jumps over the lazy dog"

# > Extract every second character in reverse from the original string

# sec_chars = (my_string[::2])
# print([sec_chars[::-1]])