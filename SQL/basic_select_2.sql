/* Query the names of all American cities in CITY with populations larger than 120000. */

SELECT NAME 
FROM CITY 
  WHERE POPULATION > 120000 AND COUNTRYCODE = 'USA';
