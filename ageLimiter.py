import pandas as pd

# Load the CSV file
file_path = "./original_stroke_risk_dataset.csv"
df = pd.read_csv(file_path)

# Convert age to 1 if > 40, else 0
df["Age greater than 50"] = df["Age"].apply(lambda x: 1 if x >= 50 else 0)

# Save the modified dataset
df.to_csv("updated_stroke_risk_dataset.csv", index=False)

print("Conversion complete! The updated dataset is saved as 'updated_stroke_risk_dataset.csv'.")
