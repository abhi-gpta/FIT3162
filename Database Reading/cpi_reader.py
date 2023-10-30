def main(file_path, upload = 1):
   
    categories = ['Lamb and goat',
                'Wine',
                'Food additives and condiments',
                'Other meats',
                'Garments for men',
                'Cheese',
                'Garments',
                'Bread',
                'Fruit',
                'Footwear for men',
                'Ice cream and other dairy products',
                'Meals out and take away foods',
                'Poultry',
                'Restaurant meals',
                'Glassware, tableware and household utensils',
                'Garments for women',
                'Other non-durable household products',
                'Beer',
                'Eggs',
                'Oils and fats',
                'Waters, soft drinks and juices',
                'Other food products n.e.c.',
                'Food products n.e.c.',
                'Footwear for women',
                'Meat and seafoods',
                'Snacks and confectionery',
                'Beef and veal',
                'Take away and fast foods',
                'Other cereal products',
                'Cakes and biscuits',
                'Coffee, tea and cocoa',
                'Jams, honey and spreads',
                'Books',
                'Dairy and related products',
                'Tobacco',
                'Alcohol and tobacco',
                'Pork',
                'Garments for infants and children',
                'Clothing and footwear',
                'Bread and cereal products',
                'Personal care products',
                'Breakfast cereals',
                'Fish and other seafood',
                'Non-alcoholic beverages',
                'Spirits',
                'Non-durable household products',
                'Footwear for infants and children',
                'Cleaning and maintenance products',
                'Newspapers, books and stationery',
                'Milk',
                'Household appliances, utensils and tools',
                'Newspapers, magazines and stationery',
                'Vegetables',
                'Footwear',
                'Alcoholic beverages',
                'Fruit and vegetables',
                'Furniture']

    xls = pd.ExcelFile(file_path)
    sheet_names = xls.sheet_names[2:-1]  # skip the first 2 sheets and the last one
    sheet_1 = pd.read_excel(xls, xls.sheet_names[0],header=None)
    #check that it is the right file
    cell_value = sheet_1.iat[5, 1]
    
    # Specify the expected value
    expected_value = "TABLE 9. CPI: Group, Sub-group and Expenditure Class, Index Numbers by Capital City"
    print(cell_value)
    assert cell_value == expected_value, "Table is not of the accepted format"
  
    # Add first sheet manually
    combined_df = pd.read_excel(xls, xls.sheet_names[1])
    # Read each sheet and concatenate it horizontally to the combined DataFrame
    for sheet_name in sheet_names:
        sheet_df = pd.read_excel(xls, sheet_name)
        sheet_df = sheet_df.drop(sheet_df.columns[0], axis=1)
        combined_df = pd.concat([combined_df, sheet_df], axis=1)

    combined_df.iloc[0] = combined_df.columns
    combined_df = combined_df.drop([2,3,4,5,6,7,8], axis=0)

    header_row = combined_df.iloc[0]

    # Split the first row into three separate values using ';'
    new_header = header_row.str.split(';').tolist()
    new_header[0] = ['Date', np.NaN, np.NaN]
    for i in range(1,len(new_header)):
        new_header[i] = new_header[i][1:3]
        for j in range(2):
            new_header[i][j] = new_header[i][j].strip()
    new_header = list(map(list, zip(*new_header)))
    new_header = pd.DataFrame(new_header)
    new_header = new_header.reset_index(drop=True)

    # Create a new DataFrame with the split values as the first row
    combined_df = combined_df.drop([0,1],axis=0)
    combined_df = combined_df.reset_index(drop=True)
    combined_df.columns = new_header.columns
    combined_df = pd.concat([new_header, combined_df], axis=0, ignore_index=True)
    combined_df.columns = combined_df.iloc[0]
    combined_df=combined_df.drop([0], axis = 0)

    filtered_df = combined_df[categories + ["Date"]]
    filtered_df['Date'] = pd.to_datetime(filtered_df['Date'])
    cols = ['Date'] + [col for col in filtered_df if col != 'Date']
    filtered_df = filtered_df[cols]

    transposed_df = filtered_df.T
    transposed_df = transposed_df.reset_index()
    dates = list(transposed_df.iloc[0][2:])
    transposed_df.columns = ['Product','City'] + dates
    transposed_df = transposed_df.drop([0])

    df_melted = transposed_df.melt(id_vars=['Product', 'City'], 
                        value_vars=dates,
                        var_name='Date', value_name='Index Value')

   # df_melted["% Change"] = df_melted['Index Value'].pct_change() * 100
    df_melted.to_csv('output.csv')
    if upload:
        upload_to_database(df_melted)
    return
    

def upload_to_database(df):
    db_config = {
        "host": "fit3162.mysql.database.azure.com",
        "user": "fit3162",
        "password": "Consumercare123!",
        "database": "fit3162",
        "port": 3306
    }

    # Create a SQLAlchemy engine
    engine = create_engine(f"mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}")

    # Get the table name
    table_name = 'cpi_data'

    # Create the table based on the dataframe structure
    df.head(0).to_sql(name=table_name, con=engine, if_exists='replace', index=False)

    # Insert the dataframe records into the table (replace if it exists)
    df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)


if __name__ == "__main__":
    import pandas as pd
    import numpy as np
    from sqlalchemy import create_engine
    import sys
    import os
    arguments = sys.argv
    file_path = arguments[1]
    upload = int(arguments[2])
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file or directory '{file_path}' does not exist.")
    
    file_extension = os.path.splitext(file_path)[1].lower()
    excel_extensions = ['.xls', '.xlsx', '.xlsm']
    if file_extension not in excel_extensions:
        raise ValueError(f"The file '{file_path}' is not an Excel file (supported extensions: {', '.join(excel_extensions)}).")
    
    print(f"File {file_path} was found")
    main(file_path, upload)