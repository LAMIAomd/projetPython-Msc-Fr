import json
from models import Livre, Utilisateur

# ==========================================
# PARTIE 3 : FONCTIONS ET STRUCTURES DE DONNÉES
# ==========================================

def ajouter_livre(bibliotheque, livre):
    """Ajoute un livre si l'ISBN est unique (Critère de l'énoncé)"""
    # Vérification de l'unicité de l'ISBN
    if any(l.isbn == livre.isbn for l in bibliotheque):
        print(f"Erreur : Un livre avec l'ISBN {livre.isbn} existe déjà.")
        return False
    
    bibliotheque.append(livre)
    print(f"Succès : Le livre '{livre.titre}' a été ajouté.")
    return True

def supprimer_livre(bibliotheque, isbn):
    """Supprime un livre en cherchant son ISBN unique"""
    for l in bibliotheque:
        if l.isbn == isbn:
            bibliotheque.remove(l)
            print(f"Succès : Le livre {isbn} a été supprimé.")
            return
    print("Erreur : Aucun livre trouvé avec cet ISBN.")

def rechercher_par_titre(bibliotheque, titre):
    """Retourne une liste de livres dont le titre correspond"""
    return [l for l in bibliotheque if titre.lower() in l.titre.lower()]

def rechercher_par_auteur(bibliotheque, auteur):
    """Retourne les livres d'un auteur spécifique (Demandé Partie 3)"""
    return [l for l in bibliotheque if auteur.lower() in l.auteur.lower()]

def afficher_tous_les_livres(bibliotheque):
    """Affiche la totalité de la collection"""
    if not bibliotheque:
        print("La bibliothèque est vide.")
    for l in bibliotheque:
        print(l)

def afficher_livres_disponibles(bibliotheque):
    """Filtre et affiche uniquement les livres avec disponible=True"""
    dispos = [l for l in bibliotheque if l.disponible]
    if not dispos:
        print("Aucun livre disponible.")
    for l in dispos: print(l)

def afficher_livres_empruntes(bibliotheque):
    """Affiche uniquement les livres empruntés"""
    empruntes = [l for l in bibliotheque if not l.disponible]
    if not empruntes:
        print("Aucun livre emprunté.")
    for l in empruntes: print(l)

def statistiques(bibliotheque, utilisateurs):
    """Affiche les chiffres clés et livres empruntés (Partie III.8)"""
    print("\n" + "="*30)
    print("   STATISTIQUES GÉNÉRALES")
    print("="*30)
    print(f"Nombre total de livres : {len(bibliotheque)}")
    print(f"Nombre d'utilisateurs  : {len(utilisateurs)}")
    
    empruntes = [l for l in bibliotheque if not l.disponible]
    print(f"Livres en cours d'emprunt : {len(empruntes)}")
    
    if empruntes:
        print("\nDétail des livres empruntés :")
        for l in empruntes:
            print(f" - {l.titre} (ISBN: {l.isbn})")
            
    if len(bibliotheque) > 0:
        taux = (len(empruntes) / len(bibliotheque)) * 100
        print(f"\nTaux d'occupation : {taux:.1f}%")
    print("="*30)

# ==========================================
# NOUVEAU : SAUVEGARDE ET CHARGEMENT (JSON)
# ==========================================

def sauvegarder_donnees(bibliotheque, utilisateurs):
    """Enregistre les listes dans un fichier JSON pour la persistance"""
    data = {
        "livres": [
            {
                "titre": l.titre, 
                "auteur": l.auteur, 
                "annee": l.annee, 
                "isbn": l.isbn, 
                "disponible": l.disponible
            } for l in bibliotheque
        ],
        "utilisateurs": [
            {
                "nom": u.nom, 
                "id": u.id_utilisateur
            } for u in utilisateurs
        ]
    }
    
    try:
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print("\n[INFO] Données sauvegardées dans 'data.json'.")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde : {e}")

def charger_donnees():
    """Récupère les données du fichier JSON au démarrage"""
    try:
        with open("data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            
            biblio = []
            for l in data["livres"]:
                nouveau_l = Livre(l["titre"], l["auteur"], l["annee"], l["isbn"])
                nouveau_l.disponible = l["disponible"]
                biblio.append(nouveau_l)
            
            users = []
            for u in data["utilisateurs"]:
                users.append(Utilisateur(u["nom"], u["id"]))
                
            print("[INFO] Données chargées avec succès.")
            return biblio, users
            
    except (FileNotFoundError, json.JSONDecodeError):
        print("[INFO] Aucune donnée existante, démarrage à vide.")
        return [], []