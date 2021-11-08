def header():
    print(f"Personal Identification")

def obtainInfo():
    yourName = input("Name: ")
    yourAge = int(input("Age: "))
    yourAddress = input("Address: ")
    return print (f"Hi, my name is {yourName}. I am {yourAge} years old and I live in {yourAddress}.")
    
header()
obtainInfo()


# another version
def header():
    print(f"Personal Identification")

def obtainInfo():
    yourName = input("Name: ")
    yourAge = int(input("Age: "))
    yourAddress = input("Address: ")
    return yourName, yourAge, yourAddress

def intro(_name, _age, _address):
    print (f"Hi, my name is {_name}. I am {_age} years old and I live in {_address}.")

header()
name, age, address = obtainInfo()
intro(name, age, address)