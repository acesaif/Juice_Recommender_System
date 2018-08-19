import os
import csv
import time
import numpy as np
import pandas as pd

df = pd.read_csv('juice_dataset.csv')
df = df.reset_index()
# df = df.reindex(np.random.permutation(df.index))

foods = df.values.tolist()

def segregate_everything():

	heading = list(df.columns)

	cold_only = [heading]
	soar_only = [heading]
	fever_only = [heading]

	cold_soar = [heading]
	soar_fever = [heading]
	cold_fever = [heading]

	cold_soar_fever = [heading]

	for item in range(len(df)):
		if df['cold'][item] == 1 and df['soar_throat'][item] == 1 and df['fever'][item] == 1:
			cold_soar_fever.append(foods[item])
		if df['cold'][item] == 1 and df['soar_throat'][item] == 1 and not df['fever'][item] == 1:
			cold_soar.append(foods[item])
		if df['soar_throat'][item] == 1 and df['fever'][item] == 1 and not df['cold'][item] == 1:
			soar_fever.append(foods[item])
		if df['cold'][item] == 1 and df['fever'][item] == 1 and not df['soar_throat'][item] == 1:
			cold_fever.append(foods[item])
		if df['cold'][item] == 1 and not df['soar_throat'][item] == 1 and not df['fever'][item] == 1:
			cold_only.append(foods[item])
		if not df['cold'][item] == 1 and df['soar_throat'][item] == 1 and not df['fever'][item] == 1:
			soar_only.append(foods[item])
		if not df['cold'][item] == 1 and not df['soar_throat'][item] == 1 and df['fever'][item] == 1:
			fever_only.append(foods[item])

	diseases = ['cold_only','soar_only','fever_only','cold_soar','soar_fever','cold_fever','cold_soar_fever']

	main_path = os.getcwd()

	for flu in diseases:
		os.makedirs(str(flu))
		os.chdir(str(flu))
		data = eval(flu)
		with open(str(flu)+'.csv', 'w') as dt:
			writer = csv.writer(dt)
			writer.writerows(data)
		os.chdir(main_path)

# segregate_everything()
