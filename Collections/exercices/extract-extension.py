## LES COLLECTIONS : LISTES / TUPLES
# Exercice "Extraire les extensions"

# extraire extension
def extraire_extensions(nom_fichier):
    nom_fichier_split = nom_fichier.split(".")
    if len(nom_fichier_split) > 1:
        return nom_fichier_split[-1]
    return None

def obtenir_definition_extension(extension, definitions):
    for definition in definitions:
        if definition[0].lower() == extension.lower():
            return definition[1]
    return "Extension non connue"



fichiers = ("notepad.exe", "mon.fichier.perso.doc", "notes.TXT", "vacances.jpeg", "planning", "data.dat")

definition_extensions = (("doc", "Document Word"),
                        ("exe", "Executable"),
                        ("txt", "Document Texte"),
                        ("jpeg", "Image JPEG"))

definition_extensions_dict = {"doc": "Document Word",
                        "exe": "Executable",
                        "txt": "Document Texte",
                        "jpeg": "Image JPEG"}



'''
notepad.exe (Executable)
mon.fichier.perso.doc (Document Word)
notes.TXT (Document Texte)
vacances.jpeg (Image JPEG)
planning (Aucune extension)
data.dat (Extension non connue)
'''
## lower/upper
## in  /index /for
## spli

for fichier in fichiers:
    ext = extraire_extensions(fichier)
    if ext:
        ## Use liste
        #definition = obtenir_definition_extension(ext, definition_extensions)
        ## en utilisant le dictionnaire
        definition = definition_extensions_dict.get(ext.lower())
        print(f"{fichier} ({definition})")
        if not definition:
            definition = "Extension non connue"
    else:
        print(f"{fichier} (Aucune extension)")