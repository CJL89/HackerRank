SET @P = 0;

SELECT REPEAT(' * ', @P := @P + 1)
FROM INFORMATION_SCHEMA.TABLES
LIMIT 20;