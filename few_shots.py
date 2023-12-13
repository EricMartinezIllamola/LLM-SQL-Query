few_shots = [
    {"Question" : "Which were the most demanded products in 2022?",
    "SQLQuery" : "SELECT p.ProductID, p.Brand, p.Category, SUM(oi.Quantity) AS Demand FROM Products p JOIN OrderItems oi ON p.ProductID = oi.ProductID JOIN Orders o ON oi.OrderID = o.OrderID WHERE o.OrderDate BETWEEN '2022-01-01' AND '2022-12-31' GROUP BY p.ProductID, p.Brand, p.Category ORDER BY Demand DESC LIMIT 5"},
    {"Question" : "Which types of RAM saw the higher number of sales?",
    "SQLQuery" : "SELECT p.RAM, SUM(oi.Quantity) AS SalesNumber FROM Products p JOIN OrderItems oi ON p.ProductID = oi.ProductID JOIN Orders o ON oi.OrderID = o.OrderID GROUP BY p.RAM ORDER BY TotalSales DESC LIMIT 5"},
    {"Question" : "What is the total value of all the products in stock?",
    "SQLQuery" : "SELECT SUM(Price * QuantityInStock) AS TotalValue  FROM Products"},
    {"Question" : "Identify the three vendors that sold more products.",
    "SQLQuery" : "SELECT v.VendorID, v.VendorName, SUM(oi.Quantity) AS TotalProductsSold FROM Vendors v JOIN Orders o ON v.VendorID = o.VendorID JOIN OrderItems oi ON o.OrderID = oi.OrderID GROUP BY v.VendorID, v.VendorName ORDER BY TotalProductsSold DESC LIMIT 3"},
    {"Question" : "Identify the customers who have placed orders for both desktops and laptops, along with the total amount spent by each customer.",
    "SQLQuery" : "SELECT c.CustomerID, c.StoreName, SUM(o.TotalOrderPrice) AS TotalAmountSpentFROM Customers AS cJOIN Orders AS o ON c.CustomerID = o.CustomerIDJOIN OrderItems AS oi ON o.OrderID = oi.OrderIDJOIN Products AS p ON oi.ProductID = p.ProductIDWHERE p.Category IN ('Desktop', 'Laptop')GROUP BY c.CustomerID, c.StoreNameORDER BY TotalAmountSpent DESC"},
    {"Question" : "List the products with the highest price in each category.",
    "SQLQuery" : "SELECT p.Category, p.ProductID, p.Price FROM Products AS p GROUP BY p.Category, p.ProductID ORDER BY p.Price DESC"},
    {"Question" : "Retrieve the top 3 vendors with the highest total salaries.",
    "SQLQuery" : "SELECT VendorName, SUM(Salary) AS TotalSalary FROM Vendors GROUP BY VendorName ORDER BY TotalSalary DESC LIMIT 3"},
    {"Question" : "Identify the top three customers who have placed the most orders in the last six months, along with the total amount spent by each customer.",
    "SQLQuery" : "SELECT c.CustomerID, c.StoreName, COUNT(DISTINCT o.OrderID) AS TotalOrders, SUM(o.TotalOrderPrice) AS TotalAmountSpent FROM Customers AS c JOIN Orders AS o ON c.CustomerID = o.CustomerID WHERE o.OrderDate BETWEEN date('now', '-6 months') AND date('now') GROUP BY c.CustomerID, c.StoreName ORDER BY TotalOrders DESC LIMIT 3"},
]

# extra_few_shots = [
#     {"Question" : "",
#     "SQLQuery" : ""},
#     {"Question" : "",
#     "SQLQuery" : ""},
#     {"Question" : "",
#     "SQLQuery" : ""},
#     {"Question" : "",
#     "SQLQuery" : ""},
# ]