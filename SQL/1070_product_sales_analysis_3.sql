# 1070 Product Sales Analysis 3
SELECT s.product_id, s.year AS first_year, s.quantity, s.price
FROM Sales s
INNER JOIN ( 
    SELECT product_id, MIN(year) AS min_year
    FROM Sales
    GROUP BY product_id) AS first_sales_year
ON s.product_id = first_sales_year.product_id AND s.year = first_sales_year.min_year
