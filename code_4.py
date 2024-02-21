import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

df = pd.read_csv(big_mac_file)
df['year'] = pd.DatetimeIndex(df['date']).year
    # Stack Overflow. (2024/02/21). “df['year'] = pd.DatetimeIndex(df['date']).year” Referenced using 
    # Stack Overflow. https://stackoverflow.com/questions/54110673/pandas-extracting-month-and-year-from-index

def get_big_mac_price_by_year(year,country_code):
    query = f"(iso_a3.str.lower() == '{country_code}') and (year == {year})"
    filter_df = df.query(query)
    mean_price_cy = filter_df['dollar_price'].mean()
    return round(mean_price_cy, 2)

def get_big_mac_price_by_country(country_code):
    query = f"(iso_a3.str.lower() == '{country_code}')"
    filter_df = df.query(query)
    mean_price_c = filter_df['dollar_price'].mean()
    return round(mean_price_c, 2)

def get_the_cheapest_big_mac_price_by_year(year):
    query = f"(year == {year})"
    filter_df = df.query(query)

    min_price_row = filter_df.loc[filter_df['dollar_price'].idxmin()]
    country_name = min_price_row['name']
    country_code = min_price_row['iso_a3']
    min_price = min_price_row['dollar_price']

    return f"{country_name}({country_code}): ${round(min_price, 2)}"

def get_the_most_expensive_big_mac_price_by_year(year):
    query = f"(year == {year})"
    filter_df = df.query(query)

    max_price_row = filter_df.loc[filter_df['dollar_price'].idxmax()]
    country_name = max_price_row['name']
    country_code = max_price_row['iso_a3']
    max_price = max_price_row['dollar_price']

    return f"{country_name}({country_code}): ${round(max_price, 2)}"

if __name__ == "__main__":
    result_a = get_big_mac_price_by_year(2010,"arg")
    print(result_a)
    result_b = get_big_mac_price_by_country("mex")
    print(result_b)
    result_c = get_the_cheapest_big_mac_price_by_year(2008)
    print(result_c)
    result_d = get_the_most_expensive_big_mac_price_by_year(2014)
    print(result_d)