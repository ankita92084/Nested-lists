a=[1,2,3,4,7,8]
i=0
p=[]
while i<len(a):
    p.append(str(a[i])+str(a[i+1]))
    i+=2
print(p)

