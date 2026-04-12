SELECT "customer_name", SUM(sales) as total_spent
FROM orders
GROUP BY "customer_name"
order By total_spent DESC
LIMIT 5;customer_name