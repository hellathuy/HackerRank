/* https://leetcode.com/problems/not-boring-movies/description/ */

SELECT id, movie, description, rating 
FROM cinema 
  WHERE id%2 != 0 AND description NOT LIKE "%boring%" ORDER BY rating DESC;
