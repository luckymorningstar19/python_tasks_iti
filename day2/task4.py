def answer(apples,size):
    total_apples=sum(apples)
    size_sorted=sorted(size,reverse=True)

    boxes=0
    apples_held=0

    for i in size_sorted:
        if apples_held>=total_apples:
            break
        apples_held=apples_held + i
        boxes=boxes+1
    return boxes  

apples = [10, 20, 15]
capacity = [15, 5, 15, 10]  
print(answer(apples, capacity)) 