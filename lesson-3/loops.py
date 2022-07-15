# Example 1
# Write a program the shows the sum of all numbers from 1 to 10.
# Foolish way of solving the issue
# sum = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
# print(f'Sum is {sum}')

# Using for loop
sum = 0
for i in range(1,11):   # the last number in range is not considered
    sum = sum + i
print(f'Sum is {sum}')

# Example 2
# Write a program the shows the sum of all EVEN numbers from 1 to 10.
sum_of_evens = 0
for i in range(2, 11, 2):  # last argument (2) means increment by 2
    sum_of_evens += i  # similar to sum_of_evens = sum_of_evens + i
print(f'Sum of evens is {sum_of_evens}')

# Example 3
# Write a program the shows the sum of all numbers from 50 to 10.
sum = 0
for i in range(50,9,-1):   # the last argument decrements by 1
    sum = sum + i

print(f'Sum is {sum}')
