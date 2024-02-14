import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)

# print(df)
# print(df.columns)
# print(type(df.columns))
# print(len(df.columns))

# print(len(df))
# print(df.index)
# print(type(df.index))

# for i in df.index:
#     # print(i)
#     # print(df['dollar_price'][i])
#     # print(df.loc[i]['name'])
#     print(type(df.iloc[i]))

# df_mex = df.query("iso_a3" == "MEX'")
# for i in range(len(df_mex)):
#     print(df_mex.loc[df_mex.index[i]])

# for index, row in df.interrows():
#     print(row['name'])
#     print(df['name'][index])

# def get_new_country_name(row):
    # print(row)
    # new_column_value = f"{row["name"]}({row["iso_a3"]})"
    # print(new_column_value)
    # return new_column_value

# print(df.apply(get_new_name, axis=1))
# df["new name"] = df.apply(get_new_name, axis=1)
# print(df)