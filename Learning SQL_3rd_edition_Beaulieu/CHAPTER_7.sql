# Exercise 7-1
# Write a query that returns the 17th through 25th characters of the string 'Please
# find the substring in this string'.
mysql> SELECT SUBSTRING('Please find the substring in this string', 17, 9);
# +--------------------------------------------------------------+
# | SUBSTRING('Please find the substring in this string', 17, 9) |
# +--------------------------------------------------------------+
# | substring                                                    |
# +--------------------------------------------------------------+
# 1 row in set (0.00 sec)

# Exercise 7-2
# Write a query that returns the absolute value and sign (−1, 0, or 1) of the number
# −25.76823. Also return the number rounded to the nearest hundredth.
mysql> SELECT ABS(-25.76823) AS Absulute, SIGN(-25.76823), ROUND(-25.76823, 2);
# +----------+-----------------+---------------------+
# | Absulute | SIGN(-25.76823) | ROUND(-25.76823, 2) |
# +----------+-----------------+---------------------+
# | 25.76823 |              -1 |              -25.77 |
# +----------+-----------------+---------------------+
# 1 row in set (0.00 sec)

# Exercise 7-3
# Write a query to return just the month portion of the current date.
mysql> SELECT EXTRACT(MONTH FROM CURRENT_DATE()) AS current_month;
# +---------------+
# | current_month |
# +---------------+
# |             9 |
# +---------------+
# 1 row in set (0.00 sec)

mysql> SELECT MONTHNAME(CURRENT_DATE()) AS current_month;
# +---------------+
# | current_month |
# +---------------+
# |September     |
# +---------------+
# 1 row in set (0.00 sec)
