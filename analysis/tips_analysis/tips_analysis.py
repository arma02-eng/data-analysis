import pandas as pd
import matplotlib.pyplot as plt

# Load data
pd.read_csv('../../data/tips.csv')

# Revenue per day
revenue_per_day = df.groupby('day')['total_bill'].sum()

# Plot revenue per day
revenue_per_day.plot(kind='bar', title='Revenue per Day')
plt.xlabel('Day')
plt.ylabel('Total Revenue')
plt.savefig('revenue_per_day.png')
plt.close()

# Average tip by gender
tip_by_gender = df.groupby('sex')['tip'].mean()

tip_by_gender.plot(kind='bar', title='Average Tip by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Tip')
plt.savefig('tips_by_gender.png')
plt.close()

# Average tip by group size
tip_by_size = df.groupby('size')['tip'].mean()

tip_by_size.plot(kind='line', marker='o', title='Average Tip by Group Size')
plt.xlabel('Group Size')
plt.ylabel('Average Tip')
plt.savefig('tips_by_size.png')
plt.close()