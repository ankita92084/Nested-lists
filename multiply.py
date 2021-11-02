a=[1,2,3,4,5,6,7,8]
i=0
b=[]
m=1
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
        m=m*a[i]
    i+=1
print(m)
