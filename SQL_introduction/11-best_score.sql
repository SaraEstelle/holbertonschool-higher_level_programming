-- List records with score >= 10 ordred by best score
SELECT score, name
From second_table
WHERE score >= 10
ORDER BY score DESC;
