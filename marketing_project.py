import pandas as pd

df = pd.read_csv("marketing_campaign_dataset.csv")

print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

print(
    df.groupby("Channel_Used")["ROI"].mean()
      .sort_values(ascending=False)
)

print(
    df.groupby("Customer_Segment")["ROI"]
      .mean()
      .sort_values(ascending=False)
)

print(
    df.groupby("Campaign_Type")["ROI"]
      .mean()
      .sort_values(ascending=False)
)

print(
    df.groupby("Channel_Used")["Clicks"]
      .mean()
      .sort_values(ascending=False)
)

print(
    df.groupby("Campaign_Type")["Conversion_Rate"]
      .mean()
      .sort_values(ascending=False)
)

print(
    df.groupby("Location")["ROI"]
      .mean()
      .sort_values(ascending=False)
)

print(df[["Clicks", "Conversion_Rate"]].corr())

print(df[["Impressions", "Clicks"]].corr())

print(df.groupby("Channel_Used")["Conversion_Rate"]
        .mean()
        .sort_values(ascending=False))

print(df[["ROI","Conversion_Rate","Clicks","Impressions"]].describe())

df["CTR"] = df["Clicks"] / df["Impressions"]    *100

print(df[["CTR"]].describe())

print(
    df.groupby("Company")["ROI"]
      .mean()
      .sort_values(ascending=False)
      .head(10)
)

df["Date"] = pd.to_datetime(df["Date"])

df["Year"] = df["Date"].dt.year

print(
    df.groupby("Year")["ROI"]
      .mean()
)

import matplotlib.pyplot as plt

df.groupby("Channel_Used")["ROI"]\
  .mean()\
  .sort_values()\
  .plot(kind="bar")

plt.title("Average ROI by Channel")

plt.savefig("roi_by_channel.png")
plt.show()

df.to_csv("marketing_analysis_final.csv", index=False)