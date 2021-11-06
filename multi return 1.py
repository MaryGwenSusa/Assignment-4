def header():
    print(f"Personal Identification")

def obtainInfo():
    yourName = input("Name: ")
    yourAge = int(input("Age: "))
    yourAddress = input("Address: ")
    return print (f"Hi, my name is {yourName}. I am {yourAge} years old and I live in {yourAddress}.")
    
header()
obtainInfo()