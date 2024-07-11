# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "23476439"))
API_HASH = getenv("API_HASH", "1626e884119a29dbccbb78e39b48128f")
BOT_TOKEN = getenv("BOT_TOKEN", " ")
OWNER_ID = int(getenv("OWNER_ID", "5993556795"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://qwerty1234:@cluster0.onmws2a.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002175816545"))
FORCESUB = getenv("FORCESUB", "savachachaji")
