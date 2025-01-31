import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

csv_file = r'C:/Users/mk1/Desktop/REM/data/CSV_data.csv'  
scatter_plot_file = r'C:/Users/mk1/Desktop/REM/results/scatter_plot.png'
histogram_file = r'C:/Users/mk1/Desktop/REM/results/histogram.png'

def analyze_elevation(csv_file, scatter_plot_file, histogram_file):
    df = pd.read_csv(csv_file)
    
    print("\nElevation statistics:")
    print(df["Z"].describe())

    plt.figure(figsize=(10, 6))
    plt.scatter(df["X"], df["Y"], c=df["Z"], cmap="viridis", s=10)
    plt.colorbar(label="Elevation (Z)")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.title("Geographic Coordinates and Elevation")
    plt.savefig(scatter_plot_file, dpi=300, bbox_inches='tight')
    print(f"Scatter plot saved as: {scatter_plot_file}")

    plt.figure(figsize=(10, 6))
    sns.histplot(df["Z"], bins=30, kde=True)
    plt.xlabel("Elevation (Z)")
    plt.ylabel("Frequency")
    plt.title("Elevation Distribution")
    plt.savefig(histogram_file, dpi=300, bbox_inches='tight')
    print(f"Histogram saved as: {histogram_file}")

    correlation_matrix = df.corr()
    print("\nCorrelation matrix:")
    print(correlation_matrix)

    high_elevation = df[df["Z"] > 300]
    print("\nPoints above 300m:")
    print(high_elevation.head())

if __name__ == "__main__":
    analyze_elevation(csv_file, scatter_plot_file, histogram_file)
