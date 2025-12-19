import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/patients.csv")

# Convert dates
df["admission_date"] = pd.to_datetime(df["admission_date"])
df["discharge_date"] = pd.to_datetime(df["discharge_date"])

# Length of stay
df["stay_days"] = (df["discharge_date"] - df["admission_date"]).dt.days

print("\n--- Dataset Overview ---")
print(df.head())

# 1. Average bill amount
avg_bill = df["bill_amount"].mean()
print(f"\nAverage Bill Amount: Rs.{avg_bill:.2f}")

# 2. Patients count by disease
disease_count = df["disease"].value_counts()
print("\nPatients by Disease:")
print(disease_count)

# 3. Average stay by disease
avg_stay = df.groupby("disease")["stay_days"].mean()
print("\nAverage Stay Days by Disease:")
print(avg_stay)

# 4. Gender wise billing
gender_bill = df.groupby("gender")["bill_amount"].sum()
print("\nTotal Bill Amount by Gender:")
print(gender_bill)

# 5. Highest bill patient
highest_bill = df.loc[df["bill_amount"].idxmax()]
print("\nHighest Bill Patient:")
print(highest_bill)

# -----------------------
# Matplotlib Charts
# -----------------------

# Chart 1: Patients by Disease
plt.figure(figsize=(6,4))
disease_count.plot(kind='bar', color='skyblue')
plt.title('Patients by Disease')
plt.xlabel('Disease')
plt.ylabel('Number of Patients')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Chart 2: Average Stay Days by Disease
plt.figure(figsize=(6,4))
avg_stay.plot(kind='bar', color='lightgreen')
plt.title('Average Stay Days by Disease')
plt.xlabel('Disease')
plt.ylabel('Average Stay Days')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Chart 3: Total Bill Amount by Gender
plt.figure(figsize=(6,4))
gender_bill.plot(kind='pie', autopct='%1.1f%%', colors=['pink','lightblue'])
plt.title('Total Bill Amount by Gender')
plt.ylabel('')
plt.show()