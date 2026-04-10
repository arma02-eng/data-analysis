# Revenue Insights Analysis — Restaurant Tips Dataset

## Objective

Analyze restaurant transaction data to understand revenue patterns, customer behavior, and operational insights that could help improve staffing and business decisions.

---

## Dataset

The dataset contains 244 restaurant transactions including:

* Total bill amount
* Tip amount
* Customer gender
* Smoking status
* Day of visit
* Meal time (Lunch/Dinner)
* Party size

---

## Key Metrics Created

To better evaluate performance, additional metrics were derived:

* **Tip Percentage** = tip / total_bill
* **Revenue per Person** = total_bill / party size

These metrics allow comparison of customer value rather than raw totals.

---

## Key Findings

### 1. Revenue by Day

Saturday generated $1778.40 total revenue, 1,452.52 more than Friday, indicating peak demand during weekends.

**Business implication:**
More staff and inventory should be allocated For Saturdays and Sundays, its the highest volume of revenue per day.

---

### 2. Lunch vs Dinner Performance

Dinner service produces significantly higher total revenue than lunch by a margin of almost 3 times $3,660.30 vs $1,167.47.

**Insight:**
Higher earnings are driven mainly by customer volume rather than higher spending per person.

---

### 3. Customer Spending Behavior

 Parties of 2 generate $8.22 per person, Parties of 6 only $5.81.

**Implication:**
Smaller parties spend more per customer than larger parties they should be prioritized through ensure good customer service for repeated visits and consistent spending.

---

### 4. Revenue Efficiency

Revenue per person varies across days, suggesting some days attract higher-value customers rather than just higher traffic.


Saturday had the highest revenue per customer per day, followed by friday, sunday, thursday

|Day    | Revenue Per Person|
|-------|-------------------|
|Sat    | 8.18              |
|Fri    | 8.13              |
|Sun    | 7.86              |
|Thur   | 7.42              |
---

### 5. Tipping Patterns

Average tip percentage differs between meal times, indicating behavioral differences in customer tipping habits.

Lunch 16.4%, 
Dinner 15.9%.

**Implication:**
Business hours draw better tipping behavior from customers(business lunches, office workers and other mid day customers) over weekends where they might be casual dinners 

---

## Visualizations

Charts generated during analysis:

* Revenue by day
* Tips by gender
* Tips by party size

All visual outputs are stored locally within the project.

---

## Tools Used

* Python
* Pandas
* Matplotlib

---

## Conclusion

The analysis shows that restaurant revenue is primarily influenced by timing and customer volume rather than party size alone. Dinner service and weekend operations represent the strongest opportunities for revenue optimization through staffing and operational planning.

---

## Future Improvements

* Add time-series trend analysis
* Compare smoker vs non-smoker spending behavior
* Build predictive model for expected revenue
