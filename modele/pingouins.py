class Pingouins:
    def __init__(self,id_pingouin,espece,ile,longueur_bec,profondeur_bec,longueur_nageoire,poids,sex,annee_naissance):
        self.id_pingouin = id_pingouin
        self.espece = espece
        self.ile = ile
        self.longueur_bec = longueur_bec
        self.profondeur_bec = profondeur_bec
        self.longueur_nageoire = longueur_nageoire
        self.poids = poids
        self.sex = sex
        self.annee_naissance = annee_naissance

        # Surcharge de la méthode __str__ pour un affichage lisible
        def __str__(self):
            return f"Pingouin {self.id_pingouin}: {self.espece}, Ile: {self.ile}, Poids: {self.poids}kg, Sexe: {self.sex}"

