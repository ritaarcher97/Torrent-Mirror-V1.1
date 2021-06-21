import sys

print("""
───────────────────────────────────────────────────────
 _____                           _     _   _     _   _ 
(___  )                         ( )   ( ) ( )   ( ) ( )
    | | _   _   ___     __     _| |   | |/'/'   | |_| |
 _  | |( ) ( )/' _ `\ /'__`\ /'_` |   | , <     |  _  |
( )_| || (_) || ( ) |(  ___/( (_| |   | |\`\    | | | |
`\___/'`\___/'(_) (_)`\____)`\__,_)   (_) (_)   (_) (_)
───────────────────────────────────────────────────────

Description : This python programme is for Ganerate config.env file for Telegram Files Mirroring bot

Repo : https://github.com/junedkh/Torrent-Mirror-V1.1
""")

I_am_new = input("Are you a new ?? (Y/n or hit enter) :- ")
if I_am_new.lower() == "n":
    iamnnew = False
else:
    iamnnew = True

if iamnnew is True:
    print("Buddy you are a new!")
    print("The telegram bot token that you get from @BotFather")

# Important
while True:
    BOT_TOKEN = input("(Require field) Enter your bot token :- ")
    if BOT_TOKEN == "":
        print("You Must Write BOT_TOKEN")
        continue
    break
if iamnnew is True:
    print("This is the folder ID of the Google Drive Folder to which you want to upload all the mirrors.")
while True:
    GDRIVE_FOLDER_ID = input("(Require field) Enter your Gdrive_Folder_id :- ")
    if GDRIVE_FOLDER_ID == "":
        print("You Must Write GDRIVE_FOLDER_ID")
        continue
    break
if iamnnew is True:
    print("The Telegram user ID (not username) of the owner of the bot")
while True:
    OWNER_ID = input("(Require field) Enter your OWNER_ID (TG id Numbers) :- ")
    if OWNER_ID == "":
        print("You Must Write OWNER_ID")
        continue
    if not OWNER_ID.isnumeric():
        print("OWNER_ID is Must in numbers")
        continue
    OWNER_ID = int(OWNER_ID)
    break
if iamnnew is True:
    print("This is to authenticate to your telegram account for downloading Telegram files.\nYou can get this from https://my.telegram.org DO NOT put this in quotes")
while True:
    TELEGRAM_API = input("(Require field) TELEGRAM_API :- ")
    if TELEGRAM_API == "":
        print("You Must Write TELEGRAM_API")
        continue
    if not TELEGRAM_API.isnumeric():
        print("TELEGRAM_API is Must in numbers")
        continue
    TELEGRAM_API = int(TELEGRAM_API)
    break

if iamnnew is True:
    print("This is to authenticate to your telegram account for downloading Telegram files.\nYou can get this from https://my.telegram.org")
while True:
    TELEGRAM_HASH = input("(Require field) TELEGRAM_HASH :- ")
    if TELEGRAM_HASH == "":
        print("You Must Write TELEGRAM_HASH")
        continue
    break

if iamnnew is True:
    print("You Must Write DOWNLOAD_DIR maybe this give error in future")
DOWNLOAD_DIR = input("Enter your Download Directory :- ")
if DOWNLOAD_DIR == "":
    DOWNLOAD_DIR = "/usr/src/app/torrentmirror/"
    print("You Must Write DOWNLOAD_DIR maybe this give error in future")

# Optional config
if iamnnew is True:
    print("A short interval of time in seconds after which the Mirror progress message is updated. (I recommend to keep it 5 seconds at least)")
try:
    DOWNLOAD_STATUS_UPDATE_INTERVAL = int(
        input("(Optional field) DOWNLOAD_STATUS_UPDATE_INTERVAL :- "))
except ValueError:
    DOWNLOAD_STATUS_UPDATE_INTERVAL = 5

if iamnnew is True:
    print("Interval of time (in seconds), after which the bot deletes it's message (and command message) which is expected to be viewed instantly.\nNote: Set to -1 to never automatically delete messages")
try:
    AUTO_DELETE_MESSAGE_DURATION = int(
        input("(Optional field) AUTO_DELETE_MESSAGE_DURATION :- "))
