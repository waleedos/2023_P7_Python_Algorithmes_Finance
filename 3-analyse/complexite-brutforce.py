import csv
import time
import matplotlib.pyplot as plt
from itertools import combinations
from termcolor import colored

MAX_INVEST = 500 * 100


def get_csv_data():
    with open("data/brutforce.csv", newline="") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader)
        for row in csv_reader:
            stock_name = row[0]
            price_in_cents = float(row[1]) * 100
            benefit_in_cents = float(row[2]) * 100
            yield (stock_name, int(price_in_cents), int(benefit_in_cents))


def generate_combinations(stocks):
    profit = 0
    best_combination = []
    for i in range(len(stocks)):
        list_combinations = combinations(stocks, i + 1)
        for combination in list_combinations:
            total_cost = sum([stock[1] for stock in combination])
            if total_cost <= MAX_INVEST:
                total_profit = sum([stock[2] for stock in combination])
                if total_profit > profit:
                    profit = total_profit
                    best_combination = combination
    return best_combination


def display_result(best_combination):
    print(colored("Liste des actions achetées :\n", "green"))
    for stock in best_combination:
        print(f"{stock[0]} {stock[1] / 100}€ {stock[2] / 100}€")
    print(colored(f"\nSomme dépensée : {sum([stock[1] for stock in best_combination]) / 100}€", "blue"))
    print(colored(f"Profit total : {sum([stock[2] for stock in best_combination]) / 100}€", "red"))


def main():
    sizes = []
    times = []
    stocks = [stock for stock in get_csv_data()]
    total_start_time = time.time()

    for i in range(1, len(stocks)+1):
        start_time = time.time()
        best_combination = generate_combinations(stocks[:i])
        end_time = time.time()
        execution_time = round(end_time - start_time, 3)
        sizes.append(i)
        times.append(execution_time)
        display_result(best_combination)

    total_end_time = time.time()
    total_execution_time = round(total_end_time - total_start_time, 3)
    print(colored(f"Total execution time: {total_execution_time} s", "magenta"))

    plt.plot(sizes, times, 'o-')
    plt.xlabel('Taille de l\'ensemble de données')
    plt.ylabel('Temps d\'exécution (s)')
    plt.title('Analyse empirique de la complexité du temps d\'exécution')
    plt.grid(True)
    plt.savefig('output_brutforce.png')  # Sauvegarder la figure dans un fichier .png


if __name__ == "__main__":
    main()
