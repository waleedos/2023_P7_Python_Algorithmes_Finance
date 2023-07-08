import csv
# Importe le module CSV pour lire et écrire des fichiers CSV

from itertools import combinations
# Importe la fonction combinations qui produit toutes les combinaisons possibles de certains éléments

MAX_INVEST = 500 * 100
# Définit une variable globale MAX_INVEST qui représente le budget maximum (500 euros convertis en centimes)


def get_csv_data():
    # Définit une fonction qui ne prend aucun argument

    """
    Get data from csv file

    :return: list of tuples
    """

    with open("../data/brutforce.csv", newline="") as csv_file:
        # Ouvre le fichier CSV en mode lecture

        csv_reader = csv.reader(csv_file, delimiter=",")
        # Crée un lecteur CSV pour lire le fichier

        next(csv_reader)
        # Passe la première ligne (en-tête du fichier CSV)

        for row in csv_reader:
            # Pour chaque ligne du fichier

            stock_name = row[0]
            # Le nom de l'action est le premier élément de la ligne

            # convert price from € to cents
            price_in_cents = float(row[1]) * 100
            # Le prix de l'action est le deuxième élément, converti de l'euro aux centimes

            # calculate benefit in cents
            benefit_in_cents = float(row[2]) * 100
            # Le bénéfice de l'action est le troisième élément, converti de l'euro aux centimes

            yield (stock_name, int(price_in_cents), int(benefit_in_cents))
            # Produit un tuple (nom de l'action, prix, bénéfice)


def generate_combinations(stocks):  # Définit une fonction qui prend une liste d'actions comme argument
    """
    Generate all cominations with the given elements

    :param actions: list of tuples (tuple = stock)
    :return list: best stocks combinations
    """

    profit = 0
    # Initialise le profit à 0

    best_combination = []
    # Initialise la meilleure combinaison à une liste vide

    for i in range(len(stocks)):
        # Pour chaque nombre de 0 à la longueur de la liste d'actions

        list_combinations = combinations(stocks, i + 1)
        # Génère toutes les combinaisons possibles de i + 1 actions

        for combination in list_combinations:
            # Pour chaque combinaison

            total_cost = sum([stock[1] for stock in combination])
            # Calcule le coût total de la combinaison

            if total_cost <= MAX_INVEST:
                # Si le coût total ne dépasse pas le budget maximum

                total_profit = sum([stock[2] for stock in combination])
                # Calcule le profit total de la combinaison

                if total_profit > profit:
                    # Si le profit total est supérieur au meilleur profit trouvé jusqu'à présent

                    profit = total_profit
                    # Met à jour le meilleur profit

                    best_combination = combination
                    # Met à jour la meilleure combinaison

    return best_combination
    # Renvoie la meilleure combinaison


def display_result(best_combination):
    # Définit une fonction qui prend la meilleure combinaison d'actions comme argument
    """Display informations about the best combination

    @param best_combination: list of stocks
    """

    print("Liste des actions achetées :\n")
    # Affiche un message

    for stock in best_combination:
        # Pour chaque action dans la meilleure combinaison

        print(f"{stock[0]} {stock[1] / 100}€ {stock[2] / 100}€")
        # Affiche le nom, le prix et le bénéfice de l'action en euros

    print(f"\nSomme dépensée : {sum([stock[1] for stock in best_combination]) / 100}€")
    # Affiche le coût total en euros

    print(f"Profit total : {sum([stock[2] for stock in best_combination]) / 100}€")
    # Affiche le profit total en euros


if __name__ == "__main__":
    # Si ce script est exécuté comme programme principal (et non importé comme module)

    stocks = [stock for stock in get_csv_data()]
    # Lit les données du fichier CSV et les stocke dans une liste

    best_combination = generate_combinations(stocks)
    # Trouve la meilleure combinaison d'actions à acheter

    display_result(best_combination)
    # Affiche les résultats
