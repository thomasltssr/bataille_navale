from grille import Grille


def story_plouf():
    print("Story : Plouf dans l’eau ")
    g = Grille(5, 8)
    print(g)

    ligne = int(input("Numéro de ligne (0-4) : "))
    colonne = int(input("Numéro de colonne (0-7) : "))

    g.tirer(ligne, colonne)
    print("Résultat du tir :")
    print(g)


if __name__ == "__main__":
    story_plouf()