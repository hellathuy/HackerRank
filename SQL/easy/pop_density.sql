/* https://www.hackerrank.com/challenges/population-density-difference/problem */

SELECT (max(population) - min(population)) AS difference 
FROM city
