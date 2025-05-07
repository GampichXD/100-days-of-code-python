#
# with open("weather_data.csv") as file:
#     data = file.readlines()
#
# print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] == 'temp':
#             continue
#         else:
#             temp = int(row[1])
#         temperature.append(temp)
#     print(temperature)

import pandas as pd
#
# # DataFrame ==> The table
# # Series ==> Column
# data = pandas.read_csv('weather_data.csv')
# # print(type(data))
# # print(type(data['temp']))
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data['temp'].to_list()
# all_temp = 0
# for tmp in temp_list:
#     all_temp += tmp
# avg = all_temp/(len(temp_list))
#
#
# print(temp_list)
# print(avg)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# #Get data in Columns
# print(data["condition"])
# print(data.condition)
#
# #Get Data in Row
# print(data[data.day == 'Monday'])
# print(data[data.temp == data["temp"].max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
# print((9/5) * monday.temp + 32)
#
# #Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy","James","Angela"],
#     "score": [76, 56, 65]
# }
# print(pandas.DataFrame(data_dict))
# pandas.DataFrame(data_dict).to_csv("new_data.csv")

data  = pd.read_csv('squirrel_count_dummy.csv')

gray_squirrel = len(data[data['Primary Fur Color'] == "Gray"])
red_squirrel = len(data[data['Primary Fur Color'] == "Cinnamon"])
black_squirrel = len(data[data['Primary Fur Color'] == "Black"])
print(gray_squirrel)
print(red_squirrel)
print(black_squirrel)

data_dict = {
    "Fur Color": ["Gray","Cinnamon","Black"],
    "Count": [gray_squirrel,red_squirrel,black_squirrel]
}
pd.DataFrame(data_dict).to_csv("squirrel_count.csv")