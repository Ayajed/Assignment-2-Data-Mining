import pandas as pd
import math

# Load data ke Pandas dataframe
df = pd.read_excel('dataset.xlsx', sheet_name='contoh')

# Cek data anomalies
def check_anomalies(dataframe):
    for column in dataframe.columns:
        # Check for missing values
        if dataframe[column].isnull().sum() > 0:
            print("Anomalies found in column '{}': {} missing values".format(column, dataframe[column].isnull().sum()))

check_anomalies(df)

# Solve anomalies
def solve_anomalies(dataframe):
    for column in dataframe.columns:
        # Isi missing data di kolom age & salary dengan mean
        if column in ['age', 'salary']:
            for job in dataframe['job'].unique():
                mask = (dataframe['job'] == job) & (dataframe[column].isnull())
                mean = math.floor(dataframe.loc[dataframe['job'] == job][column].mean())
                dataframe.loc[mask, column] = mean
    return dataframe

df = solve_anomalies(df)

# Output jadi file baru tanpa indexing
df.to_excel('output.xlsx', index=False)