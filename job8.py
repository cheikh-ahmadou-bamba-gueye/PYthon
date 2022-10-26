h = int(input("hauteur: "))
l = int(input("largeur: "))
c = "l"
e = "-"

for i in range (h):
     if i == 0 or i == h -1:
        e = "-"
     else :
        e = " "
        print (c + e * l + c)   