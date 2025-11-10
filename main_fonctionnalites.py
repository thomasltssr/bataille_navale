from grille import Grille
from bateau import PorteAvion, Croiseur, Torpilleur, SousMarin

print("=== Test de fonctionnalité : placement et tir sur un bateau ===")

g = Grille(6, 6)

pa = PorteAvion(0, 0)
ok = g.ajoute(pa)
print(f"Placement du Porte-avion réussi ? {ok}")
print(g)

g.tirer(2, 2, touche='❌')
print("Après tir raté (❌) :")
print(g)

g.tirer(0, 1, touche='💣')
print("Après tir touché (💣) :")
print(g)

coule = pa.coule(g)
print(f"Le Porte-avion est-il coulé ? {coule}")

for l, c in pa.positions:
    g.tirer(l, c, touche='💣')

coule = pa.coule(g)
print(f"Après tous les tirs, le Porte-avion est-il coulé ? {coule}")
print("Grille finale :")
print(g)