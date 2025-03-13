# > Ordering tuple by list
# Input:
# ```python
# ```
tupList = [('l', 5), ('k', 2), ('a', 1), ('e', 6)]
sortList = ['l', 'a', 'k', 'e']

newTupList = []

for i in sortList:
    for j in tupList:
        if (j[0] == i):
            newTupList.append(j)
print(newTupList)
# Output:
# ```python
# [('l', 5), ('a', 1), ('k', 2), ('e', 6)]
# ```

# Example 2:

# Python program to convert decimal to binary (in bytes) Input:

# tuple1 = (1234, 331, 437, 59, 63)
# Output: (binary of 1, binary of 2, binary of 3, binary of 4, binary of 5)