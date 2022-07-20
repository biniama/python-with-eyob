from typing import Dict

def main():
    # dictionary has a key and a value and use colon (:) in between
    # Key should always be a String datatype.
    # Value can be any datatype e.g. int, string, float, dictionary, list, ...
    # this is a very powerful and useful data type because
    # it is similar to JSON data type which is used to share data between systems
    dictionary = {"Book": "is something to read"}
    #print(dictionary)

    # list []
    # tuple ()
    # dictionary {}

    # You can embed another dictionary inside a dictionary e.g. spouse
    biniam_data = {
        "name": "Biniam",
        "age": 34,
        "profession": "Senior Software Engineer",
        "spouse": {
            "name": "Kidan",
            "age": 30
        }
    }
    print(biniam_data) # dumps the data to the screen/output

    eyob_data = {
        "first_name": "Eyob",
        "last_name": "Sertse",
        "age": 37,
        "height": 1.73,
        "spouse": {
            "name": "Betty"
        },
        "children": [
            {
                "name": "Nolawi",
                "age": 6
            },
            {
                "name": "Akila",
                "age": 3
            }
        ]
    }

    print(eyob_data)

    # To access value in dictonary
    print(eyob_data.get('first_name'))
    print(eyob_data['first_name'])

    # Using for loop to iterate/repeat over a dictionary
    # Exercise: print Biniam's data in capital letter and as a statement
    for key in biniam_data:
        print(key.upper() + ' ' + str(biniam_data[key]))
        #print(key.upper() + ' IS ' + biniam_data.get(key).upper())
        # alternative way of writing
        #print(f'{key.upper()} IS {biniam_data.get(key).upper()}')


if __name__ == '__main__':
    main()
