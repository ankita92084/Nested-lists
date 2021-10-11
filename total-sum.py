number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19]
i=0
p=[]
while i<len(n):
    j=0
    while i>j:
        if n[i]+n[j]==number:
            p.append([n[i],n[j]])
        j+=1
    i+=1
print(p)
