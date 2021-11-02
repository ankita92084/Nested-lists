l=[2,4,[9,4,7,[5,4,3],6,7,8]]
i = 0
a = []
sum=0
while i<len(l):
    if type(l[i]) == list :
        j = 0
        while j<len(l[i]):
            if type(l[i][j])==list:
                k=0
                while k<len(l[i][j]):
                    a.append(l[i][j][k])
                    sum=sum+l[i][j][k]
                    k+=1
            else:
                a.append(l[i][j])
                sum=sum+l[i][j]
            j+=1
    else:
        a.append(l[i])
        sum=sum+l[i]
    i+=1
print(a)
print(sum)
