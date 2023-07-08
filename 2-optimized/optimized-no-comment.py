import pandas as pd

pd.set_option("display.max_rows", None, "display.max_columns", None)

my_data = './database/dataset1_Python+P7.csv'
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

    actions = first_result_df['name'].to_list()

    print('====== Data base ======')
    print(first_result_df)
    print('=======================\n')
    print('Liste des actions à acheter :\n')
    print(actions)
    print('=======================\n')
    print("Montant total d'actions achetées : " + str(first_result_sum_price))
    print("Bénéfices : " + str(first_result_benefice))


def main():
    df_sorted = read_data(my_data)
    bag_algorithm(df_sorted, wallet)
    analyse(first_result)


if __name__ == '__main__':
    main()
