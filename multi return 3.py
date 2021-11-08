def openStatement():
    print(f"Budget for Comfort Food: Apple")

def moneyMonitor():
    yourWallet = float(input('Your Current Money:\n> '))
    priceOfApple = float(input('How much is the apple?\n> '))
    return yourWallet, priceOfApple

def computation(money, price):
    maximumNumberOfApples = int(money/price)
    remainingMoney = float(money%price)
    return print(f"You can buy {maximumNumberOfApples} and your change is {remainingMoney:.2f}.")

openStatement()
money, fluctuationPrice = moneyMonitor()
computation(money, fluctuationPrice)


# another version
def openStatement():
    print(f"Budget for Comfort Food: Apple")

def moneyMonitor():
    yourWallet = float(input('Your Current Money:\n> '))
    priceOfApple = float(input('How much is the apple?\n> '))
    maximumNumberOfApples = int(yourWallet/priceOfApple)
    remainingMoney = float(yourWallet%priceOfApple)
    return yourWallet, priceOfApple, print(f"You can buy {maximumNumberOfApples} and your change is {remainingMoney:.2f}.")

openStatement()
moneyMonitor()
