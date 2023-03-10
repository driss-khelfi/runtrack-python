type = 'fruits'
saison = 'hiver'

def fruit_de_saison():
 if type == 'fruits' and saison == 'hiver':
  print ('orange, mandarine et kiwi')
 elif type == 'fruits' and saison == 'printemps':
  print ('Poire, fraise et cassis')
 elif type == 'fruits' and saison == 'hiver':
  print ('carotte, topinambour, endive')
 elif type == 'fruits' and saison == 'ete':
  print ('artichaut, aubergine, navet')
 return type
 return saison

print(saison)



