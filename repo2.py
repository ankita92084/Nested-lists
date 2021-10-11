list1 = [[78, 76, 94, 86, 88], [91, 71, 98, 65],[95, 45, 78]]
i=0
while i<len(list1):
    j=0
    sum=0
    while j<len(list1[i]):
        sum=sum+list1[i][j]
        j+=1
    print(sum//len(list1[i]))
    i+=1
