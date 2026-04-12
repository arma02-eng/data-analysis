SELECT "product_name",
	category,
	sub_category,
	printf('$%,.2f', SUM(sales)) AS total_sales,
    printf('$%,.2f', SUM(profit)) as total_loss
FROM orders
GROUP BY "product_name" , "sub_category"
HAVING SUM(profit) < 0
order BY total_loss ASC
LIMIT 10;