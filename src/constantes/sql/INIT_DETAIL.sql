DROP VIEW IF EXISTS activites.details;
SET lc_time to 'fr_FR.UTF-8';
CREATE VIEW activites.details AS(
SELECT replace(replace(a.activites::text, 'factures_'::text, ''::text), 'devis_'::text, ''::text) AS "activités",
a.action,
(u.nom::text || ' '::text) || u.prenom::text AS "créateur",
COALESCE('Quantité : '::text || i.quantite, 
((('Client : '::text || d.client::text) || ' / Budget : '::text) || round(a.budget::numeric, 2)) || ' €'::text, 
((('Client : '::text || f.client::text) || ' / Budget : '::text) || round(a.budget::numeric, 2)) || ' €'::text) AS description,
to_char(a.crea_date, 'DD TMMon. YYYY à HH24:MI:SS'::text) AS "date de création", f.client, a.budget
FROM activites.activites a
LEFT JOIN inventaires.inventaires i ON i.nom::text = a.activites::text
LEFT JOIN ( SELECT DISTINCT "left"(devis.numero_devis::text, 10) AS numero_devis,
                devis.client,
                devis.crea_user
        FROM activites.devis) d ON concat_ws('_'::text, 'devis', d.numero_devis) = a.activites::text
LEFT JOIN ( SELECT DISTINCT "left"(factures.numero_facture::text, 10) AS numero_devis,
                factures.client,
                factures.crea_user
        FROM activites.factures) f ON concat_ws('_'::text, 'factures', f.numero_devis) = a.activites::text
LEFT JOIN informations.utilisateurs u ON COALESCE(i.crea_user, d.crea_user, f.crea_user)::text = u.identifiant::text
)