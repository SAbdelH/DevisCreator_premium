-- CREATE VIEW "dette_client" ----------------------------------
SET lc_time to 'fr_FR.UTF-8';
CREATE OR REPLACE VIEW "informations"."dette_client" AS
WITH 
last as (
    SELECT
        client, mail_client, tel_client,
        MAX(crea_date) AS last_date
    FROM activites.factures
    GROUP BY 1, 2, 3
),
remiseClient AS(
    SELECT DISTINCT 
        client, mail_client, tel_client,
        SUBSTR(numero_facture, 1, 10) idfr, 
        total_remise
    FROM 
        activites.factures
),
sumClient AS (
    SELECT 
        client, mail_client, tel_client,
        SUBSTR(numero_facture, 1, 10) idf,
        SUM(prix_ttc) total_prix_ttc
    FROM 
        activites.factures
    GROUP BY 1, 2, 3, 4
),
commerces AS(
    SELECT client, mail_client, tel_client, SUM(commerce) commerce
    from (
        SELECT 
            sc.client, sc.mail_client, sc.tel_client, total_prix_ttc - total_remise commerce
        FROM sumClient sc
        LEFT JOIN remiseClient rc 
                ON (sc.client = rc.client) and (sc.mail_client = rc.mail_client) AND (sc.tel_client = rc.tel_client)
                    AND (rc.idfr = sc.idf)
    ) c
    GROUP BY 1, 2, 3
),
sumClientNP AS (
    SELECT 
        client, mail_client, tel_client,
        SUBSTR(numero_facture, 1, 10) idf,
        SUM(prix_ttc) total_prix_ttcNP
    FROM 
        activites.factures
    WHERE paye IS NOT TRUE
    GROUP BY 1, 2, 3, 4
),
dettes AS (
    SELECT client, mail_client, tel_client, SUM(dette) dette
    FROM 
        (select 
            sc.client, sc.mail_client, sc.tel_client, total_prix_ttcNP - total_remise dette
        from 
            sumClientNP sc
        LEFT JOIN remiseClient rc 
            ON (sc.client = rc.client) and (sc.mail_client = rc.mail_client) AND (sc.tel_client = rc.tel_client)
                AND (rc.idfr = sc.idf)
        ) d
    GROUP BY 1, 2, 3
),
status as (
    SELECT
        client, mail_client, tel_client,
        CASE
            WHEN MIN(COALESCE(paye, FALSE)::int) = 1 AND MAX(COALESCE(paye, FALSE)::int) = 1 THEN 'reglé'
            WHEN MIN(COALESCE(paye, FALSE)::int) = 0 AND MAX(COALESCE(paye, FALSE)::int) = 1 THEN 'en attente'
            ELSE 'endetté'
        END AS statut_paiement
    FROM activites.factures
    GROUP BY 1, 2, 3
)
select 
    TO_CHAR(crea_date, 'DD TMMon. YYYY à HH24:MI:SS') "crea_date", 
    nom, 
    telephone, 
    email, 
    CONCAT(c.commerce::TEXT, ' €') commerce, 
    CONCAT(COALESCE(d.dette::TEXT, '-'), ' €') dette, 
    UPPER(COALESCE(statut_paiement, 'reglé')) statut, 
    COALESCE(TO_CHAR(last_date::timestamp, 'DD TMMon. YYYY à HH24:MI:SS')::TEXT, '') last_date
FROM informations.clients
LEFT JOIN commerces c ON (c.client = nom) and (c.mail_client = email) AND (c.tel_client = telephone)
LEFT JOIN dettes d ON (d.client = nom) and (d.mail_client = email) AND (d.tel_client = telephone)
LEFT JOIN status s ON (s.client = nom) and (s.mail_client = email) AND (s.tel_client = telephone)
LEFT JOIN last l ON (l.client = nom) and (l.mail_client = email) AND (l.tel_client = telephone)
;