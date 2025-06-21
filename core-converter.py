def convertir_unites(n):
    unites = {
        0: "zéro", 1: "un", 2: "deux", 3: "trois", 4: "quatre",
        5: "cinq", 6: "six", 7: "sept", 8: "huit", 9: "neuf"
    }
    return unites.get(n, "")

def convertir_dizaines(n):
    if n < 10:
        return convertir_unites(n)

    special = {
       11: "onze", 12: "douze", 13: "treize", 14: "quatorze",
        15: "quinze", 16: "seize"
    }

    if n in special:
        return special[n]

    dizaines = {
        1: "dix", 2: "vingt", 3: "trente", 4: "quarante",
        5: "cinquante", 6: "soixante", 7: "soixante-dix",
        8: "quatre-vingt", 9: "quatre-vingt-dix"
    }

    unite = n % 10
    dizaine = n // 10

    if dizaine == 7 or dizaine == 9:
        base = dizaines[dizaine - 1]
        return f"{base}-{convertir_dizaines(10 + unite)}"
    else:
        base = dizaines.get(dizaine, "")
        if unite == 0:
            return base
        elif unite == 1 and dizaine != 8:
            return f"{base}-et-un"
        else:
            return f"{base}-{convertir_unites(unite)}"

def convertir_centaines(n):
    if n < 100:
        return convertir_dizaines(n)

    centaines = n // 100
    reste = n % 100
    if centaines == 1:
        prefix = "cent"
    else:
        prefix = f"{convertir_unites(centaines)}-cent"

    if reste == 0:
        return prefix
    else:
        return f"{prefix} et {convertir_dizaines(reste)}"
    if name == "main":
        for nombre in [4, 17, 21, 64, 75, 88, 101, 234, 999]:
            print(f"{nombre} : {convertir_centaines(nombre)}")