# Simple-Stock

## Introduction and Inspiration

Investing is a complex process, so we wanted to make understanding stocks a much, much simpler process. With Simple-Stock, we provide stock metrics in plain English that people can use to make decisions on their stock positions.

Historically, regular folks have gotten the short end of the stick when it comes to investing information. A 2011 study by Griffin et al. demonstrated that retail investors, individual investors, continued to pour money into the 2000s dot-com bubble market, even after it was apparent that the whole market was tanking hard. Large institutional investors with more market information, on the other hand, exited their positions faster and protected relatively much more of their capital. This asymmetrical information flow caused many people to lose their livelihoods.

With time, market information has become more symmetrical, but this information is either theory spread out through many pages, or an over-over-simplification that causes people to over rely on professional analyst predictions. Web resources such as Investopedia, SeekingAlpha and Wall Street Survivor got created to educate people and share ideas about the methods of investing in different sorts of asset classes, be it stocks, bonds, options, futures, forex, etc. However, unless people already invest their time into researching stocks, their time is better spent elsewhere. Additionally, some sites provide esoteric information about analyst predictions, usually in the form of "Sell," "Hold," and "Buy". If people act upon these recommendations, they have autonomy in physically dealing with stocks, but they rest their overall decision to deal on those analysts.

Overall, Simple-Stock strives to provide a balance between too-much and too-little information. We respect people's time, and we respect that they have better things to do. So we give them information that they understand and can act upon on quickly.

## Running the Web Application

Clone the Simple-Stock folder. Cd into it. npm run dev.

## What it does

Type in the stock symbol of a company of interest, for example, Take-Two Interactive (TTWO) or Proctor & Gamble (PG). The program will output a historical chart of prices, which the user can toggle through (1-year, 2-year, 3-year history). Additionally, there are valuation seven metrics that appear, with a "True" or "False" rating. Generally and relatively, true is good, false is bad. The plain english explanations are available on the read-me at the moment

## How we built it

Ken Data Analytics-Python
Nathan Backend-Node
Khalid Frontend-React

## What's next!

Improving the appearance of the overall UI.
Adding sector-specific information and averages to make the stock indicators more relevant.
Adding more features like bond and forex investing metrics.
Adding other financial literacy features like debt, inflation and wealth growth visualization charts.

## Plain English Stock Indicator Explanations

CAGR: Compounded Annual Growth Rate. Better than average growth rate, especially when growth moves up and down
a lot throughout the years.

CAGR Revenue: Growth rate of money the company is bringing in from selling things
and interest money every year. More revenue is better.

CAGR Dividends: Growth rate of money the company is giving away to investors.
More dividends is better.

CAGR Capex: Growth rate of money the company is spending on buying and
fixing things like buildings and land. More is better, especially if company is
growing.

Short-term debt ratio: Short-term refers to a year. The ability of company to
pay off its short-term debt with the things that they own. Anything below 1 is
good; the lower the better.

Current Ratio: Current refers to a year. The ability of company to pay off its
current liabilities with its current assets. Anything above 1 is good, generally
the higher the better.

Capital Acquisition Ratio: The ability of a company to manage paying for things
like land and buildings. Anything above 1 is good, generally
the higher the better.

Income Quality Ratio: Ratio of cash the company is actually pocketing after
paying for things like taxes. Anything above 1 is good, generally
the higher the better.
