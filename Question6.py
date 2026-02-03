import pandas

crime_df = pandas.read_csv("crime.csv")

crime_df["risk"] = "LowCrime"
crime_df.loc[crime_df["ViolentCrimesPerPop"] >= 0.50, "risk"] = "High-Crime"

average_unemployment = crime_df.groupby("risk")["PctUnemployed"].mean()


print("Average unemployment rates by crime level:")
print("LowCrime:", round(average_unemployment["LowCrime"], 2))
print("High-Crime:", round(average_unemployment["High-Crime"], 2))
