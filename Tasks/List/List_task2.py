# Problem Statements: List
# 1.  Rotate a list by n places:
# Input:  lst = [1, 2, 3, 4, 5] ,  n = 2
# Output:  [4, 5, 1, 2, 3]
lst = [1, 2, 3, 4, 5]
n = 2

n = n % len(lst)
rotated_list = lst[-n:] + lst[:-n]

print(rotated_list)
# 2.  Find all unique triplets in the list that sum up to zero:
# Input:  lst = [-1, 0, 1, 2, -1, -4]
# Output:  [[-1, 0, 1], [-1, -1, 2]]

# 3.  Find the longest consecutive subsequence in a list:
# Input:  lst = [100, 4, 200, 1, 3, 2]
# Output:  4  (The longest consecutive sequence is  [1, 2, 3, 4] )
lst2 = [100, 4, 200, 1, 3, 2]
lst2.sort()
print(lst2)

# 4.  Product of every other element:Product of every other element:
# Input:  lst = [1, 2, 3, 4, 5]
# Output:  15  (The product of elements at indices 0, 2, 4 is  1*3*5 )

# 5.  Find the most frequent element in a list:
# Input:  lst = [1, 3, 1, 3, 2, 1]
# Output:  1
lst3 = [1, 3, 1, 3, 2, 1]
count = 0
max_count = 0

for i in lst3:
    coun = lst3.count(i)
    if (coun > count):
        count = coun
        max_count = i
print(max_count)

# 6.  Check if a list is a palindrome:
# Input:  lst = [1, 2, 3, 2, 1]
# Output:  True
lst4 = [1, 2, 3, 2, 1]
if (lst4 == lst4[::-1]):
    print(True)
else:
    print(False)

# 7.  Find all pairs in a list whose sum is equal to a given number
# Input:  lst = [1, 2, 3, 4, 3, 6] ,  sum = 6
# Output:  [(2, 4), (3, 3)]

# 8.  Flatten a nested list:Flatten a nested list:
# Input:  lst = [[1, 2, 3], [4, 5], [6, [7, 8]]]
# Output:  [1, 2, 3, 4, 5, 6, 7, 8]
lst5 = [[1, 2, 3], [4, 5], [6, [7, 8]]]
flattened = [j for i in lst5 for j in i]

print(flattened)


# 9.  Find the maximum product of two integers in a list
# Input:  lst = [1, 20, 30, 4, 5]
# Output:  600  (Product of 20 and 30)
lst6 = [1, 20, 30, 4, 5]
lst6.sort()
print(lst6[-1] * lst6[-2] , "Product of 20 and 30")

# 10.  Rearrange the list such that positive numbers come before negative numbers:
# Input:  lst = [-1, 2, -3, 4, 5, -6]
# Output:  [2, 4, 5, -1, -3, -6]
lst7 = [-1, 2, -3, 4, 5, -6]
lst7.sort()
print(lst7.reverse())

# 11.  Find the smallest positive integer missing from a list:
# Input:  lst = [3, 4, -1, 1]
# Output:  2

# 12.  Find the subarray with the maximum sum:
# Input:  lst = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output:  6  (The subarray  [4, -1, 2, 1]  has the maximum sum)

# 13.  Find the intersection of two lists:Find the intersection of two lists:
# Input:  lst1 = [1, 2, 3, 4] ,  lst2 = [3, 4, 5, 6]
# Output:  [3, 4]

lst_left = [1, 2, 3, 4]   
lst_right = [3, 4, 5, 6]

inter = []

for i in lst_left:
    if i in lst_right and i not in inter:
        inter.append(i)
print(inter)

# 14.  Group elements of the list based on their parity:Group elements of the list based on their parity:
# Input:  lst = [1, 2, 3, 4, 5, 6]
# Output:  [[2, 4, 6], [1, 3, 5]]  (Even numbers first, followed by odd numbers)

# 15.  Partition the list into sublists of length n:Partition the list into sublists of length n:
# Input:  lst = [1, 2, 3, 4, 5, 6, 7, 8, 9] ,  n = 3
# Output:  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 16.  Find the majority element in a list:Find the majority element in a list:
# Input:  lst = [1, 2, 3, 1, 1]
# Output:  1

# 17.  Replace all occurrences of a given value with another value:Replace all occurrences of a given value with another value:
# Input:  lst = [1, 2, 3, 1, 2, 3] ,  old_value = 2 ,  new_value = 4
# Output:  [1, 4, 3, 1, 4, 3]

# 18.  Count the number of sublists in a list:Count the number of sublists in a list:
# Input:  lst = [1, [2, 3], 4, [5, 6], 7, [8, 9]]
# Output:  3

# 19.  Find the first missing positive integer in a list:Find the first missing positive integer in a list:
# Input:  lst = [3, 4, -1, 1]
# Output:  2

# 20.  Generate all permutations of a list:Generate all permutations of a list:
# Input:  lst = [1, 2, 3]
# Output:  [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]