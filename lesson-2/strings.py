def main():
    print('This is a single line text. Recommended')
    print('It\'s raining')  # escaping
    print("It's raining")
    print('''Multi-line text. The triple quoted line can be done with three single quotes or three double quotes. 
Either way, they allow the programmer to write strings over multiple lines. 
    If you print it out, you will notice that the output retains the line breaks. 
    If you need to use single quotes in your string, then wrap it in double quotes. 
    See the following example.
    ''')

    # To add integers
    print(1 + 1)

    # String concatenation
    first_name = "Eyob"
    last_name = "Sertse"
    year = 1991
    height = 1.70

    # Simple way
    print('My full name is ' + first_name + ' ' + last_name + '. ' + 'I was born on ' + str(year) + '. ' + 'My height is ' + str(height))

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

    first = "Eyob"
    last = "Sertse"

    username = first[0:3] + last[-3:]
    print(f'Your username is {username.lower()}')

    news = '''Berlin (CNN) One of postwar Germany's most publicized terrorism trials concluded Friday 
as a former German soldier was sentenced to five-and-a-half years in prison for plotting a far-right 
attack on senior politicians while posing as a Syrian refugee.
The 33-year-old former army officer identified as Franco A. in accordance with German privacy laws 
was charged with posing under a false identity as an asylum seeker in 2017 and planning an attack that 
he apparently hoped would be blamed on refugees and migrants.
    '''
    short_news = news[:70]
    print(f'Summary: {short_news}...')
    # print('Summary: ' + short_news + '...')


if __name__ == "__main__":
    main()
