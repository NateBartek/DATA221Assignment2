# importing the pandas package
import pandas

# saving the crime csv file to crime_df
crime_df = pandas.read_csv("crime.csv")


# creating a new column in the crime_df dataframe named risk and saving lowCrime to it
crime_df["risk"] = "LowCrime"

# if ViolentCrimesPerPop was or equal to 0.5 then the risk would be changed to high crime
crime_df.loc[crime_df["ViolentCrimesPerPop"] >= 0.50, "risk"] = "High-Crime"

# calculating the average unemployment rate grouped by the risk and mean of the percent unemployed
average_unemployment = crime_df.groupby("risk")["PctUnemployed"].mean()

# print statements with rounding to the second decimals
print("Average unemployment rates by crime level:")
print("LowCrime:", round(average_unemployment["LowCrime"], 2))
print("High-Crime:", round(average_unemployment["High-Crime"], 2))
