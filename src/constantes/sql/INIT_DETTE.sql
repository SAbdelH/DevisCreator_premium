-- CREATE VIEW "dette_client" ----------------------------------
CREATE OR REPLACE VIEW "informations"."dette_client" AS
WITH last as (
    SELECT
        client,
        MAX(crea_date) AS last_date
    FROM activites.factures
    GROUP BY 1
),
dettes as (
    select client, SUM((quantite*prix_unite)) dette
    from activites.factures
    WHERE paye IS NOT TRUE
    GROUP BY 1
),
status as (
    SELECT
        client,
        CASE
            WHEN MIN(COALESCE(paye, FALSE)::int) = 1 AND MAX(COALESCE(paye, FALSE)::int) = 1 THEN 'reglé'
            WHEN MIN(COALESCE(paye, FALSE)::int) = 0 AND MAX(COALESCE(paye, FALSE)::int) = 1 THEN 'en attente'
            ELSE 'endetté'
        END AS statut_paiement
    FROM activites.factures
    GROUP BY client
)
SELECT crea_date, nom, telephone, email, CONCAT(commerce::TEXT, ' €') commerce, CONCAT(dette::TEXT, ' €') dette, UPPER(statut_paiement) statut,
COALESCE(last_date::TEXT, '') last_date
FROM informations.clients
LEFT JOIN dettes d ON d.client = nom
LEFT JOIN last l ON d.client = nom
LEFT JOIN status s ON s.client = nom
;