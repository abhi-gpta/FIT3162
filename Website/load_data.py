def loaddata():
    from sqlalchemy import create_engine
    import pandas as pd
    import numpy as np

    # MySQL database configuration
    db_config = {
        "host": "fit3162.mysql.database.azure.com",
        "user": "fit3162",
        "password": "Consumercare123!",
        "database": "fit3162",
        "port": 3306
    }

    # Create a SQLAlchemy engine
    engine = create_engine(f"mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}")

    # Table name
    table_name = "cpi_data"

    # Query to retrieve the entire table
    query = f"SELECT * FROM {table_name}"

    # Read the table into a dataframe
    df = pd.read_sql(query, con=engine)
    df = df.replace({None: np.nan})
    df.to_csv('output.csv', index = False)
    
