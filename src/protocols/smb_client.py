import logging
import os

from src.config.get_smb_config import GetSmbConfig
from src.config.get_smb_connection import GetSmbConnections


class SmbClient:
    def __init__(self) -> None:
        self.__smb_client = GetSmbConnections()
        self.__operations = self.__get_connection()
        self.__config = GetSmbConfig()

    def persist(self, file_path: str) -> None:
        try:
            with open(file_path, 'rb') as f:
                file_path_to_persist = os.path.join(self.__config.smb_remote_folder_to_persist,
                                                    os.path.basename(file_path))
                self.__get_connection().storeFile(self.__config.smb_remote_folder_share_to_watch,
                                                  file_path_to_persist, f)
        except Exception as ex:
            logging.error('Fail to persist: ', ex)
        finally:
            self.__close_connection()

    def delete_recursively(self, file_path: str):
        # self.__operations.deleteFiles(self.__shared_folder, "test/*")
        pass

    def __get_connection(self):
        self.__smb_client.connect()
        return self.__smb_client.operations

    def __close_connection(self):
        self.__smb_client.close()
