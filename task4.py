name = input("please enter your name\n")

if name == "" or name.isdigit():
    print("wrong name")
else:
    print("access approved")

email = input("please enter mail\n")

if "@" in email and "." in email:
    print("correct email")
else:
    print("wrong email")

print("name:", name, "\nemail:", email)