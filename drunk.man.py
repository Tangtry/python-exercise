import random
p=0.5
sum=0
k=0
while k <1000 :
    x=0
    i=1
    if random.random()>p :
        x=x+1
    else :
        x=x-1
    while x!=0:
        i=i+1
        if random.random()>p :
            x=x+1
        else :
            x=x-1
       
    sum = sum + i
    k =k+1
print sum/1000
