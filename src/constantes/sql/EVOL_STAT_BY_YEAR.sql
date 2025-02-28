with achat as
  (SELECT annee.annee,
          COALESCE(SUM(achat.prix), 0) AS achat
    FROM
      (SELECT date_part('year', CURRENT_DATE)::integer - 3 AS annee
      UNION SELECT date_part('year', CURRENT_DATE)::integer - 2 AS annee
      UNION SELECT date_part('year', CURRENT_DATE)::integer - 1 AS annee
      UNION SELECT date_part('year', CURRENT_DATE)::integer AS annee) AS annee
    LEFT JOIN activites.achat AS achat ON date_part('year', achat.crea_date) = annee.annee
    GROUP BY annee.annee
    ORDER BY annee.annee),
  facture as
  (SELECT annee.annee,
          COALESCE(SUM(factures.prix_ttc), 0) AS facture
    FROM
      (SELECT date_part('year', CURRENT_DATE)::integer - 3 AS annee
      UNION SELECT date_part('year', CURRENT_DATE)::integer - 2 AS annee
      UNION SELECT date_part('year', CURRENT_DATE)::integer - 1 AS annee
      UNION SELECT date_part('year', CURRENT_DATE)::integer AS annee) AS annee
    LEFT JOIN
     (SELECT *
      FROM activites.factures
      WHERE factures.paye is true) AS factures ON date_part('year', factures.crea_date) = annee.annee
    GROUP BY annee.annee
    ORDER BY annee.annee)

SELECT a.annee "années", f.facture - a.achat "Bénéfice"
FROM achat a
LEFT JOIN facture f ON f.annee = a.annee