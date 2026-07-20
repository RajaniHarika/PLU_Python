CREATE DATABASE CompanyDB;

USE CompanyDB;

CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY,
    EmployeeName VARCHAR(100),
    Department VARCHAR(50),
    Salary INT,
    JoiningDate DATE
);