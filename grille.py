class Grille:
    def __init__(self, lignes, colonnes):
        self.lignes = lignes
        self.colonnes = colonnes
        self.vide = '🌊'
        self.touche = 'X'
        self.grille = [self.vide] * (lignes * colonnes)

    def tirer(self, ligne, colonne, touche='X'):
        if 0 <= ligne < self.lignes and 0 <= colonne < self.colonnes:
            index = ligne * self.colonnes + colonne
            self.grille[index] = touche
        else:
            raise ValueError("Coordonnées hors de la grille")

    def __str__(self):
        texte = ""
        for l in range(self.lignes):
            ligne = ""
            for c in range(self.colonnes):
                idx = l * self.colonnes + c
                ligne += self.grille[idx]
            texte += ligne + "\n"
        return texte.strip()