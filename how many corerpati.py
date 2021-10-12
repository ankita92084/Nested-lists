kitna = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i=0
count=0
counter=0
people=0
while i<len(kitna):
    if kitna[i]>100000 and kitna[i]<10000000:
        count+=1
    elif kitna[i]<100000:
        counter+=1
    else:
        people+=1
    i+=1
print("lakhpati:",count)
print("dilwale :",counter)
print("crorepati:",people)
