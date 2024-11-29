import json
import subprocess
from collections import namedtuple
from processing.enumerations import LevelCritic as LVL


def getToken(objet) -> str:
    url = "https://api.insee.fr/token"
    auth_header = "Authorization: Basic VGY2YlNQWklBWkZ6RUVpTTJsT0JmS0RvcFpJYTpQdEVKYnlINkFteFlIbTZCVUxadWNSRE1vXzBh"
    data = "grant_type=client_credentials"

    curl_command = [
        "curl", "-k", "-d", data, "-H", auth_header, url
    ]

    result = subprocess.run(curl_command, capture_output=True, text=True)

    # Utilisation de json.loads pour analyser la réponse
    try:
        response_data = json.loads(result.stdout)
        token = response_data.get("access_token")
        return token
    except json.JSONDecodeError as err:
        objet.maindialog.show_notification(
            "Erreur lors de la récupération du token.",
            LVL.warning,
        )
        return None

def getInfoEtablissement(objet,  siret: str):
    token: str = getToken(objet)
    # Champs du namedtuple
    fields = ["entreprise", "respNom", "respPrenom", "adresse", "commune", "ville", "cp", "siret", "siren", "ape"]
    NT_Entreprise = namedtuple("InformationEntreprise", fields)

    if token:
        # URL de l'API (comme dans votre code précédent)
        url = f"https://api.insee.fr/entreprises/sirene/V3.11/siret/{siret}"

        # En-têtes dynamiques
        accept_header = "Accept: application/json"
        auth_header = f"Authorization: Bearer {token}"

        # Commande curl pour obtenir les données
        curl_command = [
            "curl", "-X", "GET", "-H", accept_header, "-H", auth_header, url
        ]

        result = subprocess.run(curl_command, capture_output=True, text=True)

        try:
            data = json.loads(result.stdout)
        except json.JSONDecodeError:
            objet.maindialog.show_notification(
                "Erreur lors de la récupération des données de l'établissement.",
                LVL.warning,
            )
            return None, 0  # Retourne None et 0 si la requête échoue

        if data.get("header", {}).get("statut") == 200:
            etablissement = data.get("etablissement", {})
            adresseInfo = etablissement.get("adresseEtablissement", {})
            etablissementLabel = etablissement.get("periodesEtablissement")[0]

            values = [
                etablissementLabel.get("enseigne1Etablissement"),  # entreprise
                etablissement.get("uniteLegale", {}).get("nomUniteLegale"),  # respNom
                etablissement.get("uniteLegale", {}).get("prenom1UniteLegale"),  # respPrenom
                f"{adresseInfo.get('numeroVoieEtablissement', '')} {adresseInfo.get('typeVoieEtablissement', '')} {adresseInfo.get('libelleVoieEtablissement', '')}".strip(),  # adresse
                adresseInfo.get('libelleCommuneEtablissement'),  # commune
                adresseInfo.get('complementAdresseEtablissement'),  # ville
                adresseInfo.get('codePostalEtablissement'),  # cp
                etablissement.get("siret"),  # siret
                etablissement.get("siren"),  # siren
                etablissement.get("uniteLegale", {}).get("activitePrincipaleUniteLegale", "").replace(".", "")  # ape
            ]

            nt_instance = NT_Entreprise(*values)

            # Calcul de la longueur des champs vides
            empty_count = sum(1 for value in values if not value)
            empty_count = empty_count == len(fields)

            return nt_instance, empty_count
        else:
            # Retourne un namedtuple avec des champs vides
            nt_instance = NT_Entreprise(*([None] * len(fields)))
            return nt_instance, True
    else:
        # Retourne un namedtuple avec des champs vides
        nt_instance = NT_Entreprise(*([None] * len(fields)))
        return nt_instance, True