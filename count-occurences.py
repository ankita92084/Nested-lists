# Occurences - is made from the word occur which means that ,
# how many times a certain character or word appears.

char = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
a=[]
while i<len(char):
    j=0
    count=0
    while j<len(char):
        if char[i]==char[j]:
            count+=1
        j+=1
    if char[i] in a:
        i+=1
        continue
    a.append(char[i])
    print(char[i],":",count,"times")
    