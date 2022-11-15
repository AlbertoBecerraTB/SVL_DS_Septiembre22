
/* 1. Clientes de Brasil */

SELECT *
FROM chinook.customer
where Country = 'Brazil';

/* 2. Empleados agentes de ventas*/

SELECT *
FROM chinook.employee
WHERE Title	= 'Sales Support Agent';

/* 3. Canciones AC DC*/

SELECT *
FROM track
WHERE composer = 'AC/DC';

/* 4. Clientes que no sean de USA*/

SELECT c.CustomerId, c.FirstName, c.LastName, c.Country
FROM customer AS c
WHERE c.Country != 'USA';

-- Comprobación de que ha desaparecido USA de Country.
SELECT DISTINCT Country 
FROM  (SELECT c.CustomerId, c.FirstName, c.LastName, c.Country
		FROM customer AS c
		WHERE c.Country != 'USA') AS c2
order by Country;

/* 5. Agentes de ventas*/

SELECT e.FirstName, 
	   e.LastName, 
       e.Address,
       e.City, 
       e.State, 
       e.Country,
       e.Email
FROM employee as e
WHERE e.Title = 'Sales Support Agent';

/* 6. Paises únicos facturados*/

SELECT DISTINCT i.BillingCountry
FROM invoice AS i
ORDER BY 1;

/* 7. Estados de los clientes*/

SELECT DISTINCT c.State
FROM customer AS c
WHERE c.Country = 'USA';

/* 8. Factura 37*/

SELECT InvoiceId, 
	   SUM(Quantity) AS Quantity_37
FROM invoiceline
WHERE InvoiceId=37;

/* 9. Canciones AC/DC */

SELECT COUNT(*) AS ACDC_Songs
FROM track
WHERE Composer = 'AC/DC';

/* 10. Artículos por factura */

SELECT InvoiceId, 
	   SUM(Quantity) as Quantity
FROM invoiceline
GROUP BY 1
ORDER BY 2 DESC;

/* 11. Facturas de cada país */

SELECT BillingCountry,
	   COUNT(InvoiceId) as Quantity
FROM invoice
GROUP BY BillingCountry
ORDER BY 2 DESC;

/* 12. Facturas en 2009 y 2011 */

SELECT YEAR(InvoiceDate) AS InvoiceYear,
	   COUNT(InvoiceId) AS Quantity
FROM invoice
WHERE YEAR(InvoiceDate) IN (2009, 2011)
GROUP BY InvoiceYear;     

/* 13. Facturas entre 2009 y 2011 */

SELECT COUNT(InvoiceId) AS Quantity
FROM invoice
WHERE YEAR(InvoiceDate) BETWEEN 2009 AND 2011; 

-- Comprobación
SELECT YEAR(InvoiceDate) AS InvoiceYear,
	   COUNT(InvoiceId) AS Quantity
FROM invoice
WHERE YEAR(InvoiceDate) BETWEEN 2009 AND 2011
GROUP BY YEAR(InvoiceDate); 

/* 14. Cuantos clientes hay de españa y de Brazil*/

SELECT Country,
	   COUNT(CustomerId) AS Quantity
FROM customer
WHERE Country IN ('Spain', 'Brazil')
GROUP BY 1;

/* 15. Muestrame las canciones que su titulo empieza por ‘You’ */

SELECT *
FROM track
WHERE Name LIKE 'You%';

--------- SEGUNDA PARTE ----------

/* 1. Facturas de Clientes de Brasil, 
Nombre del cliente, Id de factura, fecha de la factura
y el pais de la factura*/

SELECT i.InvoiceId, 
		CONCAT(c.FirstName, ' ', c.LastName) AS FullName,
        c.Country,
        i.InvoiceId,
        i.InvoiceDate,
        i.BillingCountry
FROM invoice AS i
JOIN customer AS c
ON i.CustomerId = c.CustomerId
WHERE c.Country='Brazil'
ORDER BY FullName;

-- Comprobación
SELECT DISTINCT CONCAT(c.FirstName, ' ', c.LastName) FROM customer AS c WHERE c.Country='Brazil';

/* 3. Muestra cada factura asociada a cada agente de ventas con su nombre completo*/

SELECT i.*,
		CONCAT(e.FirstName, ' ', e.LastName) AS FullName,
        e.Title
FROM invoice AS i
JOIN customer AS c
ON i.CustomerId = c.CustomerId
JOIN employee AS e
ON c.SupportRepId = e.EmployeeId
WHERE e.Title='Sales Support Agent';

/* 4. Muestra el nombre del cliente, el pais, el nombre del agente y el total*/

SELECT i.InvoiceId,
		CONCAT(c.FirstName, ' ', c.LastName) AS FullCustomerName,
        c.Country,
        CONCAT(e.FirstName, ' ', e.LastName) AS FullAgentName,
        i.Total
FROM invoice AS i
JOIN customer AS c
ON i.CustomerId = c.CustomerId
JOIN employee AS e
ON c.SupportRepId = e.EmployeeId
WHERE e.Title='Sales Support Agent';

-- Otra Opcion
SELECT
		CONCAT(c.FirstName, ' ', c.LastName) AS FullCustomerName,
        c.Country,
        CONCAT(e.FirstName, ' ', e.LastName) AS FullAgentName,
        SUM(i.Total)
FROM invoice AS i
JOIN customer AS c
ON i.CustomerId = c.CustomerId
JOIN employee AS e
ON c.SupportRepId = e.EmployeeId
WHERE e.Title='Sales Support Agent'
GROUP BY 1, 3;

/* 9. Quien ha sido el agente de ventas que más ha vendido en 2009? */

-- Forma Fácil
SELECT CONCAT(e.FirstName, ' ', e.LastName) AS FullEmployeeName,
		SUM(i.Total) AS TotalSale
FROM employee AS e
JOIN customer AS c
ON c.SupportRepId = e.EmployeeId
JOIN invoice AS i
ON i.CustomerId = c.CustomerId
WHERE e.Title = 'Sales Support Agent' AND YEAR(i.InvoiceDate) = 2009
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1;

-- Usando una vista temporal
WITH EmpSales AS (
SELECT CONCAT(e.FirstName, ' ', e.LastName) AS FullEmployeeName,
			 SUM(i.Total) AS TotalSale
		FROM employee AS e
		JOIN customer AS c
		ON c.SupportRepId = e.EmployeeId
		JOIN invoice AS i
		ON i.CustomerId = c.CustomerId
		WHERE e.Title = 'Sales Support Agent' AND YEAR(i.InvoiceDate) = 2009
		GROUP BY 1
)
SELECT es.FullEmployeeName,
		es.TotalSale
FROM EmpSales AS es
WHERE es.TotalSale = (select MAX(TotalSale) FROM EmpSales);

-- Guardando una vista
CREATE VIEW vw_FullEmployeeName AS (
SELECT CONCAT(e.FirstName, ' ', e.LastName) AS FullEmployeeName,
			 SUM(i.Total) AS TotalSale
		FROM employee AS e
		JOIN customer AS c
		ON c.SupportRepId = e.EmployeeId
		JOIN invoice AS i
		ON i.CustomerId = c.CustomerId
		WHERE e.Title = 'Sales Support Agent' AND YEAR(i.InvoiceDate) = 2009
		GROUP BY 1
);

SELECT es.FullEmployeeName,
		es.TotalSale
FROM vw_FullEmployeeName AS es
WHERE es.TotalSale = (select MAX(TotalSale) FROM vw_FullEmployeeName);






