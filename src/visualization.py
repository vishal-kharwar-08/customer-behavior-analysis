import matplotlib.pyplot as plt

def plot_sales_trend(df):
    monthly_sales = df.groupby('Month')['TotalPrice'].sum()

    plt.figure(figsize=(10,5))
    plt.plot(monthly_sales.index, monthly_sales.values)

    plt.title('Monthly Sales Trend')
    plt.xlabel('Month')
    plt.ylabel('Revenue')
    plt.grid(True)

    plt.savefig('outputs/charts/monthly_sales_trend.png')

    print("Chart saved successfully!")
