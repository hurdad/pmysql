SELECT City FROM Customers
UNION
SELECT City FROM Suppliers
ORDER BY City;