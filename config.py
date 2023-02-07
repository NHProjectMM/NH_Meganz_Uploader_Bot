import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5642205991:AAHSDm18TDYgmHAhj03NTqhA8KiuyaIAvF8")
    APP_ID = int(os.environ.get("APP_ID", 7978114))
    API_HASH = os.environ.get("API_HASH", "5f7839feeba133497f24acfd005ef2ec")
    Mega_email = os.environ.get("Mega_email", "ngahtut.kho@gmail.com")
    Mega_password = os.environ.get("Mega_password", "505953KhoPep$")
    Bot_username = os.environ.get("Bot_username", "NHMega_Bot")
    OWNER_ID = os.environ.get("OWNER_ID", "1760280598")
    REDIS_URI = os.environ.get("REDIS_URI", "http://redis-12663.c1.asia-northeast1-1.gce.cloud.redislabs.com:12663")
    REDIS_PASS = os.environ.get("REDIS_PASS", "MQ4wMqmWpLduKCCXpKd0bHiGxkOtgiv2")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1760280598").split())
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    ADMIN_LOCATION = "./ADOWNLOADS"
    CREDENTIALS_LOCATION = "./CREDENTIALS" 
