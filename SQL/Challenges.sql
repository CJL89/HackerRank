SELECT c.hacker_id, h.name ,count(c.hacker_id) AS c_count
FROM Hackers AS h
inner join Challenges AS c on c.hacker_id = h.hacker_id
GROUP BY c.hacker_id, h.name

HAVING
    /* output anyone with a count that is equal to... */
    c_count =
        /* the max count that anyone has */
        (SELECT MAX(temp1.cnt)
        FROM (SELECT COUNT(hacker_id) AS cnt
             FROM Challenges
             GROUP BY hacker_id
             ORDER BY hacker_id) temp1)

    /* OR anyone who's count is IN... */
    OR c_count IN
        /* the set of counts... */
        (SELECT t.cnt
         FROM (SELECT count(*) AS cnt
               FROM challenges
               GROUP BY hacker_id) t
         /* who's group of counts... */
         GROUP BY t.cnt
         /* has only one element */
         HAVING count(t.cnt) = 1)

ORDER BY c_count DESC, c.hacker_id
