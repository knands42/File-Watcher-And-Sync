from smb.SMBConnection import SMBConnection

from src.config.get_smb_config import GetSmbConfig


class GetSmbConnections():
    def __init__(self) -> None:
        self.__config = GetSmbConfig()
        self.operations = None

    def connect(self) -> None:
        self.operations = SMBConnection(username=self.__config.smb_username,
                                        password=self.__config.smb_password,
                                        my_name=self.__config.smb_client_machine_name,
                                        remote_name=self.__config.smb_server_machine_name,
                                        domain=self.__config.smb_domain_name,
                                        use_ntlm_v2=True,
                                        is_direct_tcp=True)

        self.operations.connect(
            self.__config.smb_server_ip, self.__config.smb_port)

    def close(self) -> None:
        if self.operations is not None:
            self.operations.close()
