def calcul_prix(distance, prix_km=50, frais=200):
    """Calcule le prix d'un trajet en FCFA."""
    if distance <= 0:
        raise ValueError("La distance doit être positive")
    return distance * prix_km + frais
