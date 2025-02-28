SET lc_time to 'fr_FR.UTF-8';
WITH achat_mois AS (
    SELECT mois.mois_debut, mois.mois_fin,
           COALESCE(SUM(achat.prix), 0) AS achat
    FROM (
        -- Définition des 3 derniers mois
		SELECT 
            date_trunc('month', CURRENT_DATE - INTERVAL '3 months')::date AS mois_debut,
            (date_trunc('month', CURRENT_DATE - INTERVAL '3 months') + INTERVAL '1 month - 1 day')::date AS mois_fin
        UNION
        SELECT 
            date_trunc('month', CURRENT_DATE - INTERVAL '2 months')::date AS mois_debut,
            (date_trunc('month', CURRENT_DATE - INTERVAL '2 months') + INTERVAL '1 month - 1 day')::date AS mois_fin
        UNION
        SELECT 
            date_trunc('month', CURRENT_DATE - INTERVAL '1 month')::date AS mois_debut,
            (date_trunc('month', CURRENT_DATE - INTERVAL '1 month') + INTERVAL '1 month - 1 day')::date AS mois_fin
        UNION
        SELECT 
            date_trunc('month', CURRENT_DATE)::date AS mois_debut,
            (date_trunc('month', CURRENT_DATE) + INTERVAL '1 month - 1 day')::date AS mois_fin
    ) AS mois
    LEFT JOIN activites.achat AS achat 
        ON achat.crea_date >= mois.mois_debut AND achat.crea_date <= mois.mois_fin
    GROUP BY mois.mois_debut, mois.mois_fin
    ORDER BY mois.mois_debut
),
facture_mois AS (
    SELECT mois.mois_debut, mois.mois_fin,
           COALESCE(SUM(factures.prix_ttc), 0) AS facture
    FROM (
        -- Définition des 3 derniers mois
		SELECT 
            date_trunc('month', CURRENT_DATE - INTERVAL '3 months')::date AS mois_debut,
            (date_trunc('month', CURRENT_DATE - INTERVAL '3 months') + INTERVAL '1 month - 1 day')::date AS mois_fin
        UNION
        SELECT 
            date_trunc('month', CURRENT_DATE - INTERVAL '2 months')::date AS mois_debut,
            (date_trunc('month', CURRENT_DATE - INTERVAL '2 months') + INTERVAL '1 month - 1 day')::date AS mois_fin
        UNION
        SELECT 
            date_trunc('month', CURRENT_DATE - INTERVAL '1 month')::date AS mois_debut,
            (date_trunc('month', CURRENT_DATE - INTERVAL '1 month') + INTERVAL '1 month - 1 day')::date AS mois_fin
        UNION
        SELECT 
            date_trunc('month', CURRENT_DATE)::date AS mois_debut,
            (date_trunc('month', CURRENT_DATE) + INTERVAL '1 month - 1 day')::date AS mois_fin
    ) AS mois
    LEFT JOIN (
        SELECT *
        FROM activites.factures
        WHERE factures.paye IS true
    ) AS factures 
        ON factures.crea_date >= mois.mois_debut AND factures.crea_date <= mois.mois_fin
    GROUP BY mois.mois_debut, mois.mois_fin
    ORDER BY mois.mois_debut
)

SELECT 
    to_char(a.mois_debut, 'TMMonth') AS mois,
    f.facture - a.achat "Bénéfice" 
FROM achat_mois a
LEFT JOIN facture_mois f ON f.mois_debut = a.mois_debut;