DROP VIEW IF EXISTS activites.details;
SET lc_time to 'fr_FR.UTF-8';
CREATE VIEW activites.details AS(
SELECT replace(replace(a.activites, 'factures_',''),'devis_','') "activités",
       a.action,  u.nom || ' ' || u.prenom "créateur",
       COALESCE('Quantité : '||i.quantite,
                'Client : '|| d.client || ' / Budget : ' || ROUND(a.budget::NUMERIC, 2) || ' €',
                'Client : '|| f.client || ' / Budget : ' || ROUND(a.budget::NUMERIC, 2) || ' €') "description",
       TO_CHAR(a.crea_date, 'DD TMMon. YYYY à HH24:MI:SS') "date de création"
FROM activites.activites a
LEFT JOIN inventaires.inventaires i ON i.nom = a.activites
LEFT JOIN (SELECT DISTINCT LEFT(numero_devis,10) numero_devis, client, crea_user FROM activites.devis) d
        ON CONCAT_WS('_', 'devis', d.numero_devis) = a.activites
LEFT JOIN (SELECT DISTINCT LEFT(numero_facture,10) numero_devis, client, crea_user FROM activites.factures) f
        ON CONCAT_WS('_', 'facture', f.numero_devis) = a.activites
LEFT JOIN informations.utilisateurs u ON COALESCE(i.crea_user, d.crea_user, f.crea_user) = u.identifiant)