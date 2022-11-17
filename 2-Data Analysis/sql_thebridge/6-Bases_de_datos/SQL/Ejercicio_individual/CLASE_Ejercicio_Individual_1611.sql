/*Ejercicio Chinook SQL*/

SELECT DISTINCT Country
FROM customer;

/*1. Muestra los clientes de brasil*/
SELECT *
FROM customer
WHERE Country = 'Brazil';

/*2. Muestrame los empleados que son agentes de ventas*/

/* Vemos los tipos de profesion que hay*/
SELECT DISTINCT Title
FROM employee;

SELECT *
FROM employee
WHERE Title = 'Sales Support Agent';

/*3. Muestrame las canciones de ‘AC/DC’ */
SELECT DISTINCT Composer
FROM track;

SELECT *
FROM track
WHERE Composer = 'AC/DC';

/* 12*/

SELECT InvoiceDate
FROM invoice
WHERE year(InvoiceDate) = 2009 or year(InvoiceDate) = 2011;

/* 13*/

SELECT InvoiceDate
FROM invoice
WHERE year(InvoiceDate) between 2009 and 2011;

/* 14*/

SELECT Country, count(customerId) 
FROM customer
WHERE Country = 'Spain' or Country = 'Brazil'
group by Country;

/*15*/

select Name 
from track
where Name like 'You%';

SELECT *
FROM track
LIMIT 50;

SELECT * 
FROM genre;

SELECT track.*, genre.Name AS genre_desc
FROM track
OUTER JOIN genre
ON track.GenreId = genre.GenreId
WHERE genre.Name IN ('Rock', 'Latin')
ORDER BY genre.Name;


WITH
   exp1 AS (SELECT FIRSTNAME, LASTNAME FROM EMPLOYEE)
SELECT * FROM exp1;

WITH t1 AS
	(
			SELECT Employee.EmployeeId, Employee.LastName, SUM(Invoice.Total) AS Sales09
			FROM Customer
			JOIN Employee
			ON Employee.employeeId = Customer.SupportRepId
			JOIN Invoice
			ON Invoice.CustomerId = Customer.CustomerId
			WHERE EXTRACT(YEAR FROM InvoiceDate) IN (2009)
			GROUP BY Employee.employeeId)
SELECT LastName, MAX(Sales09) FROM t1;






