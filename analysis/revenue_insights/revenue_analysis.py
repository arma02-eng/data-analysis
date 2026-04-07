# ======================================================
# Revenue Insights Analysis
# Project: Restaurant Tips Dataset
# Purpose:
#   Analyze revenue patterns and customer behavior
#   to generate business insights for staffing,
#   profitability, and customer trends.
# ======================================================

# --- Imports ---
# pandas: data manipulation
# matplotlib: visualization
# pathlib: safe file path handling (works from any directory)
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path



# ======================================================
# GLOBAL CHART STYLE (Professional Visualization Theme)
# ======================================================
# Apply a consistent visual style to all charts.
# This improves readability and creates portfolio-quality visuals.

plt.style.use("ggplot")   # clean professional theme

plt.rcParams.update({
    "figure.figsize": (8, 5),   # consistent chart size
    "axes.titlesize": 14,       # title font size
    "axes.labelsize": 12,       # axis label size
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "figure.dpi": 120           # sharper saved images
})


# ======================================================
# PROJECT PATH CONFIGURATION
# ======================================================
# This section defines important project directories.
# By centralizing paths here, the script becomes:
#    portable
#    reusable
#    safe to run from any location

# Location of this script file
SCRIPT_DIR = Path(__file__).resolve().parent

# Project root directory
# revenue_insights → analysis → project root
PROJECT_ROOT = SCRIPT_DIR.parents[1]

# Data directory (shared across analyses)
DATA_DIR = PROJECT_ROOT / "data"

# Output directory specific to THIS analysis
OUTPUT_DIR = SCRIPT_DIR / "charts"

# Create charts folder automatically if missing
OUTPUT_DIR.mkdir(exist_ok=True)


# ======================================================
# LOAD DATA
# ======================================================
# Build dataset path using centralized project paths
data_path = DATA_DIR / "tips.csv"

# Load dataset into pandas DataFrame
df = pd.read_csv(data_path)


# ======================================================
#  CREATE DERIVED METRICS (Feature Engineering)
# ======================================================
# These columns do not exist in the raw dataset.
# We create them to answer better business questions.

# Tip percentage per transaction
# Example: $4 tip on $20 bill = 0.20 (20%)
df["tip_pct"] = df["tip"] / df["total_bill"]

# Revenue generated per customer at a table
# Helps compare small vs large parties fairly
df["revenue_per_person"] = df["total_bill"] / df["size"]


# ======================================================
#  DATASET OVERVIEW
# ======================================================
# Quick validation step to confirm structure and data types
print("\n--- Dataset Info ---")
print(df.info())


# ======================================================
#  BUSINESS AGGREGATIONS
# ======================================================
# These groupby operations summarize the data
# to answer business-focused questions.

# Total revenue generated each day
print("\nRevenue By Day:")
print(df.groupby('day')['total_bill'].sum())

# Revenue comparison between Lunch and Dinner
print("\nRevenue By Time:")
print(df.groupby('time')['total_bill'].sum())

# Average bill size depending on party size
# (mean = average spending per table)
print("\nAverage Bill By Party Size:")
print(df.groupby('size')['total_bill'].mean())

# Average revenue per customer by day
# Shows efficiency rather than total volume
print("\nAverage Revenue Per Customer Per Day:")
print(df.groupby("day")["revenue_per_person"]
      .mean()
      .sort_values(ascending=False))

# Average tipping behavior during Lunch vs Dinner
print("\nAverage Tip % by Time:")
print(df.groupby("time")["tip_pct"].mean())

# Profitability efficiency by party size
print("\nRevenue Per Person By Party Size:")
print(df.groupby("size")["revenue_per_person"].mean())




# ======================================================
#  VISUALIZATION — TOTAL REVENUE BY DAY
# ======================================================
# Aggregate data for plotting
rev_day = df.groupby("day")["total_bill"].sum()

# Create bar chart
rev_day.plot(kind="bar")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Chart formatting
plt.title("Total Revenue by Day (Demand Patterns)")
plt.ylabel("Revenue")

# Prevent label overlap
plt.tight_layout()

# Save chart image to project-local charts folder
plt.savefig(OUTPUT_DIR / "revenue_by_day.png")

# Close figure to prevent memory buildup when adding more charts
plt.close()

# ======================================================
#  VISUALIZATION — TIP PERCENTAGE BY DAY
# ======================================================
# Business Question:
#   Do customers tip differently depending on the day?
# Insight Type:
#   Customer behavior analysis

# Calculate average tip percentage for each day
tip_pct_day = df.groupby("day")["tip_pct"].mean()

# Create bar chart
tip_pct_day.plot(kind="bar")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Chart formatting
plt.title("Average Tip Percentage by Day")
plt.ylabel("Average Tip %")

# Adjust layout spacing
plt.tight_layout()

# Save visualization
plt.savefig(OUTPUT_DIR / "tip_pct_by_day.png")

# Close figure to avoid overlap with next chart
plt.close()


# ======================================================
#  VISUALIZATION — REVENUE PER PERSON BY PARTY SIZE
# ======================================================
# Business Question:
#   Are larger tables actually more profitable per customer?
# Insight Type:
#   Efficiency and profitability analysis

# Compute average revenue generated per person for each party size
rev_per_person = df.groupby("size")["revenue_per_person"].mean()

# Create bar chart showing efficiency per customer
rev_per_person.plot(kind="bar")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Chart labels and formatting
plt.title("Revenue Per Person by Party Size (Efficiency Insight)")
plt.xlabel("Party Size")
plt.ylabel("Revenue Per Person")

# Prevent label overlap
plt.tight_layout()

# Save chart image
plt.savefig(OUTPUT_DIR / "revenue_per_person_by_size.png")

# Close plot
plt.close()


# ======================================================
#  VISUALIZATION — LUNCH VS DINNER REVENUE
# ======================================================
# Business Question:
#   When should staffing and operational resources
#   be prioritized during the day?
# Insight Type:
#   Operational decision support

# Calculate total revenue for Lunch vs Dinner
rev_time = df.groupby("time")["total_bill"].sum()

# Create comparison bar chart
rev_time.plot(kind="bar")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Chart formatting
plt.title("Total Revenue: Lunch vs Dinner (Operational Focus)")
plt.ylabel("Revenue")

# Improve spacing for exported image
plt.tight_layout()

# Save visualization
plt.savefig(OUTPUT_DIR / "revenue_by_time.png")

# Close figure
plt.close()

