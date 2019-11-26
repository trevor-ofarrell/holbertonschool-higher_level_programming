-- list sum of groups with same score
SELECT score,
       COUNT(*) AS number
FROM second_table
GROUP BY score
HAVING number >= 1
ORDER BY number DESC;
