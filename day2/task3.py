lst=["aba", "aa", "ad", "vcd", "aba"]
max_length=0
for i in lst:
    if len(i)>=max_length:
        max_length= len(i)

final_list=list()
for i in lst:
    if len(i)==max_length:
        final_list.append(i)
    else:
        continue


print(final_list)
        
