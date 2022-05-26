--Write an SQL statement to find the highest purchase amount ordered by the each customer with their ID and highest purchase amount.

SELECT customer_id, MAX(purchase_amount) AS max_purchase_amount FROM ORDERS
GROUP BY customer_id
ORDER BY customer_id,max_purchase_amount;

--Write an SQL statement to find the highest purchase amount on '2012-08-17' for each salesman with their ID.

SELECT salesman_id, MAX(purchase_amount) AS max_purchase_amount FROM ORDERS
WHERE ORDER_DATE = TO_DATE('2012-08-17','YYYY-MM-DD')
GROUP BY salesman_id;

--Write an SQL statement to find the highest purchase amount with their ID and order date, 
--for only those customers who have a higher purchase amount within the list [2030, 3450, 5760, 6000].

SELECT customer_id,order_date, MAX(purchase_amount) AS max_purchase_amount FROM ORDERS
GROUP BY customer_id,order_date
HAVING MAX(purchase_amount) in (2030, 3450, 5760, 6000);
