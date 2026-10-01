SELECT product, SUM(revenue) AS total_revenue
FROM sales
GROUP BY product
ORDER BY total_revenue DESC;

SELECT region, SUM(revenue)
FROM sales
GROUP BY region;

