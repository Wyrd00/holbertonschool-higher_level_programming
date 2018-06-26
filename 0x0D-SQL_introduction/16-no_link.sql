--lists all records of the table second_table w/o name
SELECT `score`, `name`
FROM second_table
WHERE `name` IS NOT NULL
ORDER BY `score` DESC;
