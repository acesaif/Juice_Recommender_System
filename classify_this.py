import os
import csv
import time
import numpy as np
import pandas as pd

df = pd.read_csv('juices_modified_dataset.csv')
df = df.reset_index()
# df = df.reindex(np.random.permutation(df.index))

heading = list(df.columns)
print(heading)

foods = df.values.tolist()

def segregate_everything():

	heading = list(df.columns)

	cold_only = [heading]
	sorethroat_only = [heading]
	fever_only = [heading]

	cold_sorethroat = [heading]
	sorethroat_fever = [heading]
	cold_fever = [heading]

	cold_sorethroat_fever = [heading]

	for item in range(len(df)):
		if df['disease_cold'][item] == 1 and df['disease_sorethroat'][item] == 1 and df['disease_fever'][item] == 1:
			cold_sorethroat_fever.append(foods[item])
		if df['disease_cold'][item] == 1 and df['disease_sorethroat'][item] == 1 and not df['disease_fever'][item] == 1:
			cold_sorethroat.append(foods[item])
		if df['disease_sorethroat'][item] == 1 and df['disease_fever'][item] == 1 and not df['disease_cold'][item] == 1:
			sorethroat_fever.append(foods[item])
		if df['disease_cold'][item] == 1 and df['disease_fever'][item] == 1 and not df['disease_sorethroat'][item] == 1:
			cold_fever.append(foods[item])
		if df['disease_cold'][item] == 1 and not df['disease_sorethroat'][item] == 1 and not df['disease_fever'][item] == 1:
			cold_only.append(foods[item])
		if not df['disease_cold'][item] == 1 and df['disease_sorethroat'][item] == 1 and not df['disease_fever'][item] == 1:
			sorethroat_only.append(foods[item])
		if not df['disease_cold'][item] == 1 and not df['disease_sorethroat'][item] == 1 and df['disease_fever'][item] == 1:
			fever_only.append(foods[item])

	diseases = ['cold_only','sorethroat_only','fever_only','cold_sorethroat','sorethroat_fever','cold_fever','cold_sorethroat_fever']

	main_path = os.getcwd()

	for flu in diseases:
		os.makedirs(str(flu))
		os.chdir(str(flu))
		data = eval(flu)
		with open(str(flu)+'.csv', 'w') as dt:
			writer = csv.writer(dt)
			writer.writerows(data)
		os.chdir(main_path)

segregate_everything()

print('finished')
