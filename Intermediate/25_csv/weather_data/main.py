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
# should get a dataframe
print(type(data))
#print(data["temp"])
series_list = data["temp"]
print(type(series_list))

# Create as a dictionary
data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

num_temps = 0
sum_temps = 0
for temp in temp_list:
    sum_temps += temp
    num_temps += 1
avg_temp = sum_temps / num_temps
print(avg_temp)

#or
print(data["temp"].mean())
print(data["temp"].min())
print(data["temp"].max())

# Also works, column is an attribute
print(data.temp.mean())

# print row
print(data[data.day == "Monday"])

# print highest temp row
print(data[data.temp == data.temp.max()])

#
monday = data[data.day == "Monday"]
print(monday.condition)

# get the temp in Ferinheit
print(monday.temp * (9/5) + 32)