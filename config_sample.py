import os
import json

# REQUIRED CONFIG
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
OWNER_ID = int(os.getenv("OWNER_ID", 0))
TELEGRAM_API = int(os.getenv("TELEGRAM_API", 0))
TELEGRAM_HASH = os.getenv("TELEGRAM_HASH", "")

# OPTIONAL CONFIG
TG_PROXY = json.loads(os.getenv("TG_PROXY", "{}"))  # Parse as JSON if set
USER_SESSION_STRING = os.getenv("USER_SESSION_STRING", "")
CMD_SUFFIX = os.getenv("CMD_SUFFIX", "")
AUTHORIZED_CHATS = os.getenv("AUTHORIZED_CHATS", "")
SUDO_USERS = os.getenv("SUDO_USERS", "")
DATABASE_URL = os.getenv("DATABASE_URL", "")
STATUS_LIMIT = int(os.getenv("STATUS_LIMIT", 4))
DEFAULT_UPLOAD = os.getenv("DEFAULT_UPLOAD", "rc")
STATUS_UPDATE_INTERVAL = int(os.getenv("STATUS_UPDATE_INTERVAL", 15))
FILELION_API = os.getenv("FILELION_API", "")
STREAMWISH_API = os.getenv("STREAMWISH_API", "")
EXCLUDED_EXTENSIONS = os.getenv("EXCLUDED_EXTENSIONS", "")
INCOMPLETE_TASK_NOTIFIER = os.getenv("INCOMPLETE_TASK_NOTIFIER", "False").lower() == "true"
YT_DLP_OPTIONS = os.getenv("YT_DLP_OPTIONS", "")
USE_SERVICE_ACCOUNTS = os.getenv("USE_SERVICE_ACCOUNTS", "False").lower() == "true"
NAME_SUBSTITUTE = os.getenv("NAME_SUBSTITUTE", "")
FFMPEG_CMDS = json.loads(os.getenv("FFMPEG_CMDS", "{}"))
UPLOAD_PATHS = json.loads(os.getenv("UPLOAD_PATHS", "{}"))

# GDrive Tools
GDRIVE_ID = os.getenv("GDRIVE_ID", "")
IS_TEAM_DRIVE = os.getenv("IS_TEAM_DRIVE", "False").lower() == "true"
STOP_DUPLICATE = os.getenv("STOP_DUPLICATE", "False").lower() == "true"
INDEX_URL = os.getenv("INDEX_URL", "")

# Rclone
RCLONE_PATH = os.getenv("RCLONE_PATH", "")
RCLONE_FLAGS = os.getenv("RCLONE_FLAGS", "")
RCLONE_SERVE_URL = os.getenv("RCLONE_SERVE_URL", "")
RCLONE_SERVE_PORT = int(os.getenv("RCLONE_SERVE_PORT", 0))
RCLONE_SERVE_USER = os.getenv("RCLONE_SERVE_USER", "")
RCLONE_SERVE_PASS = os.getenv("RCLONE_SERVE_PASS", "")

# JDownloader
JD_EMAIL = os.getenv("JD_EMAIL", "")
JD_PASS = os.getenv("JD_PASS", "")

# Sabnzbd
USENET_SERVERS = json.loads(os.getenv("USENET_SERVERS", '[{"name": "main", "host": "", "port": 563, "timeout": 60, "username": "", "password": "", "connections": 8, "ssl": 1, "ssl_verify": 2, "ssl_ciphers": "", "enable": 1, "required": 0, "optional": 0, "retention": 0, "send_group": 0, "priority": 0}]'))

# Update
UPSTREAM_REPO = os.getenv("UPSTREAM_REPO", "")
UPSTREAM_BRANCH = os.getenv("UPSTREAM_BRANCH", "master")

# Leech
LEECH_SPLIT_SIZE = int(os.getenv("LEECH_SPLIT_SIZE", 0))
AS_DOCUMENT = os.getenv("AS_DOCUMENT", "False").lower() == "true"
EQUAL_SPLITS = os.getenv("EQUAL_SPLITS", "False").lower() == "true"
MEDIA_GROUP = os.getenv("MEDIA_GROUP", "False").lower() == "true"
USER_TRANSMISSION = os.getenv("USER_TRANSMISSION", "False").lower() == "true"
HYBRID_LEECH = os.getenv("HYBRID_LEECH", "False").lower() == "true"
LEECH_FILENAME_PREFIX = os.getenv("LEECH_FILENAME_PREFIX", "")
LEECH_DUMP_CHAT = os.getenv("LEECH_DUMP_CHAT", "")
THUMBNAIL_LAYOUT = os.getenv("THUMBNAIL_LAYOUT", "")

# qBittorrent/Aria2c
TORRENT_TIMEOUT = int(os.getenv("TORRENT_TIMEOUT", 0))
BASE_URL = os.getenv("BASE_URL", "")
BASE_URL_PORT = int(os.getenv("BASE_URL_PORT", 0))
WEB_PINCODE = os.getenv("WEB_PINCODE", "False").lower() == "true"

# Queueing system
QUEUE_ALL = int(os.getenv("QUEUE_ALL", 0))
QUEUE_DOWNLOAD = int(os.getenv("QUEUE_DOWNLOAD", 0))
QUEUE_UPLOAD = int(os.getenv("QUEUE_UPLOAD", 0))

# RSS
RSS_DELAY = int(os.getenv("RSS_DELAY", 600))
RSS_CHAT = os.getenv("RSS_CHAT", "")
RSS_SIZE_LIMIT = int(os.getenv("RSS_SIZE_LIMIT", 0))

# Torrent Search
SEARCH_API_LINK = os.getenv("SEARCH_API_LINK", "")
SEARCH_LIMIT = int(os.getenv("SEARCH_LIMIT", 0))
SEARCH_PLUGINS = json.loads(os.getenv("SEARCH_PLUGINS", '[]'))  # Expecting a JSON array

# Debugging
if __name__ == "__main__":
    print(f"BOT_TOKEN: {BOT_TOKEN}")
    print(f"OWNER_ID: {OWNER_ID}")
    print(f"TELEGRAM_API: {TELEGRAM_API}")
    print(f"TELEGRAM_HASH: {TELEGRAM_HASH}")
