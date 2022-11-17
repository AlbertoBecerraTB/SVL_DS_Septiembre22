
/* 1. Facturas de Clientes de Brasil, Nombre del cliente, Id de factura, fecha de la factura
y el pais de la factura */

SELECT CONCAT(c.FirstName, ' ', c.LastName) AS  "Name",
		c.Country,
		i.InvoiceId,
        i.InvoiceDate,
        i.BillingCountry
FROM invoice i
LEFT JOIN customer c
ON i.CustomerId = c.CustomerId
WHERE c.Country="Brazil";

/*2. Facturas de Clientes de Brasil*/
SELECT i.*
FROM invoice i
LEFT JOIN customer c
ON i.CustomerId = c.CustomerId
WHERE c.Country="Brazil";

/*3. Muestra cada factura asociada a cada agente de ventas con su nombre completo*/
SELECT CONCAT(e.FirstName, ' ', e.LastName) AS "Name",
		e.Title,
        i.*
FROM invoice i
LEFT JOIN customer c
ON i.CustomerId = c.CustomerId
LEFT JOIN employee e
ON c.SupportRepId = e.EmployeeId
WHERE e.Title = "Sales Support Agent";


/*4. Muestra el nombre del cliente, el pais, el nombre del agente y el total*/
SELECT CONCAT(c.FirstName, ' ', c.LastName) AS "Name",
		c.Country,
        CONCAT(e.FirstName, ' ', e.LastName) AS "Agent Name",
        i.Total
FROM customer c
LEFT JOIN employee e
ON c.SupportRepId = e.EmployeeId
LEFT JOIN invoice i
ON i.CustomerId = c.CustomerId
WHERE e.Title = "Sales Support Agent";
        

/*5. Muestra cada articulo de la factura con el nombre de la cancion*/
SELECT i.InvoiceId,
		il.*,
		t.Name
FROM invoice i
INNER JOIN invoiceline il
ON i.InvoiceId = il.InvoiceId
INNER JOIN track t
ON t.TrackId = il.TrackId;


/*6. Muestra todas las canciones con su nombre, formato, album y genero*/
SELECT t.Name AS SongName,
		mt.Name AS MediaType,
        a.Title AS Album,
        g.Name AS Genre
FROM track t
LEFT JOIN mediatype mt
ON t.MediaTypeId = mt.MediaTypeId
LEFT JOIN album a
ON t.AlbumId = a.AlbumId
LEFT JOIN genre g
ON t.GenreId = g.GenreId;


/*7. Muestr a cuantas canciones hay en cada playlist y el nombre de cada playlist*/
SELECT CAST(p.Name as nvarchar) AS PlaylistName,
		COUNT(pt.TrackId) AS PlaylistSongs
FROM playlist p
LEFT JOIN playlisttrack pt
ON p.PlaylistId = pt.PlaylistId
GROUP BY 1;

/*8. Muestra cuánto ha vendido cada empleado*/
SELECT CONCAT(e.FirstName, ' ', e.LastName) AS "Name",
		SUM(i.Total) AS TotalSale
FROM invoice i
LEFT JOIN customer c
ON i.CustomerId = c.CustomerId
LEFT JOIN employee e
ON c.SupportRepId = e.EmployeeId
group by 1;

/*9. Quien ha sido el agente de ventas que más ha vendido en 2009?*/

SELECT total.Name, MAX(total.TotalSale)
FROM (SELECT CONCAT(e.FirstName, ' ', e.LastName) AS "Name",
				SUM(i.Total) AS TotalSale
		FROM invoice i
		LEFT JOIN customer c
		ON i.CustomerId = c.CustomerId
		LEFT JOIN employee e
		ON c.SupportRepId = e.EmployeeId
		WHERE YEAR(i.InvoiceDate) = 2009
		group by 1) total;

SELECT CONCAT(e.FirstName, ' ', e.LastName) AS "Name",
				SUM(i.Total) AS TotalSale
		FROM invoice i
		LEFT JOIN customer c
		ON i.CustomerId = c.CustomerId
		LEFT JOIN employee e
		ON c.SupportRepId = e.EmployeeId
		WHERE YEAR(i.InvoiceDate) = 2009
		group by 1
        ORDER BY 2 DESC
        LIMIT 1;

WITH total AS (SELECT CONCAT(e.FirstName, ' ', e.LastName) AS "Name",
						SUM(i.Total) AS TotalSale
				FROM invoice i
				LEFT JOIN customer c
				ON i.CustomerId = c.CustomerId
				LEFT JOIN employee e
				ON c.SupportRepId = e.EmployeeId
				WHERE YEAR(i.InvoiceDate) = 2009
				group by 1)
	
SELECT Name, Max(TotalSale)
FROM total;



/*10. Quien es son los 3 grupos que más han vendido?*/
SELECT ar.Name,
		SUM(i.Total) AS TotalSales
FROM invoice i
LEFT JOIN invoiceline il
ON i.InvoiceId = il.InvoiceId
LEFT JOIN track t
ON il.TrackId = t.TrackId
LEFT JOIN album a
ON t.AlbumId = a.AlbumId
LEFT JOIN artist ar
ON ar.ArtistId = a.ArtistId
GROUP BY ar.Name
ORDER BY 2 DESC
LIMIT 3;







