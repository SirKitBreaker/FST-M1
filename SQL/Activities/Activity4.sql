--Add new column grade to salesman table

ALTER TABLE salesman ADD (grade int);

--update salesman table to set grade to 100

UPDATE salesman SET grade = 100;

SELECT * from salesman;