"""
Name: Kennard Fung
File: inflation.py
Date: 10/05/2019
Description: Gets CPI data Federal Reserve Economic Data to
visualize how the value of money changes over time.
"""

import ast
import json

def inflation(money = 100):
	#If the input isn't an integer, return an error message.
	try:
		test = money + 1
	except TypeError:
		return("Invalid Value")

	#If all good, grab the CPI data
	inflation_data = list(open("CPI_data.json", "r"))
	inflation_data = ast.literal_eval(inflation_data[0])

	inflation_numbers_to_push = {}
	adjusted_money = []
	dates = []

	#The graph will be sloping downwards.
	#divide 100 by the CPI number for each year.
	#multiply that by money
	for x in range(len(inflation_data)):
		dates.append(inflation_data[x].get('DATE'))
		adjusted_money.append(100.0/float(inflation_data[x].get('CPIAUCSL')) * float(money))

	#now put all that data into inflation_numbers_to_push
	for x in range(len(dates)):
		inflation_numbers_to_push[str(dates[x])] = adjusted_money[x]

	#convert to json
	inflation_numbers_to_push = json.dumps(inflation_numbers_to_push)
	return(inflation_numbers_to_push)


print(inflation())
