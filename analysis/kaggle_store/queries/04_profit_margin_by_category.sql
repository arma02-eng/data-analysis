SELECT category,
	SUM(profit) as total_profit,
    SUM(sales) AS total_revenue,
    ROUND(SUM(profit) / SUM(sales) * 100, 2) AS profit_margin_pct
    
FROM orders
GROUP BY category
order BY profit_margin_pct DESC;