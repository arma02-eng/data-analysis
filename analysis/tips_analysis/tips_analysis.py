import pandas as pd

# Load data
df = pd.read_csv('../data/tips.csv')

# Total revenue per day
revenue_per_day = df.groupby('day')['total_bill'].sum()
print("Revenue Per Day:")
print(revenue_per_day)

# Average tips by gender
tip_by_gender = df.groupby('sex')['tip'].mean()
print("\nAverage Tips By Gender:")
print(tip_by_gender)

# Average tips by group size
tip_by_size = df.groupby('size')['tip'].mean()
print("Average Tips By Group Size:")
print(tip_by_size)