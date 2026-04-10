
#Imports

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# Global Chart Style
plt.style.use("ggplot")
plt.rcParams.update({
    "figure.figsize": (8,5),
    "axes.titlesize": 14,
    "axes.labelsize": 12,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "figure.dpi": 120


})



# Load data

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_DIR / "data"
OUTPUT_DIR = SCRIPT_DIR / "charts"
OUTPUT_DIR.mkdir(exist_ok=True)
df = pd.read_csv(DATA_DIR / "tips.csv")


# Revenue per day
revenue_per_day = df.groupby('day')['total_bill'].sum()

# Plot revenue per day
revenue_per_day.plot(kind='bar', title='Revenue per Day')
plt.xlabel('Day')
plt.ylabel('Total Revenue')
plt.savefig(OUTPUT_DIR /'revenue_per_day.png')
plt.close()

# Average tip by gender
tip_by_gender = df.groupby('sex')['tip'].mean()

tip_by_gender.plot(kind='bar', title='Average Tip by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Tip')
plt.savefig(OUTPUT_DIR / 'tips_by_gender.png')
plt.close()

# Average tip by group size
tip_by_size = df.groupby('size')['tip'].mean()

tip_by_size.plot(kind='line', marker='o', title='Average Tip by Group Size')
plt.xlabel('Group Size')
plt.ylabel('Average Tip')
plt.savefig(OUTPUT_DIR / 'tips_by_size.png')
plt.close()