import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)
df['year'] = pd.to_datetime(df['date']).dt.year

def get_big_mac_price_by_year(year, country_code):
    #Get the mean Big Mac price in a specific year for a given country.
    df_filtered = df[(df["year"] == year) & (df["iso_a3"].str.lower() == country_code)]
    mean_price = df_filtered["dollar_price"].mean()
    return round(mean_price, 2)

def get_big_mac_price_by_country(country_code):
    #Get the mean Big Mac price for a given country.
    df_filtered = df[df["iso_a3"] == country_code.upper()]
    mean_price = df_filtered["dollar_price"].mean()
    return round(mean_price, 2)

def get_the_cheapest_big_mac_price_by_year(year):
    #Get the country with the cheapest Big Mac price in a specific year.
    df_filtered = df[df["year"] == year]
    min_row = df_filtered.loc[df_filtered["dollar_price"].idxmin()]

    country_name = min_row["name"]
    country_code = min_row["iso_a3"]
    dollar_price = min_row["dollar_price"]
    return f"{country_name}({country_code}): $(dollar_price:.2f)"

def get_the_most_expensive_big_mac_price_by_year(year):
    #Get the country with the most expensive Big Mac price in a specific year.
    df_filtered = df[df["year"] == year]
    max_row = df_filtered.loc[df_filtered["dollar_price"].idxmax()]

    country_name = max_row["name"]
    country_code = max_row["iso_a3"]
    dollar_price = max_row["dollar_price"]
    return f"{country_name}({country_code}): $(dollar_price:.2f)"  

if __name__ == "__main__": 
    print("Price in Malaysia (MYS) in 2008:", get_big_mac_price_by_year(2008, "mys")) 
    print("Average price in Malaysia (MYS) overall:", get_big_mac_price_by_country("mys")) 
    print("Cheapest Big Mac in 2008:", get_the_cheapest_big_mac_price_by_year(2008)) 
    print("Most expensive Big Mac in 2003:", get_the_most_expensive_big_mac_price_by_year(2003))
