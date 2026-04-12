SELECT category, sum(sales) AS total_revenue
FROM orders
GROUP by category
order BY total_revenue DESC;