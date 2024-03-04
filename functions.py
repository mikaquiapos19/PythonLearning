'''
Program Description:    Learning how to write functions in python using the
                        Bro Code tutorial on Youtube

Author: Mika Quiapos

Date: 03/03/24
'''

# A function is a block of reusable code. 

def happy_birthday(name, age):
    print(f"Happy birthday to {name} !") #f string
    print(f"You are {age} !")
    print("Happy birthday to you!")
    print("\n")


happy_birthday("Ally", 2)
happy_birthday("Me", 18)
happy_birthday("Jelly", 19)


def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("Mika", 85.32, "04/03")


# return
def add(x,y):
    z = x + y
    return z

def subtract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))

