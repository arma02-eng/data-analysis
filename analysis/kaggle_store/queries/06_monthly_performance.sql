SELECT substr(order_date, 1, 2) as month,
	printf('$%,.2f', SUM(sales)) AS total_revenue,
    COUNT(*) AS num_orders
    
FROM orders
GROUP By month
order By SUM(sales) DESC;