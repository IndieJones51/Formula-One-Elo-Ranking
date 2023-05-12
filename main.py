import pandas as pd

drivers_df = pd.read_csv("data/drivers.csv")
drivers_df = drivers_df[['driverId','driverRef','surname']]

constructors_df = pd.read_csv('data/constructors.csv')
constructors_df = constructors_df[['constructorId','constructorRef']]

results_df = pd.read_csv("data/results.csv")
results_df = results_df[['resultId','raceId','driverId','constructorId','grid','position','positionText','positionOrder','rank']]

results_df = pd.merge(results_df, drivers_df, how='left', on='driverId')
results_df = pd.merge(results_df, constructors_df, how='left', on='constructorId')

print(results_df.head(10))