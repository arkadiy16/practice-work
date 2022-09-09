Exercise 4-1
Which of the payment IDs would be returned by the following filter conditions?
customer_id <> 5 AND (amount > 8 OR date(payment_date) = '2005-08-23')
Answer: ID = [101, 107]

Exercise 4-2
Which of the payment IDs would be returned by the following filter conditions?
customer_id = 5 AND NOT (amount > 6 OR date(payment_date) = '2005-06-19')
Answer: ID = [108, 110, 111, 112, 113, 115, 116, 117, 118, 119, 120]

Exercise 4-3
Construct a query that retrieves all rows from the payments table where the amount
is either 1.98, 7.98, or 9.98.
SELECT * 
  FROM payment
 WHERE amount = 1.98
    OR amount = 7.98
    OR amount = 9.98;

Exercise 4-4
Construct a query that finds all customers whose last name contains an A in the sec‐
ond position and a W anywhere after the A.
SELECT * 
  FROM customer
 WHERE last_name LIKE '_A%W%';
 
