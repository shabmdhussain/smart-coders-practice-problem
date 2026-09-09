month=int(input("enter the number of month:"))
if month in [1,3,5,7,8,10,12]:
    print("31 days")
elif month==2:
    print("28 or 29 days")
elif month in [4,6,9,11]:
    print("30 days")
else:
    print("invalid")        

       
    
    
