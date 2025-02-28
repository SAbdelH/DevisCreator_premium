WITH achat_semaine AS (
    SELECT semaine.annee, semaine.semaine_num,
           semaine.semaine_debut, semaine.semaine_fin,
           COALESCE(SUM(achat.prix), 0) AS achat
    FROM (
        -- Définition des 3 dernières semaines avec numéro de semaine
        SELECT 
            EXTRACT(YEAR FROM (CURRENT_DATE - INTERVAL '2 weeks'))::integer AS annee,
            EXTRACT(WEEK FROM (CURRENT_DATE - INTERVAL '2 weeks'))::integer AS semaine_num,
            (date_trunc('week', CURRENT_DATE - INTERVAL '2 weeks'))::date AS semaine_debut,
            (date_trunc('week', CURRENT_DATE - INTERVAL '2 weeks') + INTERVAL '1 week - 1 day')::date AS semaine_fin
        UNION
        SELECT 
            EXTRACT(YEAR FROM (CURRENT_DATE - INTERVAL '1 week'))::integer AS annee,
            EXTRACT(WEEK FROM (CURRENT_DATE - INTERVAL '1 week'))::integer AS semaine_num,
            (date_trunc('week', CURRENT_DATE - INTERVAL '1 week'))::date AS semaine_debut,
            (date_trunc('week', CURRENT_DATE - INTERVAL '1 week') + INTERVAL '1 week - 1 day')::date AS semaine_fin
        UNION
        SELECT 
            EXTRACT(YEAR FROM CURRENT_DATE)::integer AS annee,
            EXTRACT(WEEK FROM CURRENT_DATE)::integer AS semaine_num,
            (date_trunc('week', CURRENT_DATE))::date AS semaine_debut,
            (date_trunc('week', CURRENT_DATE) + INTERVAL '1 week - 1 day')::date AS semaine_fin
    ) AS semaine
    LEFT JOIN activites.achat AS achat 
        ON achat.crea_date::date >= semaine.semaine_debut AND achat.crea_date::date <= semaine.semaine_fin
    GROUP BY semaine.annee, semaine.semaine_num, semaine.semaine_debut, semaine.semaine_fin
    ORDER BY semaine.semaine_debut
),
facture_semaine AS (
    SELECT semaine.annee, semaine.semaine_num,
           semaine.semaine_debut, semaine.semaine_fin,
           COALESCE(SUM(factures.prix_ttc), 0) AS facture
    FROM (
        -- Définition des 3 dernières semaines avec numéro de semaine
        SELECT 
            EXTRACT(YEAR FROM (CURRENT_DATE - INTERVAL '2 weeks'))::integer AS annee,
            EXTRACT(WEEK FROM (CURRENT_DATE - INTERVAL '2 weeks'))::integer AS semaine_num,
            (date_trunc('week', CURRENT_DATE - INTERVAL '2 weeks'))::date AS semaine_debut,
            (date_trunc('week', CURRENT_DATE - INTERVAL '2 weeks') + INTERVAL '1 week - 1 day')::date AS semaine_fin
        UNION
        SELECT 
            EXTRACT(YEAR FROM (CURRENT_DATE - INTERVAL '1 week'))::integer AS annee,
            EXTRACT(WEEK FROM (CURRENT_DATE - INTERVAL '1 week'))::integer AS semaine_num,
            (date_trunc('week', CURRENT_DATE - INTERVAL '1 week'))::date AS semaine_debut,
            (date_trunc('week', CURRENT_DATE - INTERVAL '1 week') + INTERVAL '1 week - 1 day')::date AS semaine_fin
        UNION
        SELECT 
            EXTRACT(YEAR FROM CURRENT_DATE)::integer AS annee,
            EXTRACT(WEEK FROM CURRENT_DATE)::integer AS semaine_num,
            (date_trunc('week', CURRENT_DATE))::date AS semaine_debut,
            (date_trunc('week', CURRENT_DATE) + INTERVAL '1 week - 1 day')::date AS semaine_fin
    ) AS semaine
    LEFT JOIN (
        SELECT *
        FROM activites.factures
        WHERE factures.paye IS true
    ) AS factures 
        ON factures.crea_date::date >= semaine.semaine_debut AND factures.crea_date::date <= semaine.semaine_fin
    GROUP BY semaine.annee, semaine.semaine_num, semaine.semaine_debut, semaine.semaine_fin
    ORDER BY semaine.semaine_debut
)

SELECT 
    'Semaine ' || a.semaine_num AS semaines,
    a.achat "Achats (€)",
    f.facture "Ventes (€)"
FROM achat_semaine a
LEFT JOIN facture_semaine f ON f.semaine_debut = a.semaine_debut;