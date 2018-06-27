/* https://www.hackerrank.com/challenges/average-population-of-each-continent/problem */

SELECT continent, ROUND(AVG(city.population-0.5), 0) AS round_value
FROM country 
INNER JOIN city 
ON country.code = city.countrycode 
    GROUP BY continent;
