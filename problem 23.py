hour=int(input("enter the hour:"))
if hour<=5 and hour>=12:
    print("morning")
elif hour>=12 and hour<=17:
    print("afternoon")
elif hour<=17 and hour>=21:
    print("evening")
else:
    print("night")        
