from dataclasses import dataclass
import os


@dataclass
class GetSmbConfig:
    smb_port: int = int(os.getenv('smb_port'))
    smb_username: str = os.getenv('smb_username')
    smb_password: str = os.getenv('smb_password')
    smb_client_machine_name: str = os.getenv('smb_client_machine_name')
    smb_server_machine_name: str = os.getenv('smb_server_machine_name')
    smb_server_ip: str = os.getenv('smb_server_ip')
    smb_domain_name: str = os.getenv('smb_domain_name')
    smb_folder_to_watch: str = os.getenv('smb_folder_to_watch')
    smb_remote_folder_share_to_watch: str = os.getenv(
        'smb_remote_folder_share_to_watch')
    smb_remote_folder_to_persist: str = os.getenv(
        'smb_remote_folder_to_persist')
