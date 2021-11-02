arr=["kirtee",23,49,"53","sagarika"]
i=0
a=[]
while i<len(arr):
    if type(arr[i])==str:
        a.append(arr[i])
    i+=1
print(a)

