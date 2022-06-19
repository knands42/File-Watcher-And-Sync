import time
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()

    from src.config.logging import LoggingHandler
    from src.watchers.main import Observer

    LoggingHandler()
    observer = Observer()
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
