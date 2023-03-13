height = int(input("Entrez la hauteur : "))
width = int(input("Entrez la largeur : "))

side = "|"
separator = "-"
i=0
while i<height:
 for Range in range(height):
     if Range == 0 or Range == height -1:
        separator = "-"
        i= i+1
     else: 
      separator = " "
      i = i+1


print(side + separator * height + side)
