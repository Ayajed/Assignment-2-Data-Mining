import pandas as pd
import math

# Load data to Pandas dataframe
df = pd.read_excel('dataset.xlsx', sheet_name='sheet1')

# Check data anomalies
def check_anomalies(dataframe):
    for column in dataframe.columns:
        # Check missing datas
        if dataframe[column].isnull().sum() > 0:
            print("Anomalies found in column '{}': {} missing values".format(column, dataframe[column].isnull().sum()))
         # Check for data outliers
        if column == 'job':
            for job in dataframe['job'].unique():
                if dataframe[dataframe['job']==job].shape[0] < 5:
                    outliers = dataframe.loc[dataframe['job']==job]
                    print("Anomalies found in column '{}': Outlier job '{}'\n{}".format(column,job,outliers.to_string()))
        
check_anomalies(df)

# Solve anomalies
def solve_anomalies(dataframe):
    for column in dataframe.columns:
        # Fill missing datas with mean
        if column in ['age', 'salary']:
            for job in dataframe['job'].unique():
                mask = (dataframe['job'] == job) & (dataframe[column].isnull())
                mean = math.floor(dataframe.loc[dataframe['job'] == job][column].mean())
                dataframe.loc[mask, column] = mean
        # Remove outlier jobs
        for job in dataframe['job'].unique():
            if dataframe[dataframe['job']==job].shape[0] < 5:
                dataframe = dataframe[dataframe.job != job]
        
    return dataframe

df = solve_anomalies(df)

# Save to new file without numbering
df.to_excel('output.xlsx', index=False)