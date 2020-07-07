-- https://leetcode.com/problems/rank-scores/

-- https://dev.mysql.com/doc/refman/8.0/en/window-function-descriptions.html#function_rank
SELECT score, DENSE_RANK() OVER w AS 'Rank'
FROM Scores
WINDOW w AS (ORDER BY score DESC);
