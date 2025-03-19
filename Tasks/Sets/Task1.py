# Problem 1: Find the Unique Elements in Multiple Lists
# Problem Statement:
# You are given a list of lists, where each list contains numbers. Find all the unique elements across all the lists
# using sets.
# Sample Input:
list_of_lists = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
unique_elements = set()

for i in list_of_lists:
    unique_elements.update(i)

print(unique_elements)
# Sample Output:
# {1, 2, 3, 4, 5, 6, 7}

# Problem 2: Find the Common Elements Between Two Lists
# Problem Statement:
# Given two lists, use a set to find the common elements between them and print the result.
# Sample Input:
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common_ele = set(list1).intersection(list2)
print(common_ele)
# Sample Output:
# {3, 4, 5}

# Problem 3: Remove Duplicates from a List
# Problem Statement:
# Given a list with duplicates, remove the duplicates using sets and print the resulting list.
# Sample Input:
list1 = [1, 2, 2, 3, 3, 4, 5, 5]
removed_dup = set(list1)

print(removed_dup)
# Sample Output:
# [1, 2, 3, 4, 5]

# Problem 4: Find the Union of Two Lists
# Problem Statement:
# Given two lists, find the union of both lists using sets and print the result.
# Sample Input:
list1 = [1, 2, 3]
list2 = [3, 4, 5]

union_list = set(list1).union(list2)

print(union_list)
# Sample Output:
# {1, 2, 3, 4, 5}

# Problem 5: Find the Difference Between Two Lists
# Problem Statement:
# Given two lists, find the elements that are present in the first list but not in the second list using sets and print
# the result.
# Sample Input:
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]

find_num = set(list1).difference(list2)

print(find_num)
# Sample Output:
# {1, 2, 3}

# Problem 6: Check if Two Lists are Disjoint
# Problem Statement:
# Given two lists, check if they have no common elements using sets. Print True if they are disjoint, otherwise
# False.
# Sample Input:
list1 = [1, 2, 3]
list2 = [4, 5, 6]

checkifCommon = set(list1).isdisjoint(list2)

print(checkifCommon)
# Sample Output:
# True

# Problem 7: Count the Number of Unique Elements in a List
# Problem Statement:
# Given a list, find the number of unique elements in the list using sets.
# Sample Input:
list1 = [1, 2, 3, 3, 4, 5, 5, 6]
new_list = set(list1)

print(len(new_list))
# Sample Output:
# 6

# Problem 8: Find the Symmetric Difference Between Two Lists
# Problem Statement:
# Given two lists, find the symmetric difference (elements that are in either of the lists but not in both) using
# sets and print the result.
# Sample Input:
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

symmetric_diff = set(list1).symmetric_difference(list2)

print(symmetric_diff)
# Sample Output:
# {1, 2, 5, 6}

# Problem 9: Convert List to Set and Back to List
# Problem Statement:
# Given a list, convert it to a set and then convert it back to a list. Print the result in both cases.
# Sample Input:
list1 = [1, 2, 2, 3, 4]
mySet = set(list1)
new_list = list(mySet)

print('Set :' , mySet)
print('List :' , new_list)
# Sample Output:
# Set: {1, 2, 3, 4}
# List: [1, 2, 3, 4]

# Problem 10: Find the Subset Relationship Between Two Lists
# Problem Statement:
# Given two lists, check if the first list is a subset of the second list using sets and print the result.
# Sample Input:
list1 = [1, 2, 3]
list2 = [1, 2, 3, 4, 5]

checkifSubset = set(list1).issubset(list2)

print(checkifSubset)
# Sample Output:
# True