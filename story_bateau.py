from grille import Grille
from bateau import Bateau


def story_bateau():
    print("Story : Test des bateaux avec chevauchement 🚢\n")

    g = Grille(6, 8)

    b1 = Bateau(2, 2, longueur=3)
    b2 = Bateau(4, 1, longueur=2, vertical=True)
    b3 = Bateau(2, 3, longueur=3) 

    print("Ajout du bateau b1 :", "OK" if g.ajoute(b1) else "Échec")
    print("Ajout du bateau b2 :", "OK" if g.ajoute(b2) else "Échec")
    print("Ajout du bateau b3 :", "OK" if g.ajoute(b3) else "Échec (chevauchement)")

    print("\nGrille finale :")
    print(g)


if __name__ == "__main__":
    story_bateau()