
sam_list = [11, 13, 15, 16, 13, 15, 16, 11] 

print ("The list is: " + str(sam_list)) 

result = [] 
for i in sam_list:
 if i not in result: 
  result.append(i) 
print ("The list after removing duplicates : " + str(result))



   

 