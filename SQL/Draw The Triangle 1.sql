SET @P = 21;

SELECT REPEAT(' * ', @P := @P - 1)
FROM INFORMATION_SCHEMA.TABLES