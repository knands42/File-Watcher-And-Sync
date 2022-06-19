from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()

    from src.config.logging import LoggingHandler
    from src.watchers.main import Observer

    LoggingHandler()
    Observer()
