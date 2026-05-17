CREATE DATABASE customer_behavior;

USE customer_behavior;

CREATE TABLE customer_data (
    CustomerID VARCHAR(20),
    InvoiceNo VARCHAR(20),
    StockCode VARCHAR(20),
    Description TEXT,
    Quantity INT,
    InvoiceDate DATETIME,
    UnitPrice FLOAT,
    Country VARCHAR(100),
    TotalPrice FLOAT
);
