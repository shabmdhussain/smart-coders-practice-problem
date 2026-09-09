a=int(input("enter side:"))
b=int(input("enter side:"))
c=int(input("enter side:"))
if a+b>c and a+c>b and b+c>a:
    print("valid triangle")
else:
    print("invalid triangle")    