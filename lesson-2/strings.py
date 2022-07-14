def main():
    print('This is a single line text. Recommended')
    print('It\'s raining')
    print("It's raining")
    print("""Multi-line text. The triple quoted line can be done with three single quotes or three double quotes. 
Either way, they allow the programmer to write strings over multiple lines. 
    If you print it out, you will notice that the output retains the line breaks. 
    If you need to use single quotes in your string, then wrap it in double quotes. 
    See the following example.
    """)

    # To add integers
    print(1 + 1)

    # String concatenation
    first_name = "Eyob"
    last_name = "Sertse"
    year = 1991
    height = 1.70

    # Simple way
    print('My full name is ' + first_name + ' ' + last_name)

    # More professional and maintainable way -> f means format
    print(f'My full name is {first_name} {last_name}. I was born on {year}. My height is {height}')

    # Old way
    print('My full name is %s %s. I was born on %d. My height is %f' % (first_name, last_name, year, height))

    # Replacing strings
    # Biniam -> B1n1am -> B1n14m -> b1n14m
    print('Biniam'.replace('i', '1').replace('a', '4').lower())

    # String slicing and accessing individual characters
    my_string = "Like Python"
    # Every character has an index starting from 0
    # Like Python
    # 012345678910
    # ........-2-1
    print(my_string)     # original
    print(my_string[0:4])  # Like ( last number is not included)
    print(my_string[:4])  # Like
    print(my_string[5:11])  # Python
    print(my_string[5:])  # Python
    print(my_string[-6:])  # Python


if __name__ == "__main__":
    main()
