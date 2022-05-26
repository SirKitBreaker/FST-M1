--Write an SQL statement to find the total purchase amount of all orders.

SELECT SUM(purchase_amount) AS total_purchase FROM orders;

--Write an SQL statement to find the average purchase amount of all orders

SELECT AVG(purchase_amount) AS average_purchase FROM orders;

--Write an SQL statement to get the maximum purchase amount of all the orders

SELECT MAX(purchase_amount) AS max_purchase_amount FROM orders;

--Write an SQL statement to get the minimum purchase amount of all the orders.

SELECT MIN(purchase_amount) AS min_purchase_amount FROM orders;

--Write an SQL statement to find the number of salesmen listed in the table

SELECT count(distinct salesman_id) AS number_of_salesman FROM orders;
