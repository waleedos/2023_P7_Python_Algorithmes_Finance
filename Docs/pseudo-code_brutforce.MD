# PSEUDO-CODE de l’Algorithme BRUTEFORCE

## 1 : Définir MAX_INVEST comme 500 * 100. Cela représente le budget maximal que nous pouvons investir.

## 2 : Définir une fonction get_csv_data:
    - Ouvrir le fichier brutforce.csv pour la lecture.
    - Pour chaque ligne du fichier (en ignorant la première ligne qui est l'en-tête):
        - Extraire le nom de l'action, le prix et le bénéfice.
        - Convertir le prix et le bénéfice de l'euro en centimes.
        - Renvoyer le nom de l'action, le prix en centimes et le bénéfice en centimes comme une ligne de données.
        
## 3 : Définir une fonction generate_combinations:
    - Initialiser une variable profit à 0. Cela représente le profit maximal actuel.
    - Initialiser une liste best_combination vide. Cela représente la meilleure combinaison d'actions actuelle.
    - Pour chaque sous-ensemble d'actions (obtenues en utilisant l'algorithme de combinaisons, de taille 1 à la taille totale des actions): 
        - Calculer le coût total de la combinaison d'actions.
        - Si le coût total est inférieur ou égal à MAX_INVEST:
            - Calculer le profit total de la combinaison d'actions.
            - Si le profit total est supérieur au profit maximal actuel:
                -  Mettre à jour le profit maximal et la meilleure combinaison d'actions.

## 4 :  Définir une fonction display_result:
    - Afficher le nom de chaque action, son prix et son bénéfice dans la meilleure combinaison d'actions.
    - Calculer et afficher la somme dépensée et le profit total.

## 5 : Si le script est exécuté en tant que programme principal:
    - Appeler la fonction get_csv_data pour obtenir les actions.
    - Appeler la fonction generate_combinations pour obtenir la meilleure combinaison d'actions.
    - Appeler la fonction display_result pour afficher le résultat. 
                    