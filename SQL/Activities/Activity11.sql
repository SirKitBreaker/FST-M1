--Write a query that produces the name and number of each salesman and each customer with more than one current order. 
--Put the results in alphabetical order.

SELECT * FROM (
SELECT customer_id AS ID ,customer_name AS NAME
FROM customers WHERE customer_id in (SELECT customer_id FROM orders 
GROUP BY customer_id HAVING COUNT(order_no) > 1)
UNION
SELECT salesman_id,salesman_name
FROM salesman WHERE salesman_id in (SELECT salesman_id FROM orders 
GROUP BY salesman_id HAVING COUNT(order_no) > 1)
) ORDER BY NAME 

--Write a query to make a report of which salesman produce the largest and smallest orders on each date. 
--Also add a column that shows "highest on" and "lowest on" values

SELECT * FROM (
SELECT salesman_id,'highest on',order_date FROM orders o
WHERE purchase_amount=(SELECT MAX(purchase_amount) FROM orders a WHERE a.order_date = o.order_date)
UNION
SELECT salesman_id,'lowest on',order_date FROM orders o
WHERE purchase_amount=(SELECT MIN(purchase_amount) FROM orders a WHERE a.order_date = o.order_date)
) ORDER BY order_date;

