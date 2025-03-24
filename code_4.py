import pandas as pd

big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)

df.columns = df.columns.str.strip()  

if "date" in df.columns:
    df["year"] = pd.to_datetime(df["date"]).dt.year # Written with the help of AI
else:
    print("Error: 'date' column not found in CSV!") # Written with the help of AI

def get_big_mac_price_by_year(year, country_code):
    df_filtered = df[(df["year"] == year) & (df["iso_a3"].str.lower() == country_code)] # Written with the help of AI
    mean_price = df_filtered["dollar_price"].mean()
    return round(mean_price, 2) if not df_filtered.empty else 0.0 # Written with the help of AI

def get_big_mac_price_by_country(country_code):
    df_filtered = df[df["iso_a3"].str.lower() == country_code]
    mean_price = df_filtered["dollar_price"].mean()
    return round(mean_price, 2) if not df_filtered.empty else 0.0 # Written with the help of AI

def get_the_cheapest_big_mac_price_by_year(year):
    
    df_filtered = df[df["year"] == year]
    if df_filtered.empty:
        return "No data available"

    min_row = df_filtered.loc[df_filtered["dollar_price"].idxmin()] # Written with the help of AI
    return f"{min_row['name']}({min_row['iso_a3']}): ${format(min_row['dollar_price'], '.2f')}" # Written with the help of AI

def get_the_most_expensive_big_mac_price_by_year(year):
    df_filtered = df[df["year"] == year]
    if df_filtered.empty:
        return "No data available"

    max_row = df_filtered.loc[df_filtered["dollar_price"].idxmax()] # Written with the help of AI
    return f"{max_row['name']}({max_row['iso_a3']}): ${format(max_row['dollar_price'], '.2f')}" # Written with the help of AI

if __name__ == "__main__": 
    print("Price in Malaysia (MYS) in 2008:", get_big_mac_price_by_year(2008, "mys"))  # Written with the help of AI
    print("Average price in Malaysia (MYS) overall:", get_big_mac_price_by_country("mys"))  # Written with the help of AI
    print("Cheapest Big Mac in 2008:", get_the_cheapest_big_mac_price_by_year(2008))  # Written with the help of AI
    print("Most expensive Big Mac in 2003:", get_the_most_expensive_big_mac_price_by_year(2003))  # Written with the help of AI

# Chat-GPT(4). (2025/03/02). “Walk me through writing a code that extracts infromation from a CSV file using Pandas.” Generated using OpenAI Chat-GPT. https://chat.openai.com/ 


