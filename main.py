import random
from grille import Grille
from bateau import PorteAvion, Croiseur, Torpilleur, SousMarin

def afficher_grille_visible(g):
    """Affiche la grille sans les bateaux (pour le joueur)."""
    texte = ""
    for l in range(g.lignes):
        ligne = ""
        for c in range(g.colonnes):
            idx = l * g.colonnes + c
            case = g.grille[idx]
            if case in ['💣', '❌', '💥']:  
                ligne += case
            else:
                ligne += g.vide  
        texte += ligne + "\n"
    return texte.strip()

def afficher_solution(g):
    """Affiche la grille réelle (avec bateaux)."""
    return str(g)


g = Grille(8, 10)
bateaux_classes = [PorteAvion, Croiseur, Torpilleur, SousMarin]
liste_bateaux = []


for bateau_cls in bateaux_classes:
    positions_valides = []
    for ligne in range(g.lignes):
        for colonne in range(g.colonnes):
            for vertical in [True, False]:
                b_test = bateau_cls(ligne, colonne, vertical=vertical)
                ok = g.ajoute(b_test)
                if ok:
                    positions_valides.append((ligne, colonne, vertical))
                    for (l, c) in b_test.positions:
                        g.grille[l * g.colonnes + c] = g.vide  
    if not positions_valides:
        raise ValueError(f"Impossible de placer {bateau_cls.__name__}")
    ligne, colonne, vertical = random.choice(positions_valides)
    bateau_final = bateau_cls(ligne, colonne, vertical=vertical)
    g.ajoute(bateau_final)
    liste_bateaux.append(bateau_final)


coups = 0

while liste_bateaux:
    print("\n=== Grille de jeu ===")
    print(afficher_grille_visible(g))
    tir_input = input("Entrez la ligne du tir (0-7), 's' pour solution, ou 'q' pour quitter : ")

    if tir_input.lower() in ['q', 'quit']:
        print("Vous avez quitté la partie.")
        break
    if tir_input.lower() == 's':
        print("\n=== SOLUTION ===")
        print(afficher_solution(g))
        input("\nAppuyez sur Entrée pour revenir au jeu...")
        continue


    tir_colonne = input("Entrez la colonne du tir (0-9) ou 'q' pour quitter : ")
    if tir_colonne.lower() in ['q', 'quit']:
        print("Vous avez quitté la partie.")
        break

    try:
        tir_ligne = int(tir_input)
        tir_colonne = int(tir_colonne)
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        continue

    if not (0 <= tir_ligne < g.lignes and 0 <= tir_colonne < g.colonnes):
        print("Coordonnées hors de la grille.")
        continue

    coups += 1
    touché = False
    for b in liste_bateaux:
        if (tir_ligne, tir_colonne) in b.positions:
            touché = True
            break

    if touché:
        g.tirer(tir_ligne, tir_colonne, touche='💣')
        print("Touché !")
    else:
        g.tirer(tir_ligne, tir_colonne, touche='❌')
        print("Manqué !")


    bateaux_coules = []
    for b in liste_bateaux:
        if b.coule(g):
            bateaux_coules.append(b)
            for (l, c) in b.positions:
                g.grille[l * g.colonnes + c] = '💥'
            print(f"Bateau coulé ! 💥")

    for b in bateaux_coules:
        liste_bateaux.remove(b)


if not liste_bateaux:
    print(f"\nFélicitations ! Tous les bateaux sont coulés en {coups} coups.")