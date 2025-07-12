def getName():
    name = input("What is your name?: ")
    
    while not  name.isalpha():
        name = input("What is your name?: ")

    return name
    

def getSurname():
    surname = input("What is your surname?: ")
    
    while not surname.isalpha():
        surname = input("What is your surname?: ")

    return surname
    

def getPhoneNumber():
    number=input("What is your number?: ")

    while not number.isdigit() or  len(number) !=10:
        number=input("What is your number?: ")
    
    return number
    
        
        



if __name__ == '__main__':
    getName()
    getSurname()
    getPhoneNumber()