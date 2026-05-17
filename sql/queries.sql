SELECT SUM(TotalPrice) AS TotalRevenue
FROM customer_data;

SELECT CustomerID, SUM(TotalPrice) AS Revenue
FROM customer_data
GROUP BY CustomerID
ORDER BY Revenue DESC
LIMIT 10;

SELECT Description, SUM(Quantity) AS TotalSold
FROM customer_data
GROUP BY Description
ORDER BY TotalSold DESC
LIMIT 10;

SELECT Country, SUM(TotalPrice) AS Revenue
FROM customer_data
GROUP BY Country
ORDER BY Revenue DESC;
