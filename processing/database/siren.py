import json
import subprocess
from collections import namedtuple
from processing.enumerations import LevelCritic as LVL


def getDepartementByCommuneName(commune: str) -> str:
    # Commande curl en tant que liste d'arguments
    command = [
        "curl",
        "https://geo.api.gouv.fr/communes",
        "-G",  # Pour indiquer que c'est une requête GET
        "--data-urlencode", f"nom={commune}",
        "--data-urlencode", "fields=departement",
        "--data-urlencode", "boost=population",
        "--data-urlencode", "limit=5"
    ]

    # Exécute la commande et capture la sortie
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        response_data = eval(result.stdout)
        if len(response_data)>0:
            name = response_data[0].get("departement", {}).get("nom")
        else:
            name = None
    except subprocess.CalledProcessError as e:
        name = None
    return name

def getToken() -> str:
    return "155a471d-7c08-41c9-9a47-1d7c08a1c9b2"

def getInfoEtablissement(objet,  siret: str):
    token: str = getToken()
    # Champs du namedtuple
    fields = ["entreprise", "respNom", "respPrenom", "adresse", "commune", "ville", "cp", "siret", "siren", "ape", "departement"]
    NT_Entreprise = namedtuple("InformationEntreprise", fields)

    if token:
        # URL de l'API
        url = f"https://api.insee.fr/api-sirene/3.11/siret/{siret}"

        # En-têtes dynamiques
        accept_header = "Accept: application/json"
        auth_header = f"X-INSEE-Api-Key-Integration: {token}"

        # Commande curl pour obtenir les données
        curl_command = [
            "curl", "-X", "GET", "-H", accept_header, "-H", auth_header, url
        ]

        result = subprocess.run(curl_command, capture_output=True, text=True)

        try:
            data = json.loads(result.stdout)
        except json.JSONDecodeError:
            print("erreur 1")
            # objet.maindialog.show_notification(
            #     "Erreur lors de la récupération des données de l'établissement.",
            #     LVL.warning,
            # )
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
                etablissement.get("uniteLegale", {}).get("activitePrincipaleUniteLegale", "").replace(".", ""),  # ape
                getDepartementByCommuneName(adresseInfo.get('libelleCommuneEtablissement'))
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