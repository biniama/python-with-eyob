# Print the following stars
# *****
# *****
# *****
# *****
# *****

# Using nested for loop - for loop inside another for loop
# because we have rows and columns
for row in range(0, 5):
    for column in range(0, 5):
        print('*', end='')  # stay in the same line
    print('')
# HOW DOES THE COMPUTER DO THIS?
#MEMORY
# row =4
# column=4
#OUTPUT
# *****
# *****
# *****
# *****
# *****