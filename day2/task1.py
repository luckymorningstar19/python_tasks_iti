text = input("please enter any text to count the vowels in the sentence \n")
count = 0
for i in text :
    if i == "a" :
        count=count+1
    elif i=="e":
        count=count+1
    elif i=="i":
        count=count+1
    elif i=="o":
        count=count+1
    elif i=="u":
        count=count+1                 
print("number of vowels :",count)    