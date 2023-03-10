my_sum=[]
def even():
 L=[8, 24, 27, 48, 2,16, 9, 7, 84, 91]
 my_sum=[]
 i = 0
 x = len(L)
 while x<=len(L):
  for x in L:
   if L[i]%2==0:
    
    my_sum.append(L[i])
    i+=1
   else:
    i+=1
 print(sum(my_sum))

even()