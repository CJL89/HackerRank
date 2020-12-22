/*
Enter your query here.
*/
SELECT CONCAT(O.Name, '(', LEFT(O.Occupation, 1), ')')
FROM OCCUPATIONS O
ORDER BY O.Name;
SELECT CONCAT('There are a total of ', COUNT(O1.Occupation), ' ', LOWER(O1.Occupation), 's.') as total
FROM OCCUPATIONS O1
GROUP BY O1.Occupation
ORDER BY total
