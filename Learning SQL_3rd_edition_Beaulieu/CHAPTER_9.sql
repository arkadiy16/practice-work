# Exercise 9-1
# Construct a query against the film table that uses a filter condition with a noncorre‐
# lated subquery against the category table to find all action films (category.name =
# 'Action').
SELECT f.title
  FROM film AS f
 WHERE f.film_id IN
       (SELECT f_c.film_id
          FROM film_category AS f_c
               INNER JOIN category AS c
               ON f_c.category_id = c.category_id
                  AND c.name = 'Action');
# +-------------------------+
# | title                   |
# +-------------------------+
# | AMADEUS HOLY            |
# | AMERICAN CIRCUS         |
# ...........................
# | WEREWOLF LOLA           |
# | WOMEN DORADO            |
# | WORST BANGER            |
# +-------------------------+
# 64 rows in set (0.00 sec)

# Exercise 9-2
# Rework the query from Exercise 9-1 using a correlated subquery against the category
SELECT f.title
  FROM film AS f
 WHERE 'Action' =
       (SELECT c.name
          FROM category AS c
               INNER JOIN film_category AS f_c
               ON c.category_id = f_c.category_id
                  AND f_c.film_id = f.film_id);
                  
# Exercise 9-3
# Join the following query to a subquery against the film_actor table to show the level
# of each actor:
# SELECT 'Hollywood Star' level, 30 min_roles, 99999 max_roles
# UNION ALL
# SELECT 'Prolific Actor' level, 20 min_roles, 29 max_roles
# UNION ALL
# SELECT 'Newcomer' level, 1 min_roles, 19 max_roles
# The subquery against the film_actor table should count the number of rows for each
# actor using group by actor_id, and the count should be compared to the
# min_roles/max_roles columns to determine which level each actor belongs to.
SELECT first_name, last_name, level
  FROM
       (SELECT actor_id, count(*) AS ttl_roles
          FROM film_actor
         GROUP BY actor_id) AS ttl
  INNER JOIN actor AS a
  ON a.actor_id = ttl.actor_id
 
  INNER JOIN
             (SELECT 'Hollywood Star' AS level, 30 AS min_roles, 99999 AS max_roles
              UNION ALL
              SELECT 'Prolific Actor' AS level, 20 AS min_roles, 29 AS max_roles
              UNION ALL
              SELECT 'Newcomer' AS level, 1 AS min_roles, 19 AS max_roles) AS lvl
  ON ttl.ttl_roles BETWEEN lvl.min_roles AND lvl.max_roles
ORDER BY 3;
# +-------------+--------------+----------------+
# | first_name  | last_name    | level          |
# +-------------+--------------+----------------+
# | GRACE       | MOSTEL       | Hollywood Star |
# | KARL        | BERRY        | Hollywood Star |
# | UMA         | WOOD         | Hollywood Star |
# ...............................................
# | JAYNE       | SILVERSTONE  | Prolific Actor |
# | THORA       | TEMPLE       | Prolific Actor |
# +-------------+--------------+----------------+
# 200 rows in set (0.00 sec)
