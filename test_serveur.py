import paramiko
import os

# Informations de connexion
hostname = '85.215.137.38'
username = 'root'
password = 'qQFU47eI'  # Ou utilisez une clé SSH
local_path = '/Users/abdelhafidhousoufou/PycharmProjects/DevisCreator_premium/forms/background/sada_mont_choungui.png'
remote_path = '/chemin/distant/sur/serveur'

# Créer une connexion SSH
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Se connecter au serveur
    ssh.connect(hostname, username=username, password=password)

    # Créer un client SFTP
    sftp = ssh.open_sftp()

    # Copier le fichier
    sftp.put(local_path, remote_path)

    print("Fichier copié avec succès")

except Exception as e:
    print(f"Erreur de transfert : {e}")

finally:
    # Fermer les connexions
    sftp.close()
    ssh.close()