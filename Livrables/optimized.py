import pandas as pd
import time  # Importer le module time
from colorama import Fore, Style


pd.set_option("display.max_rows", None, "display.max_columns", None)
# configuration de pandas pour qu'il affiche toutes les lignes et colonnes lorsqu'on imprime un DataFrame. Par défaut,
# pandas n'affiche qu'un certain nombre de lignes et colonnes pour ne pas surcharger la console.

my_data_files = ['data/dataset1_Python+P7.csv', 'data/dataset2_Python+P7.csv']
# définition du chemin d'accès vers le fichier CSV qui contient les données.

wallet = 500
# définition d'une variable wallet qui représente le montant d'argent initial disponible.

first_result = {}
# définition d'un dictionnaire vide qui sera utilisé plus tard pour stocker les résultats de notre algorithme.


def read_data(my_data):
    # définit une fonction read_data qui prend en paramètre une chaîne de caractères représentant le chemin d'accès
    # vers un fichier CSV.

    df = pd.read_csv((my_data), sep=",")
    # utilisation de la fonction read_csv de pandas pour lire le fichier CSV et créer un DataFrame. Le paramètre
    # sep="," indique que les valeurs dans le fichier CSV sont séparées par des virgules.

    df['benefice'] = df['price'] * df['profit'] / 100
    # Nous créons une nouvelle colonne dans le DataFrame appelée benefice. Pour chaque ligne, la valeur dans cette
    # colonne est calculée en multipliant la valeur de price par la valeur de profit et en divisant par 100.

    df_sorted = df.loc[
        (df['price'] > 0) & (df['price'] <= wallet) & (df['benefice'] > 0)
    ].sort_values(by=['profit'], ascending=False)
    # Nous filtrons le DataFrame pour ne conserver que les lignes où price est supérieur à 0, price est inférieur ou
    # égal à wallet, et benefice est supérieur à 0. Ensuite, on trie les lignes restantes en fonction de la colonne
    # profit dans l'ordre décroissant. Le DataFrame filtré et trié est stocké dans df_sorted.

    return df_sorted
    # On retourne df_sorted à la fin de la fonction.


def bag_algorithm(df_sorted, wallet):
    # définit une fonction bag_algorithm qui prend en paramètre un DataFrame et un montant d'argent.

    for i in range(0, len(df_sorted)):
        # Nous créons une boucle for qui itère sur chaque ligne du DataFrame.

        action = df_sorted.iloc[i]['price']
        # On récupère le prix de l'action à l'index i.

        test = wallet - action
        # Nous calculons combien d'argent il resterait si nous achetions l'action.

        if action < wallet and test > 0:
            # Nous vérifions si on a assez d'argent pour acheter l'action et si il nous restera de l'argent après
            # l'achat.

            first_result[df_sorted.iloc[i]['name']] = [
                df_sorted.iloc[i]['name'],
                df_sorted.iloc[i]['price'],
                df_sorted.iloc[i]['profit'],
                df_sorted.iloc[i]['benefice']
            ]
            # Si nous pouvons acheter l'action, on ajoute une entrée au dictionnaire first_result. La clé est le nom
            # de l'action et la valeur est une liste contenant le nom, le prix, le profit et le bénéfice de l'action.

            wallet -= action
            # On soustrait le prix de l'action du montant d'argent disponible.


def analyse(first_result):
    # Définition de la fonction "analyse" qui prend en paramètre un dictionnaire.

    first_result_df = pd.DataFrame.from_dict(
            first_result,
            orient='index',
            columns=['name', 'price', 'profit', 'benefice']
        ).reset_index().drop(columns=['index'])
    # On convertit le dictionnaire first_result en DataFrame. On définit les colonnes du DataFrame comme name,
    # price, profit et benefice. On réinitialise ensuite l'index et supprime la colonne index originale.

    first_result_sum_price = sum(first_result_df['price'].to_list())
    # On calcule la somme des prix des actions achetées.

    first_result_benefice = sum(first_result_df['benefice'].to_list())
    # On calcule la somme des bénéfices des actions achetées.

    print('\n============== Data base ===============')
    # impression d'une chaîne de caractères pour séparer visuellement les sections de la sortie.
    print(first_result_df)
    # Impression du DataFrame qui contient les résultats de notre algorithme.
    print('========================================')
    # Impression d'une chaîne de caractères pour séparer visuellement les sections de la sortie.
    print(Fore.MAGENTA + "Total d'actions achetées : " + str(round(first_result_sum_price, 2)) + '€')
    # impression la somme des prix des actions achetées.
    print("Total des Bénéfices Net  : " + str(round(first_result_benefice, 2)) + '€' + Style.RESET_ALL)
    # impression de la somme des bénéfices des actions achetées.


def main():
    for my_data in my_data_files:
        # Réinitialisation du dictionnaire pour chaque fichier
        first_result.clear()

        start_time = time.time()  # Marquer le temps de début

        df_sorted = read_data(my_data)
        bag_algorithm(df_sorted, wallet)
        analyse(first_result)

        end_time = time.time()  # Marquer le temps de fin

        print(f"{Fore.RED}Temps d'exécution        : {round(end_time - start_time, 3)} secondes{Style.RESET_ALL}")
        # Afficher le temps d'exécution en millisecondes

        print(f"{Fore.BLUE}\nFin de l'analyse du fichier {my_data} {Style.RESET_ALL}\n")


if __name__ == '__main__':
    main()
