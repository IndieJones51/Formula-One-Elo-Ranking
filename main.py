import pandas as pd


def k_factor(score):
    if score > 2400:
        return 16
    elif 2100 <= score <= 2400:
        return 24
    else:
        return 32


def probability_of_win(current, opponent):
    return 1 / (1 + 10 ** ((opponent - current) / 400))


drivers_df = pd.read_csv("data/drivers.csv")
drivers_df = drivers_df[['driverId', 'driverRef', 'surname']]
drivers = drivers_df['driverId'].value_counts().keys()

constructors_df = pd.read_csv('data/constructors.csv')
constructors_df = constructors_df[['constructorId', 'constructorRef']]

results_df = pd.read_csv("data/results.csv")
results_df = results_df[
    ['resultId', 'raceId', 'driverId', 'constructorId', 'grid', 'position', 'positionText', 'positionOrder', 'rank']
]

results_df = pd.merge(results_df, drivers_df, how='left', on='driverId')
results_df = pd.merge(results_df, constructors_df, how='left', on='constructorId')

results_df = results_df.sort_values(by=['driverId'], axis=0, inplace=False)

driver_dataframes = [results_df[results_df['driverId'] == id] for id in results_df['driverId'].unique()]
driver_scores = {"name": results_df['driverRef'].unique(),
                 "elo_score": [1000 for x in range(len(results_df['driverRef'].unique()))]
                 }

driver_scores = pd.DataFrame(data=driver_scores['elo_score'], index=driver_scores['name'], columns=['elo_score'])

print(driver_scores.tail())
for driver in driver_dataframes:

    current_name = driver['driverRef'].values[0]

    for race in driver['raceId'].unique():
        current_driver = driver[driver['raceId'] == race]
        opponent_driver = results_df[
            (results_df['raceId'] == race)
            & (results_df['constructorId'] == current_driver['constructorId'].values[0])
            & (results_df['driverId'] != current_driver['driverId'].values[0])
            ]

        """print(current_driver['driverRef'].values[0], "Vs", opponent_driver['driverRef'].values[0])

        if current_driver['positionOrder'].values[0] > opponent_driver['positionOrder'].values[0]:

            current_elo = driver_scores.loc[[current_name]]
            print(current_elo)"""




