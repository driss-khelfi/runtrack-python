def product():
 L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
 my_prod = []
 i = 0
 j = 0
 x = len(L)
 y = len (my_prod)
 while x<=len(L):
  for x in L:
   if L[i]>=25 and L[i]<=90:
    my_prod.append(L[i])
    
    while y<=1:
     my_prod[y]*my_prod[y-1]
    i+=1
   else:
    i+=1
  print(my_prod)

product()

