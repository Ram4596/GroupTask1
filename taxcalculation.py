

print(" Lets do some tax calculations")

salary = int(input("enter your Annual salary "))

if( salary < 500000):
    tax = 0 
    print("The tax is", tax)
elif( salary < 7500001 ):
    tax = (salary * 15/100)
    print("your tax is", tax)
elif( salary < 1000000  ):
    tax = (salary * 20/100)
    print("your tax is", tax)
elif( salary < 1500000 ):
    tax = (salary * 30/100)
    print("your tax is", tax)
else:
    print("invalid")
    
