n=int(input("entrer le rang svp : "))
while n<2 :
    n=int(input("veuillez entrer un rang svp : "))
upp= 0
up=1
print("les termes de la suite sont : ")
print(upp,end="")
print(up,end="")
for i in range(n-1):
    u=upp+up
    print(u,end="")
    upp=up
    up=u