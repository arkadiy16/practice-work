# Exercise 5-1
# Fill in the blanks (denoted by <#>) for the following query to obtain the results that
# follow:
# +------------+-----------+------------------------+----------------+
# | first_name | last_name | address | city |
# +------------+-----------+------------------------+----------------+
# | PATRICIA | JOHNSON | 1121 Loja Avenue | San Bernardino |
# | BETTY | WHITE | 770 Bydgoszcz Avenue | Citrus Heights |
# | ALICE | STEWART | 1135 Izumisano Parkway | Fontana |
# | ROSA | REYNOLDS | 793 Cam Ranh Avenue | Lancaster |
# | RENEE | LANE | 533 al-Ayn Boulevard | Compton |
# | KRISTIN | JOHNSTON | 226 Brest Manor | Sunnyvale |
# |CASSANDRA | WALTERS | 920 Kumbakonam Loop | Salinas |
# |JACOB | LANCE | 1866 al-Qatif Avenue | El Monte |
# | RENE | MCALISTER | 1895 Zhezqazghan Drive | Garden Grove |
# +------------+-----------+------------------------+----------------+
# 9 rows in set (0.00 sec)
SELECT c.first_name, c.last_name, a.address, ct.city
  FROM customer AS c
       INNER JOIN address AS a
       ON c.address_id = a.address_id
       INNER JOIN city AS ct
       ON a.city_id = ct.city_id
 WHERE a.district = 'California';
 
# Exercise 5-2
# Write a query that returns the title of every film in which an actor with the first name
# JOHN appeared.
SELECT f.title
  FROM film as f
       INNER JOIN film_actor as fa
       ON f.film_id = fa.film_id
       INNER JOIN actor AS a
       ON fa.actor_id = a.actor_id
 WHERE a.first_name = 'JOHN';
# +---------------------------+
# | title                     |
# +---------------------------+
# | ALLEY EVOLUTION           |
# | BEVERLY OUTLAW            |
# | CANDLES GRAPES            |
# | CLEOPATRA DEVIL           |
# | COLOR PHILADELPHIA        |
#  ...........................
# | SATISFACTION CONFIDENTIAL |
# | SONG HEDWIG               |
# +---------------------------+
# 29 rows in set (0.00 sec) 


# Exercise 5-3
# Construct a query that returns all addresses that are in the same city. You will need to
# join the address table to itself, and each row should include two different addresses.
SELECT a1.address, a2.address
  FROM address AS a1
       INNER JOIN address AS a2
       ON a1.city_id = a2.city_id
 WHERE a1.address != a2.address
 GROUP BY a1.city_id;
# +--------------------+----------------------+
# | address            | address              |
# +--------------------+----------------------+
# | 47 MySakila Drive  | 23 Workhaven Lane    |
# | 28 MySQL Boulevard | 1411 Lillydale Drive |
# | 1497 Yuzhou Drive  | 548 Uruapan Street   |
# | 587 Benguela Manor | 43 Vilnius Manor     |
# +--------------------+----------------------+
# 4 rows in set (0.00 sec)
