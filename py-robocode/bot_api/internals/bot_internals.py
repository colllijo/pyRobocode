import os

from bot_api.bot import Bot

class BotInternals:
    DEFAULT_SERVER_URL = "ws://localhost:7654"

    def __init__(self, bot: Bot, bot_info, server_url: str = str(), server_secret: str = str()) -> None:
        self.bot_info = bot_info
        self.server_url = server_url if server_url else self.get_server_url_from_env()
        self.server_secret = server_secret if server_secret else self.get_server_secret_from_env()

    def get_server_url_from_env(self) -> str:
        url = os.getenv("SERVER_URL")

        return url if url else self.DEFAULT_SERVER_URL

    def get_server_secret_from_env(self) -> str:
        secret = os.getenv("SERVER_SECRET")

        return secret if secret else str()

    def start(self) -> None:
        pass
