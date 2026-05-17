from src.preprocessing import load_and_clean_data
from src.analysis import analyze_data
from src.visualization import plot_sales_trend

def main():
    df = load_and_clean_data()
    analyze_data(df)
    plot_sales_trend(df)

if __name__ == "__main__":
    main()
