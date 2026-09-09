a=int(input("enter a side:"))
b=int(input("enter a side:"))
c=int(input("enter a side:"))
if a==b and b==c:
    print("equilateral triangle")
elif a==b or b==c and a==c:
    print("isoceles triangle")
else:
    print("scalene triangle")        