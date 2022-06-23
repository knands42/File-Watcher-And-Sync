import logging
import time

from dotenv import load_dotenv

from src.config.logging import LoggingHandler

if __name__ == "__main__":
    load_dotenv()

    from src.config.get_smb_config import GetSmbConfig
    from src.watchers.handler import WatcherHandler
    from watchdog.observers import Observer

    LoggingHandler()
    logging.info("Initializing Observer")
    observer = Observer()
    path = GetSmbConfig().smb_folder_to_watch
    observer.schedule(event_handler=WatcherHandler(), path=path,
                      recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

