import logging
from watchdog.observers import Observer as WatchdogObserver
from src.config.get_smb_config import GetSmbConfig
from src.watchers.handler import WatcherHandler


class Observer:

    def __init__(self) -> None:
        self.__event_handler = WatcherHandler()
        self.__smb_config = GetSmbConfig()

    def start(self):
        logging.info("Initializing Observer")
        observer = WatchdogObserver()
        observer.schedule(self.__event_handler,
                          self.__smb_config.smb_folder_to_watch, recursive=True)
        return observer
