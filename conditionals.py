# based on the user's age, say something.

def conditionals():
    age = 19

    if (age > 0 and age <= 10):  # if (0 < age <=10)
        print("You are a child!")
    elif (age >=11 and age <=18):  # elif (11 < age <=18)
        print("You are a teenager!")
    elif (age >18 and age <=50):  # elif (18 < age <=50)
        print("You are adult!")
    else:
        print("You are old!")


if __name__ == "__main__":
    conditionals()
