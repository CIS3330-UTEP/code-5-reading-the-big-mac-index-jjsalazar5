import pandas as pd

# Load the CSV file
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)

# Check column names
df.columns = df.columns.str.strip()  # Remove extra spaces

# Ensure 'date' column exists and convert to 'year'
if "date" in df.columns:
    df["year"] = pd.to_datetime(df["date"]).dt.year
else:
    print("Error: 'date' column not found in CSV!")

def get_big_mac_price_by_year(year, country_code):
    """
    Get the mean Big Mac price in a specific year for a given country.
    """
    df_filtered = df[(df["year"] == year) & (df["iso_a3"].str.lower() == country_code)]
    mean_price = df_filtered["dollar_price"].mean()
    return round(mean_price, 2) if not df_filtered.empty else 0.0

def get_big_mac_price_by_country(country_code):
    """
    Get the mean Big Mac price for a given country.
    """
    df_filtered = df[df["iso_a3"].str.lower() == country_code]
    mean_price = df_filtered["dollar_price"].mean()
    return round(mean_price, 2) if not df_filtered.empty else 0.0

def get_the_cheapest_big_mac_price_by_year(year):
    """
    Get the country with the cheapest Big Mac price in a specific year.
    """
    df_filtered = df[df["year"] == year]
    if df_filtered.empty:
        return "No data available"

    min_row = df_filtered.loc[df_filtered["dollar_price"].idxmin()]
    return f"{min_row['name']}({min_row['iso_a3']}): ${min_row['dollar_price']:.2f}"

def get_the_most_expensive_big_mac_price_by_year(year):
    """
    Get the country with the most expensive Big Mac price in a specific year.
    """
    df_filtered = df[df["year"] == year]
    if df_filtered.empty:
        return "No data available"

    max_row = df_filtered.loc[df_filtered["dollar_price"].idxmax()]
    return f"{max_row['name']}({max_row['iso_a3']}): ${max_row['dollar_price']:.2f}"

if __name__ == "__main__": 
    print("Price in Malaysia (MYS) in 2008:", get_big_mac_price_by_year(2008, "mys")) 
    print("Average price in Malaysia (MYS) overall:", get_big_mac_price_by_country("mys")) 
    print("Cheapest Big Mac in 2008:", get_the_cheapest_big_mac_price_by_year(2008)) 
    print("Most expensive Big Mac in 2003:", get_the_most_expensive_big_mac_price_by_year(2003))  
