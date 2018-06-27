/* https://www.hackerrank.com/challenges/weather-observation-station-7/problem */

SELECT DISTINCT city FROM station 
    WHERE city LIKE "%a"
UNION
SELECT DISTINCT city FROM station 
    WHERE city LIKE "%e"
UNION
SELECT DISTINCT city FROM station 
    WHERE city LIKE "%i"
UNION
SELECT DISTINCT city FROM station 
    WHERE city LIKE "%o"
UNION
SELECT DISTINCT city FROM station 
    WHERE city LIKE "%u";
