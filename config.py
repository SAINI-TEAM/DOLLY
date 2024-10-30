from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "12380656"))
API_HASH = getenv("API_HASH", "d927c13beaaf5110f25c505b7c071273")
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_ID = int(getenv("OWNER_ID", "7673640235"))
MONGO_URL = getenv("MONGO_URL", None)
SUPPORT_GRP = getenv("SUPPORT_GRP", "quizbysu")
UPDATE_CHNL = getenv("UPDATE_CHNL", "quizbys")
MUSIC = getenv("MUSIC", "musu_musicbot")
REPO = getenv("REPO", " https://github.com/SAINI-TEAM/DOLLY")
OWNER_USERNAME = getenv("OWNER_USERNAME", "attitude_boy91")

# Random Start Images
IMG = [
    "https://files.catbox.moe/3rga8l.jpg",
    "https://files.catbox.moe/tr8qch.jpg",
    "https://files.catbox.moe/lssvia.jpg",
    "https://files.catbox.moe/0nvt5r.jpg",
    "https://files.catbox.moe/3ko9qj.jpg",
    "https://files.catbox.moe/rl6nfu.jpg",
    "https://files.catbox.moe/nkz33j.jpg",
    "https://files.catbox.moe/iebw30.jpg",
    "https://files.catbox.moe/zf88cw.jpg",
    "https://files.catbox.moe/3rga8l.jpg",
    "https://files.catbox.moe/tr8qch.jpg",
    "https://files.catbox.moe/lssvia.jpg",
    "https://files.catbox.moe/0nvt5r.jpg",
    "https://files.catbox.moe/3ko9qj.jpg",
    "https://files.catbox.moe/rl6nfu.jpg",
    "https://files.catbox.moe/nkz33j.jpg",
]


# Random Stickers
STICKER = [
    "CAACAgUAAxkBAAKjMmcXK375DGZR2n-0TzIoVKWf7d3BAAJBEQAC0mr5V-K7OoRxykvDHgQ",
    "CAACAgUAAxkBAAKjMWcXK3Upzn2i9hfBumg2pJswfZzuAALmEAAC0jnwV_PAgENbv5PGHgQ",
    "CAACAgUAAxkBAAKjMGcXK2wKMM5knt3peJszujeK903BAAIqEgACElr5VwOSLsmyHxQ7HgQ",
]


EMOJIOS = [
    "🎲",
    "🔥",
    "⚡️",
    "⛈",
    "🌩",
    "🌦",
    "☀️",
    "💫",
    "🐳",
    "🦑",
]