except ValueError:
    AUTO_DELETE_MESSAGE_DURATION = 20
if iamnnew is True:
    print("(Optional field) (Leave empty if unsure) if this field is set to True , bot will check file in drive, if it is present in drive, downloading will be stopped.")
STOP_DUPLICATE_MIRROR = input(
    "(Optional field) STOP_DUPLICATE_MIRROR (Y/n or hit enter) :- ")
if STOP_DUPLICATE_MIRROR.lower() == "y":
    STOP_DUPLICATE_MIRROR = "true"
else:
    STOP_DUPLICATE_MIRROR = "false"

if iamnnew is True:
    print("(Optional field) (Leave empty if unsure) Whether to use service accounts or not.\nFor this to work see 'Using service accounts' in README.md")
USE_SERVICE_ACCOUNTS = input(
    "(Optional field) USE_SERVICE_ACCOUNTS (Y/n or hit enter) :- ")
if USE_SERVICE_ACCOUNTS.lower() == "y":
    USE_SERVICE_ACCOUNTS = "true"
else:
    USE_SERVICE_ACCOUNTS = "false"

if iamnnew is True:
    print("(Optional field) Set to (True) if GDRIVE_FOLDER_ID is from a Team Drive else False or Leave it empty.")
IS_TEAM_DRIVE = input("(Optional field) IS_TEAM_DRIVE (Y/n or hit enter) :- ")
if IS_TEAM_DRIVE.lower() == "y":
    IS_TEAM_DRIVE = "true"
else:
    IS_TEAM_DRIVE = "false"
if iamnnew is True:
    print("(Optional field) To limit cloning Google Drive (leave space between number and unit, TB or GB only), examples: if you fill 1 GB it will limit 1GB.")
CLONE_LIMIT = input(
    "leave space between number and unit, examples: 1 TB or 100 GB only CLONE_LIMIT :- ")
if iamnnew is True:
    print("(Optional field) Write all the User and Group ID's you want to authorize Bot Separated by Space (Example : '123456789 987654321 -1001234567890') Bot Can Distinguish Between User ID and Group Id & Allow only users to Restart the bot while Group IDs can't Restart the Bot.")
AUTHORIZED_CHATS = input("(Optional field) AUTHORIZED_CHATS :- ")
if iamnnew is True:
    print("(Optional field) Refer to https://github.com/ParveenBhadooOfficial/Google-Drive-Index The URL should not have any trailing '/'.")
INDEX_URL = input("(Optional field) INDEX_URL :- ")
if iamnnew is True:
    print("(Optional field) View Link button to open file Index Link in browser instead of direct download link, you can figure out if it's compatible with your Index code or not, open any video from you Index and check if the END of link from browser link bar is ?a=view, if yes make it True it will work (Compatible with Bhadoo Index Code).")
VIEW_LINK = input("(Optional field) VIEW_LINK (Y/n or hit enter) :- ")
if VIEW_LINK.lower() == "y":
    VIEW_LINK = "true"
else:
    VIEW_LINK = "false"
if iamnnew is True:
    print("Mega.nz api key to mirror mega.nz links.")
MEGA_KEY = input("(Optional field) MEGA_KEY :- ")
if iamnnew is True:
    print("Your username you used to sign up on mega.nz for using premium accounts (Leave th)")
MEGA_USERNAME = input("(Optional field) MEGA_USERNAME :- ")
if iamnnew is True:
    print("Your password for your mega.nz account")
MEGA_PASSWORD = input("(Optional field) MEGA_PASSWORD :- ")
if iamnnew is True:
    print("(Optional field) If you want to remove mega.nz mirror support (bcoz it's too much buggy and unstable), set it to True.")
BLOCK_MEGA_LINKS = input("BLOCK_MEGA_LINKS :- ")
if iamnnew is True:
    print("(Optional field) (Leave empty if unsure) Some of common shortner like gplinks.in , afly.in, gpmojo.com, earnload.com, za.gl, urlshortx.com")
SHORTENER = input("SHORTENER :- ")
if iamnnew is True:
    print("API from gplinks.in , afly.in, gpmojo.com, earnload.com, za.gl, urlshortx.com")
