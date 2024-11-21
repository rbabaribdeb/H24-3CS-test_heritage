from Exemples_Poo.ville import Ville
from Exemples_Poo.capitale import Capitale

v1 = Ville(99, "Ca", 4000000)
print(v1)
c1 = Capitale("quebec", "Ca", 500000, "parlement")
print(c1)
c2 = Capitale("Ottawa", "Ca", 1000000, "parlement")
# Polymorphisme ????
l=[]
l.append(v1)
l.append(c1)
l.append(c2)

print(type(l[0]), type(l[1]) ) # plusieurs formes
for i in l:
    print(i.type_ville()) # se comportent de la meme maniere
