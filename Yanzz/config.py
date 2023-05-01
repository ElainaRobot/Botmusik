class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 21514379
    API_HASH = "74d2ed4a390441cc56f66daed5bfe8c4"
    CASH_API_KEY = "ogZ49lgly7KXyiX"  # ketik get /cashapi di @YanzzSupportt
    DATABASE_URL = ""  # ketik get /sql di @YanzzSupportt
    EVENT_LOGS = ()  # ketik get /eventlogs di @YanzzSupportt
    MONGO_DB_URI = ""   # ketik get /mongo di @YanzzSupportt
    # Tautan telegraph dari gambar yang akan ditampilkan pada perintah mulai.
    START_IMG = "https://telegra.ph/file/51c8712f990fd5ab751b8.jpg"
    SUPPORT_CHAT = "ElainaManagerSupport"  # Grup Untuk Dukungan kalian
    TOKEN = "6208942065:AAGx-r9ApBDQ0QT6RXGpHRqQmlQ0rQRtIdg"  # ketik get /tokenbot di @YanzzSupportt
    TIME_API_KEY = "ogZ49lgly7KXyiX"  # ketik get /timeapi di @YanzzSupportt
    OWNER_ID = 6029970020  # User id kamu/owner

    # Kolom opsional
    BL_CHATS = []  # Daftar grup yang ingin Anda daftar hitam.
    DRAGONS = []  # ID pengguna dari pengguna sudo
    DEV_USERS = []  # ID pengguna dari pengguna dev
    DEMONS = []  # ID pengguna dari pengguna pendukung
    TIGERS = []  # ID pengguna pengguna harimau
    WOLVES = []  # ID pengguna dari pengguna daftar putih

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