SHORTENER_API = input("SHORTENER_API :- ")

if iamnnew is True:
    print("(Optional field) Set it to True if you want to use MAX_TORRENT_SIZE.")
ENABLE_FILESIZE_LIMIT = input(
    "(Optional field) ENABLE_FILESIZE_LIMIT (Y/n or hit enter) :- ")
if ENABLE_FILESIZE_LIMIT.lower() == "y":
    ENABLE_FILESIZE_LIMIT = "true"
else:
    ENABLE_FILESIZE_LIMIT = "false"

if iamnnew is True:
    print("To limit the Torrent mirror size, Fill The amount you want to limit, examples: if you fill 15 it will limit 15gb.")
try:
    MAX_TORRENT_SIZE = int(
        input("MAX_TORRENT_SIZE :- "))
except ValueError:
    MAX_TORRENT_SIZE = 15


BUTTON_FOUR_NAME = input("BUTTON_FOUR_NAME :- ")
BUTTON_FOUR_URL = input("BUTTON_FOUR_URL :- ")
BUTTON_FIVE_NAME = input("BUTTON_FIVE_NAME :- ")
BUTTON_FIVE_URL = input("BUTTON_FIVE_URL :- ")
BUTTON_SIX_NAME = input("BUTTON_SIX_NAME :- ")
BUTTON_SIX_URL = input("BUTTON_SIX_URL :- ")


real_config = {}

real_config["BOT_TOKEN"] = BOT_TOKEN
real_config["GDRIVE_FOLDER_ID"] = GDRIVE_FOLDER_ID
real_config["OWNER_ID"] = OWNER_ID
real_config["DOWNLOAD_DIR"] = DOWNLOAD_DIR
real_config["TELEGRAM_API"] = TELEGRAM_API
real_config["TELEGRAM_HASH"] = TELEGRAM_HASH
real_config["DOWNLOAD_STATUS_UPDATE_INTERVAL"] = DOWNLOAD_STATUS_UPDATE_INTERVAL
real_config["AUTO_DELETE_MESSAGE_DURATION"] = AUTO_DELETE_MESSAGE_DURATION
real_config["USE_SERVICE_ACCOUNTS"] = USE_SERVICE_ACCOUNTS
real_config["IS_TEAM_DRIVE"] = IS_TEAM_DRIVE
real_config["AUTHORIZED_CHATS"] = AUTHORIZED_CHATS
real_config["CLONE_LIMIT"] = CLONE_LIMIT
real_config["INDEX_URL"] = INDEX_URL
real_config["VIEW_LINK"] = VIEW_LINK
real_config["MEGA_KEY"] = MEGA_KEY
real_config["MEGA_USERNAME"] = MEGA_USERNAME
real_config["MEGA_PASSWORD"] = MEGA_PASSWORD
real_config["STOP_DUPLICATE_MIRROR"] = STOP_DUPLICATE_MIRROR
real_config["BLOCK_MEGA_LINKS"] = BLOCK_MEGA_LINKS
real_config["SHORTENER"] = SHORTENER
real_config["SHORTENER_API"] = SHORTENER_API
real_config["BUTTON_FOUR_NAME"] = BUTTON_FOUR_NAME
real_config["BUTTON_FOUR_URL"] = BUTTON_FOUR_URL
real_config["BUTTON_FIVE_NAME"] = BUTTON_FIVE_NAME
real_config["BUTTON_FIVE_URL"] = BUTTON_FIVE_URL
real_config["BUTTON_SIX_NAME"] = BUTTON_SIX_NAME
real_config["BUTTON_SIX_URL"] = BUTTON_SIX_URL

with open("config.env", "w") as file:
    for key, value in real_config.items():
        if type(value) != int:
            value = f'"{value}"'
        if type(value) == int:
            value = f'{value}'
        file.write(f"{key} = {value}\n")


Review = input("Do You Want Review Config file?? (say Y/n or hit enter) :- ")
if Review.lower() == "y":
    config_file = open("config.env", "r")
    print(config_file.read())
else:
    sys.exit()
