# (c) @AbirHasan2005

import os
import heroku3


class Config(object):
    # Get This From @TeleORG_Bot
    API_ID = int(os.environ.get("27432531"))
    API_HASH = os.environ.get("30781ab9f9fbbcd7711e59b6972cafe3")
    # Get This From @StringSessionGen_Bot
    STRING_SESSION = os.environ.get("BQBGK_oNhnR6OsjvOjjPuE1JnFFLnvLV2-wJb76CvkQvOPXXTmdGtOdknmKrFHciqRcDZAWpnsId7jQkPr5MdbaP0dPdeNPHSunSvMlX0rdJAfssxwEdrefdw4rzlxZgCKg1YLPcPYwRIf5a3n_jo-zW2on8RhPGDvQSXL635_PEOP_nMLNiS4AdQrp0Krr6broIvmimop0WrJ8B5vg8NwenGlrc9cHRNjGVlnd0btAhHjmDxAQkIpRtkDfmlXHoF0jpNvejaouMjEd36GtTESJrISEQ_gd7HMq-G9tFujachxpz7sWOkszyl2p54ZT6Ptyv2Uk3kV4LUUZqfxkvPfvVAAAAAVyOcZ0A")
    # Forward From Chat ID
    FORWARD_FROM_CHAT_ID = list(set(int(x) for x in os.environ.get("FORWARD_FROM_CHAT_ID", "-1001801147332").split()))
    # Forward To Chat ID
    FORWARD_TO_CHAT_ID = list(set(int(x) for x in os.environ.get("FORWARD_TO_CHAT_ID", "-1001897417356").split()))
    # Filters for Forwards
    DEFAULT_FILTERS = "video document photo audio text gif forwarded poll sticker"
    FORWARD_FILTERS = list(set(x for x in os.environ.get("FORWARD_FILTERS", DEFAULT_FILTERS).split()))
    BLOCKED_EXTENSIONS = list(set(x for x in os.environ.get("BLOCKED_EXTENSIONS", "").split()))
    MINIMUM_FILE_SIZE = os.environ.get("MINIMUM_FILE_SIZE", None)
    BLOCK_FILES_WITHOUT_EXTENSIONS = bool(os.environ.get("BLOCK_FILES_WITHOUT_EXTENSIONS", False))
    # Forward as Copy. Value Should be True or False
    FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
    # Sleep Time while Kang
    SLEEP_TIME = int(os.environ.get("SLEEP_TIME", 10))
    # Heroku Management
    HEROKU_API_KEY = os.environ.get("bf899ee8-c46d-4f1d-8ad3-eabc7e32b13c")
    HEROKU_APP_NAME = os.environ.get("mahalla-yetakchi")
    HEROKU_APP = heroku3.from_key(HEROKU_API_KEY).apps()[HEROKU_APP_NAME] if HEROKU_API_KEY and HEROKU_APP_NAME else None
    # Message Texts
    HELP_TEXT = """
This UserBot can forward messages from any Chat to any other Chat also you can kang all messages from one Chat to another Chat.

👨🏻‍💻 **Commands:**
• `!start` - Check UserBot Alive or Not.
• `!help` - Get this Message.
• `!kang` - Start All Messages Kanger.
• `!restart` - Restart Heroku App Dyno Workers.
• `!stop` - Stop Kanger & Restart Service.

©️ **Developer:** @AbirHasan2005
👥 **Support Group:** [【★ʟя★】](https://t.me/JoinOT)"""
