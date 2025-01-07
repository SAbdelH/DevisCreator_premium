SELECT CASE WHEN valid IS TRUE THEN 'Factures validées' ELSE 'Factures non-validées' END "valid",
       COUNT(DISTINCT SUBSTR(numero_devis,1,10)) AS effectif
    FROM activites.factures
    WHERE {filtre}
    GROUP BY 1;