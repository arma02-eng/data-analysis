SELECT segment,
	printf('$%,.2f', SUM(sales)) As total_revenue,
    count (*) AS num_orders,
    printf('$%,.2f', SUM(sales) / count(*)) as avg_order_value
From orders
GROUP By segment
order BY avg_order_value DESC;