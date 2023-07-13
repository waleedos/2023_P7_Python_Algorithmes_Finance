import pandas as pd
import time
import matplotlib.pyplot as plt
from colorama import Fore, Style

pd.set_option("display.max_rows", None, "display.max_columns", None)

my_data_files = ['./data/dataset1_Python+P7.csv', './data/dataset2_Python+P7.csv']
wallet = 500
first_result = {}


def read_data(my_data):
    df = pd.read_csv((my_data), sep=",")
    df['benefice'] = df['price'] * df['profit'] / 100
    df_sorted = df.loc[
        (df['price'] > 0) & (df['price'] <= wallet) & (df['benefice'] > 0)
    ].sort_values(by=['profit'], ascending=False)
    return df_sorted


def bag_algorithm(df_sorted, wallet):
    for i in range(0, len(df_sorted)):
        action = df_sorted.iloc[i]['price']
        test = wallet - action

        if action < wallet and test > 0:
            first_result[df_sorted.iloc[i]['name']] = [
                df_sorted.iloc[i]['name'],
                df_sorted.iloc[i]['price'],
                df_sorted.iloc[i]['profit'],
                df_sorted.iloc[i]['benefice']
            ]
            wallet -= action


def analyse(first_result):
    first_result_df = pd.DataFrame.from_dict(
            first_result,
            orient='index',
            columns=['name', 'price', 'profit', 'benefice']
        ).reset_index().drop(columns=['index'])

    first_result_sum_price = sum(first_result_df['price'].to_list())
    first_result_benefice = sum(first_result_df['benefice'].to_list())

    '''actions = first_result_df['name'].to_list()'''

    print('============== Data base ===============')
    print(first_result_df)
    print('========================================')
    print(Fore.MAGENTA + "Total d'actions achetées : " + str(round(first_result_sum_price, 2)) + '€')
    # impression la somme des prix des actions achetées.
    print("Total des Bénéfices Net  : " + str(round(first_result_benefice, 2)) + '€' + Style.RESET_ALL)
    # impression de la somme des bénéfices des actions achetées.


def main():
    sizes = []
    times = []
    for my_data in my_data_files:
        # Réinitialisation du dictionnaire pour chaque fichier
        first_result.clear()

        start_time = time.time()  # Marquer le temps de début

        df_sorted = read_data(my_data)
        bag_algorithm(df_sorted, wallet)
        analyse(first_result)

        end_time = time.time()  # Marquer le temps de fin
        execution_time = round(end_time - start_time, 3)  # Calculer le temps d'exécution

        print(f"{Fore.RED}Temps d'exécution        : {execution_time} secondes{Style.RESET_ALL}\n")
        # Afficher le temps d'exécution en secondes

        print(f"{Fore.BLUE}\nFin de l'analyse du fichier {my_data} {Style.RESET_ALL}\n")

        sizes.append(len(df_sorted))
        times.append(execution_time)

    # Tracer le temps d'exécution en fonction de la taille de l'ensemble de données
    plt.plot(sizes, times, 'o-')
    plt.xlabel('Taille de l\'ensemble de données')
    plt.ylabel('Temps d\'exécution (s)')
    plt.title('Analyse empirique de la complexité du temps d\'exécution')
    plt.grid(True)
    plt.savefig('output-optimised.png')  # Sauvegarder la figure dans un fichier .png


if __name__ == '__main__':
    main()
