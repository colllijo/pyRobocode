from internals import BotInternals
from . import BotInfo

class Bot:
    def __init__(self, bot_info: BotInfo, server_url: str = "", server_secret: str = "") -> None:
        self.internals = BotInternals(self, bot_info, server_url, server_secret)

    def start(self) -> None:
        self.internals.start()

    def on_connected(self, event) -> None:
        print("connected")

    def on_disconnected(self, event) -> None:
        print("disconnected")

    def on_connection_error(self, event) -> None:
        print("connection error")
