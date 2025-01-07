SET lc_time to 'fr_FR.UTF-8';
WITH mois_jours AS (
    SELECT GENERATE_SERIES(
        DATE_TRUNC('month', CURRENT_DATE)::DATE, -- Premier jour du mois en cours
        (DATE_TRUNC('month', CURRENT_DATE) + INTERVAL '1 month - 1 day')::DATE, -- Dernier jour du mois en cours
        '1 day'::INTERVAL  -- Intervalle de 1 jour
    )::DATE AS jour
),
stat AS (
    SELECT crea_date::DATE AS jour, COUNT(DISTINCT SUBSTR(numero_devis, 1, 10)) AS effectif
    FROM activites.{table}
    WHERE date_part('month',crea_date) = date_part('month',CURRENT_DATE)
    GROUP BY 1
)

SELECT TO_CHAR(mois_jours.jour, 'DD TMMon') jour, COALESCE(stat.effectif, 0) AS effectif
FROM mois_jours
LEFT JOIN stat ON mois_jours.jour = stat.jour
ORDER BY mois_jours.jour;