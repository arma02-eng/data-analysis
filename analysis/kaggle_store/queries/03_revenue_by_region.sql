SELECT region, SUM(sales) As total_revenue, count(*) as num_orders
FROM orders
GROUP BY region
order by total_revenue DESC;
