WITH mois_annuel AS (
    SELECT
        '{{"01": "Janv",
          "02": "Févr",
          "03": "Mars",
          "04": "Avril",
          "05": "Mai",
          "06": "Juin",
          "07": "Juil",
          "08": "Août",
          "09": "Sept",
          "10": "Oct",
          "11": "Nov",
          "12": "Déc"}}'::JSONB AS month_mapping
),
stat AS (
    SELECT TO_CHAR(crea_date, 'mm') AS nmonth, COUNT(DISTINCT SUBSTR({col_idx},1,10)) AS effectif
    FROM activites.{table}
    WHERE TO_CHAR(crea_date, 'yyyy') = TO_CHAR(CURRENT_DATE, 'yyyy')
    GROUP BY 1
)

SELECT month_mapping->>key AS jour, COALESCE(effectif, 0) AS effectif
FROM mois_annuel,
LATERAL JSONB_EACH_TEXT(month_mapping) AS j(key, val)
LEFT JOIN stat ON key = stat.nmonth
ORDER BY key::INT;