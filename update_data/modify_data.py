import csv
import numpy as np
import pandas as pd

df = pd.read_csv('juice_dataset.csv')
juices = df.values.tolist()

for row in range(len(df)):
	if juices[row][2] == 1 and juices[row][3] != 1 and juices[row][4] != 1:
		juices[row].append('cold')
	if juices[row][3] == 1 and juices[row][2] != 1 and juices[row][4] != 1:
		juices[row].append('soarthroat')
	if juices[row][4] == 1 and juices[row][2] != 1 and juices[row][3] != 1:
		juices[row].append('fever')
	if juices[row][2] == 1 and juices[row][3] == 1 and juices[row][4] != 1:
		juices[row].append('cold_soarthroat')
	if juices[row][3] == 1 and juices[row][4] == 1 and juices[row][2] != 1:
		juices[row].append('soarthroat_fever')
	if juices[row][2] == 1 and juices[row][4] == 1 and juices[row][3] != 1:
		juices[row].append('cold_fever')
	if juices[row][2] == 1 and juices[row][3] == 1 and juices[row][4] == 1:
		juices[row].append('cold_soarthroat_fever')

modified_data = [['fid', 'juice_name', 'disease_cold', 'disease_soarthroat', 'disease_fever', 'disease_curing']]

for data_row in juices:
	modified_data.append(data_row)

with open('juices_modified_dataset.csv', 'w') as dt:
	writer = csv.writer(dt)
	writer.writerows(modified_data)

print('finished')
