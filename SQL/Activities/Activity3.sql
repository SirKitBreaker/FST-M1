--Display data depending on different conditions

SELECT salesman_id,salesman_city 
FROM salesman;

SELECT salesman_id,salesman_city 
FROM salesman 
WHERE salesman_city = 'Paris';

SELECT salesman_id , commission  
FROM salesman 
WHERE salesman_name = 'Paul Adam';

