# Restaurant Forecasting Analysis

In spring 2023 had a contract to analyze a restaurant’s sales data to forecast the proceeding year's sales. The stakeholder was most interested in the categorical breakdown for menu items and bar sales, particularly the forecasting of them. It being 2024 now, I thought about what I have learned, how I could have done things better and most importantly how accurate was my forecast?

2023 EDA:

Originally I had focused on helping them clean their data, and establish better standards for their data storage while getting my first taste of real-world data. The data was far from clean, with many empty fields for rather important cost-related data, and out-of-date data from the restaurant's conception. I spent a while tackling these and dealing with one of the biggest hurdles for this project, the Point of Sales System (usually called a P.O.S. system). This system is a typical standard in restaurants but this is where all the data is stored and collected. It is very different from any useful database. I found the data I needed to extract from the system and how to do it, extracting it into CSV. 

The main goal of the contract was to make the business an interactable dashboard with the breakdown of sales, item counts and the forecasting for the next year in an easily accessible and readable way for the stakeholders. For this, I needed a time series but how the P.O.S. system worked and stored data did not give date-time data with the other necessary data so I created the time-series myself. Exporting all the cleaned data into a master csv where I utilized VLOOKUP in a Google sheet to collect and create the necessary data. I used Tableau to create the interactable dashboard and included KPIs.

2024 Review and Project Improvement:

Since completing the contract in the spring of 2023 I learned more about pandas and Python for data analysis. I realized instead of manually importing the data into the master Google Sheets and using VLOOKUP to create the time-series I could have done all those hours of work in a few lines of code. Using pandas with boolean masks I easily grabbed the data I wanted without importing a full sheet for a half dozen of rows I wanted. After this, I stored the data in variables and appended it to a copy of the previous master time-series data set. 

See here for detailed code for data extraction and appending to master time series: https://github.com/adallan/Restaurant-Forecasting-Analysis/blob/main/data-extraction.py

The next steps included formatting the time-series to be consistent and interact with Tableau properly (ex. data formatting, tableau can mistake the month as day resulting in all data being in January), altering the data source of the dashboard to the new time series and re-adjusting the updated dashboard. Afterwards, new KPIs were created and the new data was analyzed. Using the previous dashboard and the data gathered for 2023 I compared and analyzed all forecasting options and combinations of seasonality to gather a new dataset and analyze which forecasting model was most accurate for the sales data. A new dashboard was generated for this project visualization, altering sales numbers, and food and bar categorized items to anonymize the dashboard and protect the data privacy of the stakeholder's company. 

See here for the anonymized dashboard: https://public.tableau.com/app/profile/alexander.allan/viz/RestaurantSalesForecasting/Dashboard1

Conclusion:
After comparing and analyzing four forecasting models forecast of Net Sales, Net Profit and Profit Margin of 2023 with the actual data from 2023 I found the following:
1. Additive Forecasting with No Seaonality (the original forecasting I went with) was pretty off the totals for Net Sales and Net Profit but oddly accurate on the Profit Margin average, this may be because of the incredibly high profit margin of December 2023 (over 10% higher than a normal month and historical data, implying it could be missing data or an outlier)   
2. Additive Forecasting with Additive Seasonality and Additive Forecasting with Multiplicative Seasonality were incredibly close on most numbers and were by far the more accurate in predicting Net Sales and Net Profit but Additive forecasting with Additive Seasonality was more accurate of the two in predicting Profit Margin.
3. Multiplicative Forecasting with Multiplicative Seasonality was fairly accurate at predicting Net Profit and Profit Margin but where it fell short of the others was in Net Sales where the model would start to become skewered over the year, being accurate in the first two-quarters numbers would be overinflated by the end of the year.

In conclusion, the Additive forecasting model with Additive seasonality was the most accurate and was used for the updated dashboard for the stakeholders.
Insights:
Over the past 2 years, there has been a consistent spike in sales in the March-April and December months. I recommend increasing staffing and inventory in these months.
Starting in March throughout the summer and in November-December beer sales historically have a high increase, perfect month for things like beer specials perhaps food pairing to increase sales further since there is already an interest in local beers these months.
Dinner sales start to drop off in the fall, perhaps a good area to push specials and deals on coursed dinners to catch up to the burger sales.

What I could do further to improve the project:
1. Deepen the time series to daily instead of monthly.
2. Further breakdown the itemized categories of sales and highlight items most profitable with high sales counts.
3. Find a way to interact the the Point of Sales system’s API to gain a constant data steam. 
