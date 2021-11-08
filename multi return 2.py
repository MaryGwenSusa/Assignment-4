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


# another version
def welcome():
    print(f"Welcome to Apple and Orange Cart!")

def computeFruitQ():
    appleQ = int(input("How many apples do you want to buy?\n> "))
    orangeQ = int(input("How many oranges do you want to buy?\n> "))
    return appleQ, orangeQ

def fruitPrices(applePrice, orangePrice):
    applePrice = applePrice*20
    orangePrice = orangePrice*25
    return applePrice, orangePrice

def total(computeAppleQ, computeOrangeQ):
    totalAmount = computeAppleQ+computeOrangeQ
    return print(f"The total amount is {totalAmount}.")

welcome()
numberOfApple, numberOfOrange = computeFruitQ()
fruitPrices(numberOfApple, numberOfOrange)
totalApple, totalOrange = fruitPrices(numberOfApple, numberOfOrange)
total(totalApple, totalOrange)


# another version
def welcome():
    print(f"Welcome to Apple and Orange Cart!")

def computeFruitQ():
    appleQ = int(input("How many apples do you want to buy?\n> "))
    orangeQ = int(input("How many oranges do you want to buy?\n> "))
    return appleQ, orangeQ

def fruitPrices(applePrice, orangePrice):
    applePrice = applePrice*20
    orangePrice = orangePrice*25
    totalAmount = applePrice+orangePrice
    return applePrice, orangePrice, print (f'The total amount is {totalAmount}.')

welcome()
numberOfApple, numberOfOrange = computeFruitQ()
fruitPrices(numberOfApple, numberOfOrange)