import pandas as pd

df = pd.read_csv('housing.csv')

print(df.info())

df.total_bedrooms = df.total_bedrooms.fillna(-999)
print(df.info())

print(df.columns)

features = [f for f in df.columns]
df_original = df.copy()
for col in features:
    df.loc[:, col] = df[col].astype(str).fillna("NONE")
print(df.info())
features = []
for f in df.columns:
    features.append(f)
print(features)

df2 = df.drop(["ocean_proximity"], axis="columns")
print(df2.info())

print("Type is ", type(df_original["housing_median_age"].values[2]))
df_original["housing_median_age"] = df_original[df_original["housing_median_age"]>30]
print(df_original["housing_median_age"])

import matplotlib.pyplot as plt
df.housing_median_age.hist()
plt.show()
