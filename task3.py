lst1=["mohamed","osama","ahmed","ali","osman"]

dict1 = dict()
for name in lst1:

    first_letter = name[0]

    if first_letter in dict1:
        dict1[first_letter].append(name)
    else:
        dict1[first_letter] = [name]

sort=sorted(dict1.keys())
print(sort)
sorted_result = {}
for key in sort:
    sorted_result[key] = sorted(dict1[key])

print(sorted_result)

