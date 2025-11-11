import pytest
from grille import Grille


def test_init():
    g = Grille(5, 8)
    assert len(g.grille) == 40
    assert all(c == g.vide for c in g.grille)


def test_tirer_valide():
    g = Grille(3, 3)
    g.tirer(1, 1)
    assert g.grille[4] == g.touche  


def test_tirer_invalide():
    g = Grille(3, 3)
    with pytest.raises(ValueError):
        g.tirer(5, 5)