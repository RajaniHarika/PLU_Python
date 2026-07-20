CREATE DATABASE CompanyDB;

USE CompanyDB;

CREATE TABLE Book (
    BookID INT,
    BookName VARCHAR(100),
    Author VARCHAR(50),
    Price INT
);

INSERT INTO Book
VALUES
(1,'Python Basics','John',500),
(2,'Learning SQL','David',700);

DELIMITER //

CREATE PROCEDURE GetBooks()
BEGIN
    SELECT * FROM Book;
END //

DELIMITER ;

CALL GetBooks();