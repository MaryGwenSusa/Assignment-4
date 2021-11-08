
def welcome():
    print(f"Welcome to Apple and Orange Cart!")

def computeFruitQ():
    appleQ = int(input("How many apples do you want to buy?\n> "))
    appleQ*=20
    orangeQ = int(input("How many oranges do you want to buy?\n> "))
    orangeQ*=25
    return appleQ, orangeQ

def total(computeAppleQ, computeOrangeQ):
    totalAmount = computeAppleQ+computeOrangeQ
    return print(f"The total amount is {totalAmount}.")

welcome()
numberOfApple, numberOfOrange = computeFruitQ()
total(numberOfApple, numberOfOrange)