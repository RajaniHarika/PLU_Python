CREATE DATABASE CompanyDB;

USE CompanyDB;

CREATE TABLE Orders (
    OrderID INT,
    CustomerName VARCHAR(50),
    OrderDate DATE,
    Amount INT
);

CREATE INDEX idx_OrderID
ON Orders(OrderID);