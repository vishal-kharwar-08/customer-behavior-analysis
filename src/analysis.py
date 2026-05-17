def analyze_data(df):
    print("\nTop 10 Customers by Revenue\n")

    customer_revenue = df.groupby('CustomerID')['TotalPrice'].sum().sort_values(ascending=False)

    print(customer_revenue.head(10))

    print("\nCountry Wise Revenue\n")

    country_revenue = df.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False)

    print(country_revenue.head(10))
