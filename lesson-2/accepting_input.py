def accepting_input():
    # when you accept an input, it always gives you a string.
    age_str = input('Enter your age ')

    # cast (converting the type of the variable)
    age = int(age_str)

    result = age + 5
    print('Your result is ', result)

    light_str = input('Is the light on?')

    if light_str.lower() == 'true':
        print('Light is on')
    elif light_str.lower() == 'false':
        print('Light is off')
    else:
        print('We do not know if light is on or off')
    # It is not a must to include else case.


if __name__ == "__main__":
    accepting_input()