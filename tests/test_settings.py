# IRC settings
HOST = "test.example.com"
PORT = 6667
USE_SSL = False
PASSWORD = None
NICKNAME = "shesaidbot"
REALNAME = "bot: provides quotations from notable women"

CHANNEL = "#test"

# Trigger phrases, in lowercase
TRIGGERS = (
    "twss",
    )

# Process settings
PID_FILE = "./talkbackbot.pid"
LOG_FILE = "./talkbackbot.log"
QUOTES_FILE = "tests/test_quote.txt"