import time
import logging
from watchdog.observers import Observer
from src.config.get_smb_config import GetSmbConfig
from src.watchers.handler import WatcherHandler


class Observer:

    def __init__(self) -> None:
        self.__event_handler = WatcherHandler()
        self.__smb_config = GetSmbConfig()

    def start(self) -> None:
        logging.info("Initializing Observer")
        observer = Observer()
        observer.schedule(self.__event_handler,
                          self.__smb_config.smb_folder_to_watch, recursive=True)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
