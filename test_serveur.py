# Informations de connexion
hostname = '85.215.137.38'
username = 'root'
password = 'sGy1EcNV'
local_path = '/Users/abdelhafidhousoufou/PycharmProjects/DevisCreator_premium/forms/background/sada_mont_choungui.png'
remote_path = '/root/Documents/sada_mont_choungui.png'  # Chemin complet
port = 22


from ftplib import FTP



ftp = FTP(timeout=30)
ftp.connect(host= hostname, port=port)
ftp.login(user=username, passwd=password)

ftp.quit()
print("success")