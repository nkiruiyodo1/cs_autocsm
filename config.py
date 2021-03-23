import os

# Storage Path

LOGS_PATH = os.getenv(
    "LOGS_PATH", os.path.join(os.path.dirname(os.path.realpath(__file__)), "logs/sdk.logs")
)

RESOURCE_PATH = os.getenv(
    "RESOURCE_PATH", os.path.join(os.path.dirname(os.path.realpath(__file__)), "resource/")
)

# ZOHO MUST API Keys
ZOHO_CLIENT_ID = os.getenv("ZOHO_CLIENT_ID", "1000.GZHO5NGZL1HZEAT5GABPLFO0EEXWCY")
ZOHO_CLIENT_SECRET = os.getenv(
    "ZOHO_CLIENT_SECRET", "16f59311502a8c70ac196ad61948478917a661b7ef"
)
ZOHO_REDIRECT_URI = os.getenv("ZOHO_REDIRECT_URI", "https://example.com")


STORAGE_PATH = os.getenv(
    "STORAGE_PATH", os.path.join(os.path.dirname(os.path.realpath(__file__)),"storage")
)

# ZOHO OPTIONAL API Keys

ZOHO_ACCOUNTS_URL = os.getenv("ZOHO_ACCOUNTS_URL", "https://accounts.zoho.com.cn")
ZOHO_API_BASE_URL = os.getenv("ZOHO_API_BASE_URL", "https://www.zohoapis.com.cn")
ZOHO_CURRENT_USER_EMAIL = os.getenv("ZOHO_CURRENT_USER_EMAIL", "alexolthoff@yodo1.com")
ZOHO_REDIRECT_URI = os.getenv("ZOHO_REDIRECT_URI", "https://example.com")


GRANT_TOKEN = os.getenv("GRANT_TOKEN","1000.55fb6090c8af98d3f78a0317204f6872.df993cccf208dbd3878ade6e89b9211b")
REFRESH_TOKEN = os.getenv("REFRESH_TOKEN","1000.fde2713d0603ec1a72ebf401c7d9c283.7b3958ed15ae3fa717a79a72cca8bad6")

# Mongo DB Config
DB_HOST = "dds-2zef2ffd23a67e541.mongodb.rds.aliyuncs.com"
DB_USERNAME = "dbviewer"
DB_PASSWORD = "C2#xaymsaiz"
DB_NAME = "adminportal"
DB_PORT = 3717

