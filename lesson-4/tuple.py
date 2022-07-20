# tuple is immutable data type - you cannot add/append or remove an element to/from a tuple
def main():
    tuple = (32, 29, 27)
    # index   0   1   2
    # index  -3  -2  -1
    print(tuple)

    for t in tuple:
        print(t, end='\t')

    # accessing tuple elements using indexes
    print(tuple[0:2]) # prints (32, 29) # last index in not included

    #tuple.append(32) # error: AttributeError: 'tuple' object has no attribute 'append'

    #tuple.remove(32) # error: AttributeError: 'tuple' object has no attribute 'remove'

    # you can convert a tuple to a list
    # like you covert an integer to a string or vice versa
    converted_list = list(tuple)
    print(converted_list)   # prints [32, 29, 27]


if __name__ == '__main__':
    main()