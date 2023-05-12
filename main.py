import pandas as pd

drivers_df = pd.read_csv("data/drivers.csv")
drivers_df = drivers_df[['driverId','driverRef','surname']]

constructors_df = pd.read_csv('data/constructors.csv')
constructors_df = constructors_df[['constructorId','constructorRef']]

results_df = pd.read_csv("data/results.csv")
results_df = results_df[['resultId','raceId','driverId','constructorId','grid','position','positionText','positionOrder','rank']]

results_df = pd.merge(results_df, drivers_df, how='left', on='driverId')
results_df = pd.merge(results_df, constructors_df, how='left', on='constructorId')


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

                print(race_df)
                print(opponent_df)






