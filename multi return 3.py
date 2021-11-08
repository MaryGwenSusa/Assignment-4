def openStatement():
    print(f"Budget for Comfort Food: Apple")

def moneyMonitor():
    yourWallet = float(input('Your Current Money:\n> '))
    priceOfApple = float(input('How much is the apple?\n> '))
    return yourWallet, priceOfApple

def computation(money, price):
    maximumNumberOfApples = int(money/price)
    