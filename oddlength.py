# o/p = [2,8,9,3]
length=[7,3,6,5,1,9,7,5,9]
i=0
odd=[]
while i<=len(length):
    if i%2==0:
        odd.append(length[i])
    i+=1
print(odd)

