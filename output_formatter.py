def assembler_texte(signe, partie_entiere, partie_decimale=None):
    """Assemble les parties du nombre en une seule phrase fluide."""
    prefixe = "moins " if signe == '-' else ''
    if not partie_decimale:
        return f"{prefixe}{partie_entiere}"
    return f"{prefixe}{partie_entiere} virgule {partie_decimale}"

def format_output(original, texte_final, detail=None):
    """Assemble l’affichage utilisateur."""
    result = f"Nombre saisi       : {original}\nEn lettres          : {texte_final}"
    if detail:
        result += f"\nForme détaillée     : {detail}"
    return result
#fonction qui compte le nombre de mot 
def count_words(phrase):
    """Compte le nombre de mots utiles dans une phrase."""
    return len(phrase.replace('-', ' ').split())


#fonction prenant en parametre une chaine et un fichier txt qui enregistre chacune des converstion
def save_to_history(chaine, fichier="historique.txt"):
    """Ajoute la conversion dans un fichier texte."""
    with open(fichier, "a", encoding="utf-8") as file:
        file.write(chaine + "\n\n")