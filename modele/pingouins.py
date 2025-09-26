# Classe représentant un pingouin
class Pingouins:
    # Constructeur : initialise un objet Pingouins avec toutes ses caractéristiques
    def __init__(self, id_pingouin, espece, ile, longueur_bec, profondeur_bec, longueur_nageoire, poids, sex, annee_naissance):
        self.id_pingouin = id_pingouin          # Identifiant unique du pingouin
        self.espece = espece                      # Espèce du pingouin
        self.ile = ile                            # Île d'origine ou de vie du pingouin
        self.longueur_bec = longueur_bec          # Longueur du bec en cm
        self.profondeur_bec = profondeur_bec      # Profondeur du bec en cm
        self.longueur_nageoire = longueur_nageoire # Longueur de la nageoire en cm
        self.poids = poids                        # Poids du pingouin en kg
        self.sex = sex                            # Sexe du pingouin ('M' ou 'F')
        self.annee_naissance = annee_naissance    # Année de naissance

    # Surcharge de la méthode __str__ pour un affichage lisible de l'objet
    # Cela permet de faire par exemple: print(pingouin) et obtenir un texte compréhensible
    def __str__(self):
        return f"Pingouin {self.id_pingouin}: {self.espece}, Ile: {self.ile}, Poids: {self.poids}kg, Sexe: {self.sex}"
