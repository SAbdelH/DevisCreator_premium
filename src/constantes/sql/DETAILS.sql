SELECT * FROM 
(SELECT * FROM activites.details ORDER BY "date de création" DESC LIMIT 14) T 
ORDER BY "date de création" ASC