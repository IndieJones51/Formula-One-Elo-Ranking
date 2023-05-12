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


def updated_score(score):

    return score + k_factor(score) * ()

drivers_df = pd.read_csv("data/drivers.csv")
drivers_df = drivers_df[['driverId','driverRef','surname']]

constructors_df = pd.read_csv('data/constructors.csv')
constructors_df = constructors_df[['constructorId','constructorRef']]

results_df = pd.read_csv("data/results.csv")
results_df = results_df[['resultId','raceId','driverId','constructorId','grid','position','positionText','positionOrder','rank']]

results_df = pd.merge(results_df, drivers_df, how='left', on='driverId')
results_df = pd.merge(results_df, constructors_df, how='left', on='constructorId')

results_df['Elo'] = 1000

drivers = results_df['driverId'].value_counts().keys()


for driver in drivers:

    driver_df = results_df[results_df['driverId'] == driver]

    races = driver_df['raceId'].value_counts().keys()
    teams = driver_df['constructorId'].value_counts().keys()

    for race in races:

        for team in teams:

            race_df = driver_df[(driver_df['raceId'] == race) & (driver_df['constructorId'] == team)]
            opponent_df = results_df[(results_df['driverId'] != driver) & (results_df['raceId'] == race) & (results_df['constructorId'] == team)]

            if len(race_df) != 0 and len(opponent_df) != 0:

                current_elo = race_df['Elo'].values[0]
                opponent_elo = race_df['Elo'].values[0]

                current_probability = Elo.probability_of_win
                opponent_probability = 1 - current_probability



                print(race_df['surname'].values[0], race_df['positionOrder'].values[0], race_df['Elo'].values[0], opponent_df['surname'].values[0], opponent_df['positionOrder'].values[0], race_df['Elo'].values[0])






