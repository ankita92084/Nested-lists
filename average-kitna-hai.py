elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sum=0
sum1=0
count=0
counter=0
while i<len(elements):
    if elements[i]%2==0:
        sum+=elements[i]
        count+=1
    else:
        sum1+=elements[i]
        counter+=1
    i+=1
average=sum//count
print("even number sum is:",sum,"average:",average)
print()
print("odd number sum is:",sum1,"average:",sum1//counter)

