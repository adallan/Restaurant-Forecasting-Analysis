# Restaurant Forecasting Analysis (Work in progress)

In spring 2023 had a contract to analyze a restaurant’s sales data to forecast the proceeding year's sales. The stakeholder was most interested in the categorical breakdown for menu items and bar sales, particularly the forecasting of them. It being 2024 now, I thought about what I have learned, how I could have done things better and most importantly how accurate was my forecast?

2023 EDA:

Originally I had focused on helping them clean their data, and establish better standards for their data storage while getting my first taste of real-world data. The data was far from clean, with many empty fields for rather important cost-related data, and out-of-date data from the restaurant's conception. I spent a while tackling these and dealing with one of the biggest hurdles for this project, the Point of Sales System (usually called a P.O.S. system). This system is a typical standard in restaurants but this is where all the data is stored and collected. It is very different from any useful database. I found the data I needed to extract from the system and how to do it, extracting it into CSV. 

The main goal of the contract was to make the business an interactable dashboard with the breakdown of sales, item counts and the forecasting for the next year in a easily accessible and readable way for the stakeholders. For this, I needed a time series but how the P.O.S. system worked and stored data did not give date-time data with the other necessary data so I created the time-series myself. Exporting all the cleaned data into a master csv where I utilized VLOOKUP in a Google sheet to collect and create the necessary data. I used Tableau to create the interactable dashboard and included KPIs.

2024 Review and Project Improvement:

Since completing the contract in the spring of 2023 I learned more about pandas and Python for data analysis. I realized instead of manually importing the data into the master Google Sheets and using VLOOKUP to create the time-series I could have done all those hours of work in a few lines of code. Using pandas with boolean masks I easily grabbed the data I wanted without importing a full sheet for a half dozen of rows I wanted. After this, I stored the data in variables and appended it to a copy of the previous master time-series data set. 

Next steps: 
1. Formatting the master time-series to be consistent.
2. New KPIs, analyze and compare the current data to the forecasting.
3. A new dashboard that can be dynamically updated monthly with the extracting and updating functions created.
4. Present findings to the stakeholders.

What I could do further to improve the project:
1. Deepen the time series to daily instead of monthly.
2. Further breakdown the itemized categories of sales and highlight items most profitable with high sales counts.
3. Find a way to interact the the Point of Sales system’s API to gain a constant data steam.
