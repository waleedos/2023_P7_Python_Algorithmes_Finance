import csv
from itertools import combinations

MAX_INVEST = 500 * 100


def get_csv_data():
    with open("data/brutforce.csv", newline="") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader)

        for row in csv_reader:
            stock_name = row[0]

            # convert price from € to cents
            price_in_cents = float(row[1]) * 100

            # calculate benefit in cents
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
    print("Liste des actions achetées :\n")

    for stock in best_combination:
        print(f"{stock[0]} {stock[1] / 100}€ {stock[2] / 100}€")

    print(f"\nSomme dépensée : {sum([stock[1] for stock in best_combination]) / 100}€")
    print(f"Profit total : {sum([stock[2] for stock in best_combination]) / 100}€")


if __name__ == "__main__":
    stocks = [stock for stock in get_csv_data()]
    best_combination = generate_combinations(stocks)
    display_result(best_combination)
