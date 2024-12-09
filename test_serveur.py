# Informations de connexion
hostname = '85.215.137.38'
username = 'root'
password = 'sGy1EcNV'
local_path = '/Users/abdelhafidhousoufou/PycharmProjects/DevisCreator_premium/forms/background/sada_mont_choungui.png'
remote_path = '/root/Documents/sada_mont_choungui.png'  # Chemin complet

import os
import subprocess
from ftplib import FTP
import paramiko
from typing import Optional, Union
from pathlib import Path


class FileUploader:
    """A unified class for handling file uploads to Linux servers using various protocols."""

    def __init__(self):
        self.last_error = None

    def upload_ftp(self, hostname: str, username: str, password: str,
                   local_file: Union[str, Path], remote_path: str) -> bool:
        """
        Upload a file using FTP protocol.

        Args:
            hostname: FTP server hostname
            username: FTP username
            password: FTP password
            local_file: Path to local file
            remote_path: Remote path where to upload the file

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            with FTP(hostname) as ftp:
                ftp.login(username, password)
                with open(local_file, 'rb') as file:
                    ftp.storbinary(f'STOR {remote_path}', file)
            print(f"Successfully uploaded {local_file} to {remote_path} via FTP")
            return True

        except Exception as e:
            self.last_error = str(e)
            print(f"FTP upload error: {str(e)}")
            return False

    def upload_sftp(self, hostname: str, username: str,
                    local_file: Union[str, Path], remote_path: str,
                    private_key_path: Optional[str] = None,
                    password: Optional[str] = None) -> bool:
        """
        Upload a file using SFTP protocol.

        Args:
            hostname: SSH server hostname
            username: SSH username
            local_file: Path to local file
            remote_path: Remote path where to upload the file
            private_key_path: Path to private key file (optional)
            password: Password for authentication (optional)

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            # Connect using either private key or password
            if private_key_path:
                private_key = paramiko.RSAKey.from_private_key_file(private_key_path)
                ssh.connect(hostname, username=username, pkey=private_key)
            elif password:
                ssh.connect(hostname, username=username, password=password)
            else:
                raise ValueError("Either private_key_path or password must be provided")

            # Upload file
            with ssh.open_sftp() as sftp:
                sftp.put(local_file, remote_path)

            ssh.close()
            print(f"Successfully uploaded {local_file} to {remote_path} via SFTP")
            return True

        except Exception as e:
            self.last_error = str(e)
            print(f"SFTP upload error: {str(e)}")
            return False

    def upload_scp(self, local_file: Union[str, Path], remote_user: str,
                   remote_host: str, remote_path: str) -> bool:
        """
        Upload a file using scp command.

        Args:
            local_file: Path to local file
            remote_user: Remote username
            remote_host: Remote hostname
            remote_path: Remote path where to upload the file

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            command = f'scp {local_file} {remote_user}@{remote_host}:{remote_path}'
            subprocess.run(command, shell=True, check=True)
            print(f"Successfully uploaded {local_file} to {remote_host}:{remote_path} via SCP")
            return True

        except subprocess.CalledProcessError as e:
            self.last_error = str(e)
            print(f"SCP upload error: {str(e)}")
            return False

    def get_last_error(self) -> Optional[str]:
        """Return the last error message if any."""
        return self.last_error


# Example usage:
if __name__ == "__main__":
    uploader = FileUploader()

    # Example FTP upload
    uploader.upload_ftp(
        hostname=hostname,
        username=username,
        password=password,
        local_file=local_path,
        remote_path=remote_path
    )

    # Example SFTP upload with private key
    # uploader.upload_sftp(
    #     hostname="server.example.com",
    #     username="user",
    #     local_file="local_file.txt",
    #     remote_path="/remote/path/file.txt",
    #     private_key_path="/path/to/private_key"
    # )

    # Example SFTP upload with password
    # uploader.upload_sftp(
    #     hostname="server.example.com",
    #     username="user",
    #     local_file="local_file.txt",
    #     remote_path="/remote/path/file.txt",
    #     password="pass"
    # )

    # Example SCP upload
    # uploader.upload_scp(
    #     local_file="local_file.txt",
    #     remote_user="user",
    #     remote_host="server.example.com",
    #     remote_path="/remote/path/file.txt"
    # )