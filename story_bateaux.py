from grille import Grille
from bateau import PorteAvion, Croiseur, Torpilleur, SousMarin

print("Story : Test des sous-classes de bateaux 🚢 🚤 🚣 🐟")

g = Grille(6, 6)

pa = PorteAvion(0, 0) 
cr = Croiseur(1, 2, vertical=True)
tp = Torpilleur(4, 1) 
sm = SousMarin(5, 4)  

g.ajoute(pa)
g.ajoute(cr)
g.ajoute(tp)
g.ajoute(sm)

print("\n Grille après ajout des bateaux :")
print(g)