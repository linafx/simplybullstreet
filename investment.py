"""
Name: Kennard Fung
File: investment.py
Date: 10/05/2019
Description: get the big 7 stats for a company's stock
"""
import json
import requests
import sys

def investment(ticker):
	base_url = "https://financialmodelingprep.com/api/v3/financials/"

	# collect data for balance cheet
	balance_sheet_url = base_url + "balance-sheet-statement/" + str(ticker)
	balance_sheet_json = requests.get(balance_sheet_url).json()

	# verify that the stock exists
	if not "financials" in balance_sheet_json:
		return '{"error": "invalid stock ticker"}'

	# collect data for cash flow
	cash_flow_url = base_url + "cash-flow-statement/" + str(ticker)
	cash_flow_json = requests.get(cash_flow_url).json()

	# collect data for income statement
	income_statement_url = base_url + "income-statement/" + str(ticker)
	income_statement_json = requests.get(income_statement_url).json()

	IS_financials = income_statement_json.get("financials")
	CF_financials = cash_flow_json.get("financials")
	BS_financials = balance_sheet_json.get("financials")

	# collect data for the big five criteria
	# CAGR Revenue
	IS_length = len(IS_financials)
	last_revenue = float(IS_financials[0].get("Revenue"))
	last_net_income = float(IS_financials[0].get("Net Income"))

	if IS_length >= 5:
		first_revenue = float(IS_financials[4].get("Revenue"))
		first_net_income = float(IS_financials[4].get("Net Income"))
		year_count = 4
	else:
		first_revenue = float(IS_financials[CF_length - 1].get("Revenue"))
		first_net_income = float(IS_financials[CF_length - 1].get("Net Income"))
		year_count = CF_length

	CAGR_Revenue = (((last_revenue/first_revenue) ** (1/year_count)))
	CAGR_Revenue_rounded = str(round(CAGR_Revenue, 2))

	if CAGR_Revenue >= 1:
		CAGR_Revenue_question = "True"
	else:
		CAGR_Revenue_question = "False"

	#CAGR CAPEX
	CF_length = len(CF_financials)
	last_capex = float(CF_financials[0].get("Capital Expenditure"))
	last_dividends = float(CF_financials[0].get("Dividend payments"))
	last_ops_CF = float(CF_financials[0].get("Operating Cash Flow"))

	if CF_length >= 5:
		first_capex = float(CF_financials[4].get("Capital Expenditure"))
		first_dividends = float(CF_financials[4].get("Dividend payments"))
		year_count = 4
	else:
		first_capex = float(CF_financials[CF_length - 1].get(
			"Capital Expenditure"))
		first_dividends = float(CF_financials[CF_length - 1].get(
			"Dividend payments"))

		year_count = CF_length

	#CAGR Dividends
	try:
		CAGR_Dividends = (((last_dividends/first_dividends) ** (1/year_count)))
		CAGR_Dividends_rounded = str(round(CAGR_Dividends, 2))

		if CAGR_Dividends >= 0:
			CAGR_Dividends_question = "True"
		else:
			CAGR_Dividends_question = "False"
	except:
		CAGR_Dividends_rounded = "None"
		CAGR_Dividends_question = "None"

	#CAGR CAPEX
	CAGR_Capex = (((last_capex/first_capex) ** (1/year_count)))
	CAGR_Capex_rounded = str(round(CAGR_Capex, 2))

	CAGR_Capex_question = str(CAGR_Capex >= 1)

	#Short-Term Debt Ratio
	#Grab short term debt and total assets for the latest year

	st_debt = float(BS_financials[0].get("Short-term debt"))
	total_assets = float(BS_financials[0].get("Total assets"))

	st_debt_ratio = (st_debt/total_assets)
	st_debt_ratio_rounded = str(round(st_debt_ratio, 2))

	st_debt_question = str(st_debt_ratio <= 1)

	#Current Ratio
	current_assets = float(BS_financials[0].get(
		"Total current assets"))
	current_liabilities = float(BS_financials[0].get(
		"Total current liabilities"))

	current_ratio = (current_assets/current_liabilities)
	current_ratio_rounded = str(round(current_ratio, 2))

	current_ratio_question = str(current_ratio >= 1)

	#Capital Acquisition Ratio
	#divide cash flow from ops by CAPEX
	cap_acq = (last_ops_CF/abs(last_capex))
	cap_acq_rounded = str(round(cap_acq, 2))

	cap_acq_question = str(cap_acq >= 1)

	# Quality of Income Ratio
	# divide operating cash flow by net income
	income_quality = (last_ops_CF/last_net_income)
	income_quality_rounded = str(round(income_quality, 2))

	income_quality_question = str(income_quality >= 1)

# ==============================================================================
# ============================= FORMAT OUTPUT ==================================
# ==============================================================================

	#Create a JSON file with all the relevant data
	investment_json = {}

	investment_json["CAGR Revenue"] = CAGR_Revenue_rounded
	investment_json["CAGR Revenue Question"] = CAGR_Revenue_question

	investment_json["CAGR Dividends"] = CAGR_Dividends_rounded
	investment_json["CAGR Dividends Question"] = CAGR_Dividends_question

	investment_json["CAGR Capex"] = CAGR_Capex_rounded
	investment_json["CAGR Capex Question"] = CAGR_Capex_question

	investment_json["Short-Term Debt Ratio"] = st_debt_ratio_rounded
	investment_json["Short-Term Debt Question"] = st_debt_question

	investment_json["Current Ratio"] = current_ratio_rounded
	investment_json["Current Ratio Question"] = current_ratio_question

	investment_json["Capital Acquisition Ratio"] = cap_acq_rounded
	investment_json["Capital Acquisition Question"] = cap_acq_question

	investment_json["Income Quality Ratio"] = income_quality_rounded
	investment_json["Income Quality Question"] = income_quality_question

	investment_json = json.dumps(investment_json)

	return(investment_json)

def main():
	company = sys.argv[1].upper()
	print(investment(company))

if __name__ =="__main__":
	main()
