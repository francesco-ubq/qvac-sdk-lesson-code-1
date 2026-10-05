-- The query the agent writes on screen
-- Lesson: 2:45 (idea 01 card) and again in the s08 agent loop at 5:12
SELECT name, SUM(total)
FROM orders GROUP BY 1
ORDER BY 2 DESC LIMIT 5;
