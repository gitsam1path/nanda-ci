import pytest
from prix import calcul_prix

def test_prix_standard():
    assert calcul_prix(10) == 700

def test_prix_personnalise():
    assert calcul_prix(10, prix_km=100, frais=0) == 1000

def test_distance_invalide():
    with pytest.raises(ValueError):
        calcul_prix(0)
