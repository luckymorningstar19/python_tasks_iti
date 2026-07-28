text = input("enter text to found the location of the i:\n")

location = 0

for step in text:
    if step =="i":
        print("location of i is ",location)
    else:
        location=location+1    
