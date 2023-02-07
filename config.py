import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
    APP_ID = int(os.environ.get("APP_ID", 123456))
    API_HASH = os.environ.get("API_HASH", "")
    Mega_email = os.environ.get("Mega_email", "")
    Mega_password = os.environ.get("Mega_password", "")
    Bot_username = os.environ.get("Bot_username", "")
    OWNER_ID = os.environ.get("OWNER_ID", "")
    REDIS_URI = os.environ.get("REDIS_URI", "")
    REDIS_PASS = os.environ.get("REDIS_PASS", "")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    ADMIN_LOCATION = "./ADOWNLOADS"
    CREDENTIALS_LOCATION = "./CREDENTIALS" 
