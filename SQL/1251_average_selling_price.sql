-- 1251 Average Selling Price 
SELECT Prices.product_id, COALESCE(ROUND(SUM(units*price)/SUM(units), 2), 0) AS average_price
FROM Prices
LEFT JOIN UnitsSold ON Prices.product_id = UnitsSold.product_id
AND purchase_date BETWEEN start_date AND end_date
GROUP BY product_id