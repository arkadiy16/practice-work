# Exercise 8-1
# Construct a query that counts the number of rows in the payment table.
SELECT count(*)
  FROM payment;
# +----------+
# | count(*) |
# +----------+
# |    16049 |
# +----------+
# 1 row in set (0.01 sec)

# Exercise 8-2
# Modify your query from Exercise 8-1 to count the number of payments made by each
# customer. Show the customer ID and the total amount paid for each customer.
SELECT customer_id, SUM(amount)
  FROM payment
 GROUP BY 1
HAVING customer_id < 5 OR customer_id > 596;
# +-------------+-------------+
# | customer_id | SUM(amount) |
# +-------------+-------------+
# |           1 |      118.68 |
# |           2 |      128.73 |
# |           3 |      135.74 |
# |           4 |       81.78 |
# |         597 |       99.75 |
# |         598 |       83.78 |
# |         599 |       83.81 |
# +-------------+-------------+
# 7 rows in set (0.01 sec)

# Exercise 8-3
# Modify your query from Exercise 8-2 to include only those customers who have
# made at least 40 payments.
SELECT customer_id, count(*), SUM(amount)
  FROM payment
 GROUP BY 1
HAVING count(*) >= 40;
# +-------------+----------+-------------+
# | customer_id | count(*) | SUM(amount) |
# +-------------+----------+-------------+
# |          75 |       41 |      155.59 |
# |         144 |       42 |      195.58 |
# |         148 |       46 |      216.54 |
# |         197 |       40 |      154.60 |
# |         236 |       42 |      175.58 |
# |         469 |       40 |      177.60 |
# |         526 |       45 |      221.55 |
# +-------------+----------+-------------+
# 7 rows in set (0.02 sec)
