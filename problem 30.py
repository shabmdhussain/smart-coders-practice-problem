a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
op=input("enter operator(+,-,*,/):")
if op=='+':
    print("answer=",a+b)
elif op=='-':
    print("answer=",a-b)
elif op=='*':
    print("answer=",a*b)
elif op=='/':
    print("answer=",a/b)
else:
    print("invalid operator")
        