# ==========================================
# PARTIE 1 & 2 : PROGRAMMATION ORIENTÉE OBJET
# ==========================================

class Livre:
    """Classe représentant un livre de la bibliothèque"""
    def __init__(self, titre, auteur, annee, isbn):
        # Initialisation des attributs requis par l'énoncé
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.isbn = isbn
        self.disponible = True  # Par défaut, le livre est présent

    def __str__(self):
        # Méthode pour afficher les informations du livre (Partie I)
        etat = "Disponible" if self.disponible else "Emprunté"
        return f"Livre: {self.titre} | Auteur: {self.auteur} | ISBN: {self.isbn} | État: {etat}"

    def emprunter(self):
        # Marque le livre comme indisponible
        self.disponible = False

    def retourner(self):
        # Marque le livre comme disponible
        self.disponible = True

class Utilisateur:
    """Classe représentant un membre de la bibliothèque"""
    def __init__(self, nom, id_utilisateur):
        self.nom = nom
        self.id_utilisateur = id_utilisateur
        self.livres_empruntes = []  # Liste pour stocker les objets Livre

    def __str__(self):
        # Affiche les infos de l'utilisateur (Partie II)
        return f"Utilisateur: {self.nom} (ID: {self.id_utilisateur}) | Livres: {len(self.livres_empruntes)} emprunté(s)"

    def emprunter_livre(self, livre):
        # Ajoute l'objet livre à la liste de l'utilisateur
        self.livres_empruntes.append(livre)

    def retourner_livre(self, livre):
        # Retire le livre de la liste s'il est présent
        if livre in self.livres_empruntes:
            self.livres_empruntes.remove(livre)