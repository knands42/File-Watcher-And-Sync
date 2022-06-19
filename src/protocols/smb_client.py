from src.config.get_smb_config import GetSmbConfig
from src.config.get_smb_connection import GetSmbConnections


class SmbClient:
    def __init__(self) -> None:
        self.__smb_client = GetSmbConnections()
        self.__operations = self.__get_connection()
        self.__config = GetSmbConfig()

    def persist(self) -> None:
        try:
            # self.__operations.storeFile(self.__shared_folder, "test")
            pass
        except Exception as ex:
            print('Fail to persist: ', ex)
        finally:
            self.__close_connection()

    def delete_recursively(self):
        # self.__operations.deleteFiles(self.__shared_folder, "test/*")
        pass

    def __get_connection(self):
        self.__smb_client.connect()
        return self.__smb_client.operations

    def __close_connection(self):
        self.__smb_client.close()
