/* Query all columns for all American cities in CITY with populations larger than 100000. */

SELECT * 
FROM CITY
  WHERE POPULATION > 100000 AND COUNTRYCODE = 'USA';
