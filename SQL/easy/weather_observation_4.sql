/* https://www.hackerrank.com/challenges/weather-observation-station-4/problem */

SELECT (count(city) - count(DISTINCT city)) 
FROM station;
