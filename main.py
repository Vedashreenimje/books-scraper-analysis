from google.colab import files

def main():
    print("🔍 Scraping book data...")
    base_url = "https://books.toscrape.com"
    df = scrape_books(base_url, pages=5)

    print("✅ Data scraped. Here's a preview:")
    print(df.head())

    # 💾 Save as CSV
    df.to_csv("books.csv", index=False)
    print("\n📁 CSV file 'books.csv' has been created.")

    print("\n📊 Analyzing data...")
    analyze_data(df)

    # 📥 Download the CSV file
    files.download("books.csv")

main()
