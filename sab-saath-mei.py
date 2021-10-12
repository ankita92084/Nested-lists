elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
even=0
odd=0
sum=0
sum1=0
while i<len(elements):
    if elements[i]%2==0:
        sum+=elements[i]
        even+=1
    else:
        sum1+=elements[i]
        odd+=1
    i+=1
print("count of even numbers :",even)
print("count of odd numbers  :",odd)
print("even number sum: ",sum)
print("odd number sum: ",sum1)
print("average of even: ",sum//even)
print("average of odd: ",sum1//odd)