from bot_api import Bot
from bot_api import BotInfo

class PySample(Bot):
    def __init__(self, botInfo: BotInfo) -> None:
        super().__init__(botInfo)

if __name__ == "__main__":
    bot = PySample(BotInfo.from_file("./PySample.json"))
    bot.start()
