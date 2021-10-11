list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7]
i=0
a=[]
while i<len(list1):
    k=list1[i]
    if k not in list2:
        a.append(k)
    i+=1
print(a)