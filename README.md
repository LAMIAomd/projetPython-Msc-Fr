# Système de Gestion de Bibliothèque Personnelle - Rapport Technique

## 1. Présentation du Projet
Ce logiciel permet de gérer une collection de livres, des membres (utilisateurs) et le flux des emprunts/retours. Il a été développé en Python dans le cadre du projet final TC SPRING M1 2026.

## 2. Détails du Code Source

### A. Architecture (models.py)
Le projet utilise la **Programmation Orientée Objet (POO)** pour structurer les données :
- **Classe `Livre`** : 
    - Attributs : `titre`, `auteur`, `annee`, `isbn`, `disponible`.
    - Méthodes : `emprunter()` et `retourner()` qui basculent l'état booléen du livre.
- **Classe `Utilisateur`** : 
    - Attributs : `nom`, `id_utilisateur`, `livres_empruntes` (une liste d'objets).
    - Méthodes : `emprunter_livre()` et `retourner_livre()` pour mettre à jour la liste personnelle du membre.

### B. Logique Métier (actions.py)
Ce fichier contient les fonctions de manipulation des structures de données (Listes) :
- **Gestion** : Fonctions pour ajouter ou supprimer des livres par ISBN.
- **Recherche** : Algorithme de filtrage pour trouver un livre par son titre.
- **Statistiques** : Calcul dynamique du nombre de livres, d'utilisateurs et du taux d'occupation.

### C. Persistance des Données (JSON)
Le programme assure la conservation des données entre deux utilisations :
- **Sauvegarde** : Les listes d'objets sont converties en dictionnaires et enregistrées dans `data.json` lors de la fermeture (Option 12).
- **Chargement** : Au démarrage, le programme scanne le fichier `data.json` pour recréer les objets `Livre` et `Utilisateur` et restaurer l'état de la bibliothèque.

### D. Interface Utilisateur (main.py)
Le point d'entrée du programme gère un **menu interactif à 12 options** :
- Utilisation d'une boucle `while True` pour maintenir l'application ouverte.
- **Gestion des erreurs** : Intégration de blocs `try...except` sur les saisies numériques (ID et Année) pour garantir la robustesse du programme et éviter les arrêts brutaux.

## 3. Guide d'utilisation
1. Lancer le terminal dans le dossier du projet.
2. Exécuter la commande : `python main.py`.
3. Naviguer dans le menu en tapant le chiffre correspondant à l'action souhaitée.
4. **Important** : Toujours quitter via l'option **12** pour garantir la sauvegarde des données.

## 4. Grille de conformité
- **POO** : Validé (Classes et méthodes implémentées).
- **Structures de données** : Validé (Listes et dictionnaires).
- **Entrées/Sorties** : Validé (Menu interactif).
- **Gestion des erreurs** : Validé (Exceptions gérées).
- **Persistance** : Validé (Lecture/Écriture JSON).

---
 Équipe de Projet Informatique :  OUMMAD Lamia, BOUZEKRAOUI Youssef, BACHA Rabah (groupe 2, MSC1 FR)