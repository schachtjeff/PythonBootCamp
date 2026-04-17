# Imports
import csv

# Read all the lines, but everything is in string
#with open('weather_data.csv') as csv_file:
#    data = csv_file.readlines()

#print(data)

#Use csv to put into a proper list
#with open('weather_data.csv') as csv_file:
#    data = csv.reader(csv_file)
#    temperatures = []
#    skip_num = 0
#    for row in data:
#        if skip_num > 0:
#            temperatures.append(int(row[1]))
#        skip_num += 1
#    print(temperatures)

import pandas

data = pandas.read_csv('weather_data.csv')
print(data["temp"])