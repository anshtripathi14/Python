
# Worling with Lists
l=[1,2,3,4,5]
print("\nThe given list is: ",l)

l.append(6)
print("\nAfter appending, the updated list is: ",l) 

del l[2]
print("\nAfter deletion, the updated list is: ",l)

l.insert(1,10)
print("\nAfter insertion, the updated list is: ",l)

l.sort(reverse=True)
print("\nThe updated list in descending order is: ",l)

# Working with Tuple

t=("apple", "banana", "cherry")
print("\nThe given tuple is: ",t)

print("\nThe second element of tuple is: ",t[1])