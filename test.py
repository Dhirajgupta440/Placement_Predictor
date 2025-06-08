import pandas as pd

# Load the CSV file
df = pd.read_csv("placement.csv")

# Drop a column by name, e.g., "unwanted_column"
df = df.drop(columns=["sn"])

# Save the updated DataFrame back to CSV (overwrite or save as new file)
df.to_csv("placement.csv", index=False)