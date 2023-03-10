list=[5,2,6,1]
def trier(list=[5,2,6,1]):
 count=0
 for i in list:
  count+=1
 for i in range(1,count):
    valeur=list[i]
    j=i-1
    while j>=0 and valeur < list[j]:
        list[j+1]=list[j]
        j-=1
        list[j+1]=valeur
 print(list)

