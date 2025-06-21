import re

def nettoyer_saisie(saisie):
    """Nettoie la saisie : supprime espaces et remplacer la virgule par un point."""
    return saisie.strip().replace(',', '.')

def valider_saisie(saisie):
    """Valide que la saisie est bien un nombre (entier ou décimal, avec ou sans signe)."""
    motif = r'^-?\d+(\.\d+)?$'
    return re.match(motif, saisie)

def parser_nombre(saisie):
    """
    Analyse la saisie :
    - Détecte le signe
    - Sépare partie entière et décimale
    - Retourne proprement les morceaux
    """
    saisie_nettoyée = nettoyer_saisie(saisie)
    if not valider_saisie(saisie_nettoyée):
        raise ValueError("Format invalide")

    signe = '-' if saisie_nettoyée.startswith('-') else ''
    valeur = saisie_nettoyée.lstrip('-')

    if '.' in valeur:
        partie_entiere, partie_decimale = valeur.split('.')
    else:
        partie_entiere, partie_decimale = valeur, None

    return int(partie_entiere), partie_decimale, signe