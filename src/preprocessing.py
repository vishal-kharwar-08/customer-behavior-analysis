import pandas as pd

def load_and_clean_data():
    file_path = 'data/raw/customer_data.csv'

    df = pd.read_csv(file_path)

    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)

    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

    df['Month'] = df['InvoiceDate'].dt.month
    df['Year'] = df['InvoiceDate'].dt.year

    df.to_csv('data/processed/cleaned_data.csv', index=False)

    print("Data cleaned successfully!")

    return df
