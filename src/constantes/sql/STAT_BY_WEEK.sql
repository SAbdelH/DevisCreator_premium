WITH jours_semaine AS (
    SELECT
        '{{"1": "Lundi",
          "2": "Mardi",
          "3": "Mecredi",
          "4": "Jeudi",
          "5": "Vendredi",
          "6": "Samedi",
          "0": "Dimanche"}}'::JSONB AS jour_mapping
),
stat AS (
    SELECT EXTRACT(DOW FROM crea_date)::TEXT AS nday, COUNT(DISTINCT SUBSTR(numero_devis,1,10)) AS effectif
    FROM activites.{table}
    WHERE date_part('week',crea_date) = date_part('week',CURRENT_DATE)
    GROUP BY 1
)

SELECT jour_mapping->>key AS jour, COALESCE(effectif, 0) AS effectif
FROM jours_semaine,
LATERAL JSONB_EACH_TEXT(jour_mapping) AS j(key, val)
LEFT JOIN stat ON key = stat.nday
ORDER BY REPLACE(key,'0','7')::INT;