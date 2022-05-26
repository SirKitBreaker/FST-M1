--Write a query to find all the orders issued against the salesman who may works for customer whose id is 3007

SELECT * FROM orders
WHERE salesman_id in (SELECT DISTINCT salesman_id FROM orders WHERE customer_id=3007);

--Write a query to find all orders attributed to a salesman in New York

SELECT * FROM orders
WHERE salesman_id in (SELECT DISTINCT salesman_id FROM salesman WHERE salesman_city='New York');

--Write a query to count the customers with grades above New York's average

SELECT count(*) FROM customers
WHERE grade > (SELECT AVG(grade) FROM customers WHERE city='New York');

--Write a query to extract the data from the orders table for those salesman who earned the maximum commission

SELECT * FROM orders
WHERE salesman_id in (SELECT DISTINCT salesman_id FROM salesman WHERE commission = (SELECT max(commission) FROM salesman));