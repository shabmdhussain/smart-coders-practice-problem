age=int(input("enter the age:"))
if age<5:
    price=0
    print("ticket price=",price)
elif age<=12:
    price=50
    print("ticket price=",price)
elif age<=59:
    price=100
    print("ticket price=",price)
else:
    price=50
    print("ticket price=",price)
            