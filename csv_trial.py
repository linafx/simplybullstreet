import csv
import json
import ast

inflation_csv = open("CPI.csv", 'r')
inflation_json = open("CPI_data.json", 'w')

reader = csv.DictReader(inflation_csv)
jsonList = []

for row in reader:
	jsonList.append(ast.literal_eval(json.dumps(row)))

inflation_json.write(str(jsonList))
inflation_json.close()


# inflation_json = list(open("inflation_data.json", 'r'))
#
# x = (ast.literal_eval(inflation_json[0]))
#
# y = json.dumps(x)
# print(type(y))


#print(x[5].get("DATE"))



# data = json.loads(x)
# print(data)

# print('[', end='')
# for obj in jsonList:
# 	if not (obj == jsonList[-1]):
# 		print(obj, end=',\n')
# 	else:
# 		print(obj)
# print(']')


# inflation_json = inflation_data.json()
# print(inflation_json)

# inflation_json = open("inflation.json", 'w')

# inflation_collection = {}

# for i in range(1, count):
# 	inflation_collection.append(inflation_data[i])

# inflation_json.write(inflation_collection)
