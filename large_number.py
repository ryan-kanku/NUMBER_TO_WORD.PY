from core_converter import convertir_centaines, convertir_unites

def convertir_grands_nombres(n):
    """Gère milliers et millions (jusqu’à 999 999 999 pour l'instant)."""
    if n < 1000:
        return convertir_centaines(n)
    
    millions = n // 1_000_000
    milliers = (n % 1_000_000) // 1000
    reste = n % 1000

    morceaux = []

    if millions:
        prefixe = "un" if millions == 1 else convertir_centaines(millions)
        morceaux.append(f"{prefixe} million{'s' if millions > 1 else ''}")
    if milliers:
        prefixe = "mille" if milliers == 1 else f"{convertir_centaines(milliers)} mille"
        morceaux.append(prefixe)
    if reste:
        morceaux.append(convertir_centaines(reste))

    return ' '.join(morceaux)

def convertir_decimale(decimal_str):
    """Convertit chaque chiffre décimal en lettres avec espaces."""
    return ' '.join(convertir_unites(int(ch)) for ch in decimal_str if ch.isdigit())

