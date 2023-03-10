i = 1


while i<=1000:
    j=1
    counter=0
    while j<=i:
        if i%j==0:
            counter+=1
        j+=1
    if counter==2:
        print(i)
    i+=1

 