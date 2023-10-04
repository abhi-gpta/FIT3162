def regress(product):
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    import sklearn
    import xgboost as xgb
    from sklearn.metrics import mean_squared_error
    from sklearn.linear_model import LinearRegression
    color_pal = sns.color_palette()
    import os.path

    plt.style.use('bmh')
    
    if os.path.isfile('output.csv'): 
        df = pd.read_csv('output.csv')
    else:
        from load_data import loaddata
        loaddata()
        df = pd.read_csv('output.csv')
    
    df = df[df['Product'] == product]
    df = df.groupby(['Date'])['Index Value'].mean().reset_index()
    df = df.sort_values(by='Date')
    df = df.set_index('Date')
    df.index = pd.to_datetime(df.index)
    df = df[df['Index Value'].notna()]
    
    train = df.loc[df.index < '01-01-2016']
    test = df.loc[df.index >= '01-01-2016']
    
    last_date = test.index[-1]
    for i in range(10):
        for j in range(4):
            last_date += pd.DateOffset(months=3)
            test.loc[last_date] = np.NaN
    
    def create_features(df):
        df = df.copy()
        df['quarter'] = df.index.quarter
        df['year'] = df.index.year
        df1 = pd.get_dummies(df, columns=['quarter'], prefix=['quarter'])
        df1['quarter'] = df.index.quarter
        return df1
    df = create_features(df)

    train = create_features(train)
    test = create_features(test)

    FEATURES = ['year', 'quarter_1','quarter_2','quarter_3','quarter_4']	
    TARGET = 'Index Value'

    X_train = train[FEATURES]
    y_train = train[TARGET]

    X_test = test[FEATURES]
    y_test = test[TARGET]
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    test['prediction'] = model.predict(X_test)
    df = df.merge(test[['prediction']], how='outer', left_index=True, right_index=True)
    plt.tight_layout()

    ax = df[['Index Value']].plot(figsize=(15, 5))
    ax.set_ylabel('Index Points')
    df['prediction'].plot(ax=ax, style='-')
    plt.legend(['Real Data', 'Predictions'])
    ax.set_title('Forecasted Relative Price for: ' + product)
    plt.savefig('static/plot.png', bbox_inches='tight', format='png')
    plt.close()
