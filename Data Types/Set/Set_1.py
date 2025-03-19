mySet = set()

print(f"{type(mySet)} -> {mySet}")
mySet = {1,}

print(f"{type(mySet)} -> {mySet}")
mySet = set([1, 2, 23, 12, 3334, 354, 34, 23, 12, 5, 32])

mySet

mySet = {1, 2, 3, "Python", 'dsf', 'a', 2.333, 12.37}
mySet

myList = {11, 23, 11, 34, 22, 34, 22, 45, 456, 546, 56, 45, 56}
myList

myList = ['veggies', 'snacks', 'biscoots', 'fruits', 'ice-creams', 'chocolates']
print(set(myList))

ms = set(['veggies', 'snacks', 'biscoots', 'fruits', 'ice-creams', 'chocolates'])
ms.add('fast-food')
ms.discard('veggies')
print(ms)

mySet = {23, 45, 79, 34, 13}
dummy_set = {23, 45, 799, 34, 13}
disjoint_set = {2, 3}
new_set = {23, 45}

# mySet - dummy_set

mySet.difference_update(dummy_set)

{1, 2, 3}.isdisjoint({23, 22, 4})

mySet.intersection(dummy_set)

mySet.intersection_update(dummy_set)

new_set.issubset(dummy_set)

dummy_set.issuperset(new_set)

mySet.pop()

mySet.remove(45)
mySet.symmetric_difference(dummy_set)

mySet.symmetric_difference_update(dummy_set)
mySet.update((3, 203))

{1, 2}.union({3., 4})
{1, 2, 3.0, 4}
# del mySet, dummy_set, disjoint_set, new_set
