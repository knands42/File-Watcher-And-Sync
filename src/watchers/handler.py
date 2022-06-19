import logging

from watchdog.events import FileSystemEventHandler

from src.protocols.smb_client import SmbClient


class WatcherHandler(FileSystemEventHandler):
    def __init__(self) -> None:
        super().__init__()
        self.sender = SmbClient()

    def on_modified(self, event):
        self.__synchronize_creation_modification_with_remote_server(event)

    def on_created(self,  event):
        self.__synchronize_creation_modification_with_remote_server(event)

    def on_deleted(self,  event):
        self.__synchronize_deletion_with_remote_server(event)

    def __synchronize_creation_modification_with_remote_server(self, event):
        logging.info(
            f"event type: {event.event_type} - path: {event.src_path}")
        self.sender.persist()

    def __synchronize_deletion_with_remote_server(self, event):
        logging.info(
            f"event type: {event.event_type} - path: {event.src_path}")
        self.sender.delete_recursively()
