# Array in C++ or Java {} or Python List []
ages = [34, 37, 40, 25, 80, 45]

# print the elements in a list
# print(ages) # prints everything in the list
# [34, 37, 40, 25, 80, 45]

# accessing each element of the list
for i in ages:
    print(f'Double the age is {i * 2}')

# adding elements to the list
ages.append(15)  # append means add to the end
ages.append(20)
ages.append(15)
# result 34	37	40	25	80	45	15	20  15

ages.remove(15)  # Remove first occurrence of value (remove 15 from the list)
# result 34	37	40	25	80	45	20  15

ages.append(20)
ages.append(20)
# result 34	37	40	25	80	45	20	15	20	20
# Removing all occurrences of an element from the list
# using while loop
while 20 in ages:
    ages.remove(20)
# result 34	37	40	25	80	45	15

# similar implementation using for loop
# for i in ages:
#     if i == 20:
#         ages.remove(20)

# deleting a specific element from the list using the index
ages.pop(5)  # removes 45 (index 5) from the list
# result 34	37	40	25	80	20	15

# accessing each element of the list
for i in ages:
    print(i, end='\t')  # add tab as a separator

