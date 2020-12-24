
SELECT H.HACKER_ID, H.NAME, SUM(SUB.SCORE)
FROM HACKERS H
JOIN (SELECT S.HACKER_ID, S.CHALLENGE_ID, MAX(S.SCORE) AS SCORE FROM SUBMISSIONS S GROUP BY S.HACKER_ID, S.CHALLENGE_ID) AS SUB ON H.HACKER_ID = SUB.HACKER_ID
GROUP BY H.HACKER_ID, H.NAME
HAVING SUM(SUB.SCORE) > 0
ORDER BY SUM(SUB.SCORE) DESC, H.HACKER_ID
