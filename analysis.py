import pandas as pd

# Load the dataset
df = pd.read_csv("data/titanic.csv")

print("=" * 50)
print("TITANIC DATASET ANALYSIS")
print("=" * 50)

# Total records
total_records = len(df)
print(f"Total Records: {total_records}")

# Survival rate
survival_rate = df["Survived"].mean() * 100
print(f"Survival Rate: {survival_rate:.2f}%")

# Average age
average_age = df["Age"].mean()
print(f"Average Age: {average_age:.2f} years")

# Class-wise distribution
print("\nPassenger Class Distribution:")
class_distribution = df["Pclass"].value_counts().sort_index()

for passenger_class, count in class_distribution.items():
    print(f"Class {passenger_class}: {count} passengers")