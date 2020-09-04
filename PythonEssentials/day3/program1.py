altitude = int(input("Enter altitude:"))

if altitude<=1000:
    print("Land the plane")
elif altitude>1000 and altitude<=5000:
    print("Bring down to 1000ft")
else:
    print("Turn Around")
