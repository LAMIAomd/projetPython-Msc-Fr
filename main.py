# ==========================================
# PARTIE 4 : INTERFACE UTILISATEUR (MENU)
# ==========================================
from models import Livre, Utilisateur
import actions

def afficher_menu():
    print("\n=== BIBLIOTHÈQUE PERSONNELLE ===")
    print("1. Ajouter un livre          7. Ajouter un utilisateur")
    print("2. Supprimer un livre        8. Afficher tous les utilisateurs")
    print("3. Rechercher un livre       9. Emprunter un livre")
    print("4. Afficher tous les livres  10. Retourner un livre")
    print("5. Afficher disponibles      11. Statistiques")
    print("6. Afficher empruntés        12. Quitter")

def main():
    # CHARGEMENT DES DONNÉES AU DÉMARRAGE (Livrable 3)
    bibliotheque, utilisateurs = actions.charger_donnees()

    while True:
        afficher_menu()
        choix = input("\nEntrez votre choix : ")

        # --- GESTION DES LIVRES ---
        if choix == "1":
            t = input("Titre : ")
            a = input("Auteur : ")
            try:
                an = int(input("Année : "))
                i = input("ISBN : ")
                nouveau_l = Livre(t, a, an, i)
                # La fonction vérifie maintenant l'ISBN unique
                actions.ajouter_livre(bibliotheque, nouveau_l)
            except ValueError:
                print("Erreur : L'année doit être un nombre entier.")

        elif choix == "2":
            i = input("Entrez l'ISBN du livre à supprimer : ")
            actions.supprimer_livre(bibliotheque, i)

        elif choix == "3":
            print("\n--- OPTIONS DE RECHERCHE ---")
            print("1. Par Titre")
            print("2. Par Auteur")
            sous_choix = input("Votre choix : ")

            if sous_choix == "1":
                t = input("Entrez le titre à rechercher : ")
                resultats = actions.rechercher_par_titre(bibliotheque, t)
                if resultats:
                    for res in resultats: print(res)
                else: print("Aucun livre trouvé.")
            
            elif sous_choix == "2":
                a = input("Entrez l'auteur à rechercher : ")
                resultats = actions.rechercher_par_auteur(bibliotheque, a)
                if resultats:
                    for res in resultats: print(res)
                else: print("Aucun livre trouvé.")
            else:
                print("Option invalide.")

        elif choix == "4":
            actions.afficher_tous_les_livres(bibliotheque)

        elif choix == "5":
            actions.afficher_livres_disponibles(bibliotheque)

        elif choix == "6":
            actions.afficher_livres_empruntes(bibliotheque)

        # --- GESTION DES UTILISATEURS ---
        elif choix == "7":
            n = input("Nom de l'utilisateur : ")
            try:
                id_u = int(input("ID : "))
                utilisateurs.append(Utilisateur(n, id_u))
                print("Utilisateur ajouté.")
            except ValueError:
                print("Erreur : L'ID doit être un nombre entier.")

        elif choix == "8":
            if not utilisateurs:
                print("Aucun utilisateur enregistré.")
            for u in utilisateurs: print(u)

        # --- SYSTÈME D'EMPRUNT / RETOUR ---
        elif choix == "9":
            try:
                id_u = int(input("ID Utilisateur : "))
                isbn_l = input("ISBN du livre : ")
                u = next((user for user in utilisateurs if user.id_utilisateur == id_u), None)
                l = next((livre for livre in bibliotheque if livre.isbn == isbn_l), None)

                if u and l and l.disponible:
                    l.emprunter()
                    u.emprunter_livre(l)
                    print(f"Succès : {u.nom} a emprunté {l.titre}")
                else:
                    print("Erreur : ID/ISBN incorrect ou livre déjà emprunté.")
            except ValueError:
                print("Erreur : ID invalide.")

        elif choix == "10":
            isbn_l = input("ISBN du livre à retourner : ")
            l = next((livre for livre in bibliotheque if livre.isbn == isbn_l), None)
            
            if l and not l.disponible:
                l.retourner()
                # On le retire de la liste de l'utilisateur concerné
                for u in utilisateurs:
                    u.retourner_livre(l)
                print(f"Succès : Le livre {l.titre} a été rendu.")
            else:
                print("Erreur : Ce livre n'est pas marqué comme emprunté.")

        elif choix == "11":
            actions.statistiques(bibliotheque, utilisateurs)

        elif choix == "12":
            # SAUVEGARDE DES DONNÉES AVANT DE QUITTER
            actions.sauvegarder_donnees(bibliotheque, utilisateurs)
            print("Fermeture du programme... Au revoir !")
            break

        else:
            print("Choix invalide, veuillez recommencer.")

if __name__ == "__main__":
    main()