import seaborn as sns
import matplotlib.pyplot as plt

def analyze_data(df):
    print("\n📈 Basic Info:")
    print(df.info())

    print("\n📊 Summary Statistics:")
    print(df.describe())

    print("\n📌 Top 5 Books by Price:")
    print(df.sort_values(by='Price (£)', ascending=False).head())

    print("\n📚 Rating Distribution:")
    sns.countplot(data=df, x='Rating')
    plt.title("Book Rating Distribution")
    plt.show()

    print("\n💷 Price Distribution:")
    sns.histplot(df['Price (£)'], bins=20, kde=True)
    plt.title("Price Distribution of Books")
    plt.show()
