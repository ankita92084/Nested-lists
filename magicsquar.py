magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
i=0
while i<len(magic_square):
    j=0
    sum=0
    while j<len(magic_square):
        sum=sum+magic_square[i][j]
        j+=1
    print("row :",sum)
    a=0
    sum1=0
    while a<len(magic_square):
        sum1=sum1+magic_square[a][i]
        a+=1
    print("column:",sum)
    i+=1
p=0
for i in range (len(magic_square)):
    for c in range(len(magic_square[i])):
        if i==c:
            p=p+magic_square[i][c]
print("diagolous",p)
s=0
for i in range(len(magic_square)):
        for c in range(len(magic_square[i])):
            if i+c==len(magic_square[i])-1:
                s=s+magic_square[i][c]
print("diagnolous",s)

            






