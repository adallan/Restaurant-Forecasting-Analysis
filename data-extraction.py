#Create a function to clean all the headers off data. The headers and totals have the exact same name.
#Create or overwrite old csvs
def clean_sales_data(Month):
    base_path = '/data location/'
    data = pd.read_csv(base_path+Month+' '+'2023 Sales Data.csv')
    # The headers have a Null or NaN Count column.
    cleaned_data = data[data['Count'].notna()]
    df.to_csv(base_path+Month+' '+'2023 Sales by Inv.csv')

#Function that extracxts the necessary data and returns a tuple of it to be stored in a variable
def data_extraction(Month):
    base_path = '/user_location/folder_containg_data'
    df = pd.read_csv(base_path+'Sales Data File Folder/'+Month+' '+'2023 Sales.csv')
    # Drop Blank row created by cleaning function 
    df = df.drop('Unnamed: 0.1',axis=1)
    #Masks
    #First row has no header, Pandas gives it 'Unnamed: 0'
    burger_mask = df['Unnamed: 0'] == 'Burgers'
    main_menu_mask = df['Unnamed: 0'] == 'Main Menu'
    sides_mask = df['Unnamed: 0'] == 'Sides'
    lunch_mask = df['Unnamed: 0'] == 'Lunch Items'
    misc_food_mask = df['Unnamed: 0'] == 'Misc Food'
    cocktail_catergory1_mask = df['Unnamed: 0'] == 'Cocktails type 1'
    cocktail_catergory2_mask= df['Unnamed: 0'] == 'Cocktails type 2'
    beer_catergory1_mask = df['Unnamed: 0'] == 'Beer type 1'
    beer_catergory2_mask = df['Unnamed: 0'] == 'Beer type 2'
    red_wine_mask = df['Unnamed: 0'] == 'Red Wine'
    white_wine_mask = df['Unnamed: 0'] == 'White Wine'
    totals_mask = df['Unnamed: 0'] == 'Total' 
    # Food item breakdowns
    # .iat[0,3] Retreieves the data at an index, 0,3 is the count. 0,6 is the sales total
    Burger_counts = df[burger_mask].iat[0,3]
    Burger_sales = df[burger_mask].iat[0,6]
    Main_menu_counts = df[main_menu_mask].iat[0,3]
    Main_menu_sales = df[main_menu_mask].iat[0,6]
    # Used to calc food sales
    sides_sales = df[sides_mask].iat[0,6]
    lunch_sales = df[lunch_mask].iat[0,6]
    misc_food_sales = df[misc_food_mask].iat[0,6]
    # Food, Net and Bar Sales
    Food_Sales = pd.to_numeric(Burger_sales + sides_sales + lunch_sales + misc_food_sales + Main_menu_sales)
    Net_sales = pd.to_numeric(df[totals_mask].iat[0,6])
    Bar_sales = Net_sales - Food_Sales
    # Bar Sales Catergoies breakdown (Sales/Counts)
    Cocktails_count = df[cocktail_catergory1_mask].iat[0,3]+df[cocktail_catergory2_mask].iat[0,3]
    Cocktails_sales = df[cocktail_catergory1_mask].iat[0,6]+df[cocktail_catergory2_mask].iat[0,6]
    # Beer
    Beer_count = df[beer_catergory1_mask].iat[0,3]+df[beer_catergory2_mask].iat[0,3]
    Beer_sales = df[beer_catergory1_mask].iat[0,6]+df[beer_catergory2_mask].iat[0,6]
    # Wine
    Wine_count = df[red_wine_mask].iat[0,3]+df[white_wine_mask].iat[0,3]
    Wine_sales = df[red_wine_mask].iat[0,6]+df[white_wine_mask].iat[0,6]
    
    #Retreive Cost of Goods Solds
    # .to_numeric casts the data type to a float. Oringial data type was stored as a string.
    df2 = pd.read_csv(base_path+'Receiving Data Folder/'+Month+' '+'2023 Receiving.csv')
    cogs_mask = df2['Category'] == 'Total' 
    COGS = pd.to_numeric(df2[cogs_mask].iat[0,4])
    Cog_percent = (round(COGS/Net_sales,4)*100)
    
    #Labour data
    df3 = pd.read_csv(base_path+'Payroll Data Folder/'+Month+' '+'2023 Payroll.csv')
    # Remove $, convert to int and then sum the total
    df3_clean = pd.to_numeric((df3['Paid.3'].map(lambda x: x.lstrip('$'))))
    Labour = df3_clean.sum()
    Labour_percent = (round(Labour/Net_sales,4)*100)
    
    Net_Profit = round(Net_sales - Labour - COGS,2)
    Profit_margin = round((1-(Labour/Net_sales)-(COGS/Net_sales))*100,2)
    
    return Month, Burger_counts, Burger_sales, Main_menu_counts, Main_menu_sales, Beer_count, Beer_sales, Cocktails_count, Cocktails_sales, Wine_count, Wine_sales, Food_Sales, Bar_sales, Net_sales, COGS, Cog_percent, Labour, Labour_percent, Net_Profit, Profit_margin

#Store the data extracted to be appended to the time-series
data = data_extraction('Month')

#Function to open and append the new data into the time-series
def update_timeseries(month,year,data):
    with open(base_path+'Timeseries Dataset.csv','a',encoding='UTF8') as f:
        writing = csv.writer(f)
        writing.writerow([year+'-'+month+'-'+'01',data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18],data[19]])

# Use once to create a new row before appending to the timerseires. 
with open(base_path+'Timeseries Dataset.csv','a',encoding='UTF8') as f:
        writing = csv.writer(f)
        writing.writerow(' ')
update_timeseries('01','2023',1st_variable)
