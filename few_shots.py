few_shots = [
    {"Question" : "Which were the most demanded products in 2022?",
    "SQLQuery" : "SELECT p.ProductID, p.Brand, p.Category, COUNT(oi.OrderItemID) AS Demand \nFROM Products p \nJOIN OrderItems oi ON p.ProductID = oi.ProductID \nJOIN Orders o ON oi.OrderID = o.OrderID \nWHERE o.OrderDate BETWEEN '2022-01-01' AND '2022-12-31' \nGROUP BY p.ProductID, p.Brand, p.Category \nORDER BY Demand DESC LIMIT 5"},
    {"Question" : "Which types of RAM saw the higher sales?",
    "SQLQuery" : "SELECT p.RAM, SUM(oi.Quantity) AS TotalSales \nFROM Products p \nJOIN OrderItems oi ON p.ProductID = oi.ProductID \nJOIN Orders o ON oi.OrderID = o.OrderID GROUP BY p.RAM ORDER BY TotalSales DESC LIMIT 5"},
    {"Question" : "What is the total value of all the products in stock?",
     "SQLQuery" : "SELECT SUM(Price * QuantityInStock) AS TotalValue \n FROM Products"},
    {"Question" : "Identify the three vendors that sold more products.",
    "SQLQuery" : "SELECT v.VendorID, v.VendorName, COUNT(oi.ProductID) AS TotalProductsSold \nFROM Vendors v \nJOIN Orders o ON v.VendorID = o.VendorID \nJOIN OrderItems oi ON o.OrderID = oi.OrderID \nGROUP BY v.VendorID, v.VendorName \nORDER BY TotalProductsSold DESC LIMIT 3"},
    {"Question" : "Identify the customers who have placed orders for both desktops and laptops, along with the total amount spent by each customer.",
    "SQLQuery" : "SELECT c.CustomerID, c.StoreName, SUM(o.TotalOrderPrice) AS TotalAmountSpent\nFROM Customers AS c\nJOIN Orders AS o ON c.CustomerID = o.CustomerID\nJOIN OrderItems AS oi ON o.OrderID = oi.OrderID\nJOIN Products AS p ON oi.ProductID = p.ProductID\nWHERE p.Category IN ('Desktop', 'Laptop')\nGROUP BY c.CustomerID, c.StoreName\nORDER BY TotalAmountSpent DESC"},
    {"Question" : "List the products with the highest price in each category.",
    "SQLQuery" : "SELECT p.Category, p.ProductID, p.Price \nFROM Products AS p \nGROUP BY p.Category, p.ProductID \nORDER BY p.Price DESC"},
]