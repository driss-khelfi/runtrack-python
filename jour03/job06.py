alpha = ""

def pyramide(str, x):
    count = 0
    ligne=""
    for i in range(x):
        for y in range(count, count+i):
            while y>=len(str):
                 y-=len(str)
            if count >=len(str):
                count -=len(str)
            ligne+=str[y]
            count+=1
        print(ligne)
        ligne=""

pyramide("abcdefghijklmnopqrstuvwxyz", 10)

