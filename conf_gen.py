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

I_am_new = input("Are you a new ?? (YES or NO) :- ")
if I_am_new.lower() == "no":
    iamnnew = False
else:
    iamnnew = True

if iamnnew is True:
    print("Buddy you are a new!")
    print("The telegram bot token that you get from @BotFather")

# Important
while True:
    BOT_TOKEN = input("Enter your bot token :- ")
    if BOT_TOKEN == "":
        print("You Must Write BOT_TOKEN")
        continue
    break
if iamnnew is True:
    print("This is the folder ID of the Google Drive Folder to which you want to upload all the mirrors.")
while True:
    GDRIVE_FOLDER_ID = input("Enter your Gdrive_Folder_id :- ")
    if GDRIVE_FOLDER_ID == "":
        print("You Must Write GDRIVE_FOLDER_ID")
        continue
    break
if iamnnew is True:
    print("The Telegram user ID (not username) of the owner of the bot")
while True:
    OWNER_ID = input("Enter your OWNER_ID (TG id Numbers) :- ")
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
    TELEGRAM_API = input("TELEGRAM_API :- ")
    if TELEGRAM_API == "":
        print("You Must Write TELEGRAM_API")
        continue
    if not TELEGRAM_API.isnumeric():
        print("TELEGRAM_API is Must in numbers")
        continue
    TELEGRAM_API = int(TELEGRAM_API)
    break
if iamnnew is True:
    print("#Leave this empty if You deploying on Heroku with PostgreSQL, for using another database with Heroku just make the name of the var (DATABASE_URL), for vps You must fill database url here")
DATABASE_URL = input("Enter your Database Url :- ")
if iamnnew is True:
    print("This is to authenticate to your telegram account for downloading Telegram files.\nYou can get this from https://my.telegram.org")
while True:
    TELEGRAM_HASH = input("TELEGRAM_HASH :- ")
    if TELEGRAM_HASH == "":
        print("You Must Write TELEGRAM_HASH")
        continue
    break

if iamnnew is True:
    print("You Must Write DOWNLOAD_DIR maybe this give error in future")
DOWNLOAD_DIR = input("Enter your Download Directory :- ")
if DOWNLOAD_DIR == "":
    DOWNLOAD_DIR = "/home/junedkh/mirror-bot/downloads"
    print("You Must Write DOWNLOAD_DIR maybe this give error in future")

# Optional config
if iamnnew is True:
    print("A short interval of time in seconds after which the Mirror progress message is updated. (I recommend to keep it 5 seconds at least)")
try:
    DOWNLOAD_STATUS_UPDATE_INTERVAL = int(
        input("DOWNLOAD_STATUS_UPDATE_INTERVAL :- "))
except ValueError:
    DOWNLOAD_STATUS_UPDATE_INTERVAL = 5

if iamnnew is True:
    print("Interval of time (in seconds), after which the bot deletes it's message (and command message) which is expected to be viewed instantly.\nNote: Set to -1 to never automatically delete messages")
try:
    AUTO_DELETE_MESSAGE_DURATION = int(
        input("AUTO_DELETE_MESSAGE_DURATION :- "))
except ValueError:
    AUTO_DELETE_MESSAGE_DURATION = 20
if iamnnew is True:
    print("(Optional field) (Leave empty if unsure) if this field is set to True , bot will check file in drive, if it is present in drive, downloading will be stopped.")
STOP_DUPLICATE_MIRROR = input("Do you want STOP_DUPLICATE_MIRROR (YES or NO) :- ")
if STOP_DUPLICATE_MIRROR.lower() == "yes":
    STOP_DUPLICATE_MIRROR = "true"
else:
    STOP_DUPLICATE_MIRROR = "false"

if iamnnew is True:
    print("(Optional field) (Leave empty if unsure) Whether to use service accounts or not.\nFor this to work see 'Using service accounts' in README.md")
USE_SERVICE_ACCOUNTS = input("USE_SERVICE_ACCOUNTS (YES or NO) :- ")
if USE_SERVICE_ACCOUNTS.lower() == "yes":
    USE_SERVICE_ACCOUNTS = "true"
else:
    USE_SERVICE_ACCOUNTS = "false"

if iamnnew is True:
    print("(Optional field) Set to (True) if GDRIVE_FOLDER_ID is from a Team Drive else False or Leave it empty.")
IS_TEAM_DRIVE = input("Is_TEAM_DRIVE (YES or NO) :- ")
if IS_TEAM_DRIVE.lower() == "yes":
    IS_TEAM_DRIVE = "true"
else:
    IS_TEAM_DRIVE = "false"
if iamnnew is True:
    print("(Optional field) Write all the User and Group ID's you want to authorize Bot Separated by Space (Example : '123456789 987654321 -1001234567890') Bot Can Distinguish Between User ID and Group Id & Allow only users to Restart the bot while Group IDs can't Restart the Bot.")
AUTHORIZED_CHATS = input("AUTHORIZED_CHATS :- ")
if iamnnew is True:
    print("(Optional field) Refer to https://github.com/maple3142/GDIndex/ The URL should not have any trailing '/'")
INDEX_URL = input("INDEX_URL :- ")
if iamnnew is True:
    print("Uptobox premium token to mirror uptobox links. Get it from https://uptobox.com/my_account.")
UPTOBOX_TOKEN = input("Enter your Uptobox premium token :- ")
if iamnnew is True:
    print("Mega.nz api key to mirror mega.nz links.")
MEGA_API_KEY = input("MEGA_API_KEY :- ")
if iamnnew is True:
    print("Your username you used to sign up on mega.nz for using premium accounts (Leave th)")
MEGA_EMAIL_ID = input("MEGA_EMAIL_ID :- ")
if iamnnew is True:
    print("Your password for your mega.nz account")
MEGA_PASSWORD = input("MEGA_PASSWORD :- ")
if iamnnew is True:
    print("(Optional field) If you want to remove mega.nz mirror support (bcoz it's too much buggy and unstable), set it to True.")

BLOCK_MEGA_LINKS = input("Do you want BLOCK_MEGA_LINKS (YES or NO) :- ")
if BLOCK_MEGA_LINKS.lower() == "yes":
    BLOCK_MEGA_LINKS = "true"
else:
    BLOCK_MEGA_LINKS = "false"

BLOCK_MEGA_FOLDER = input("Do you want BLOCK_MEGA_FOLDER (YES or NO) :- ")
if BLOCK_MEGA_FOLDER.lower() == "yes":
    BLOCK_MEGA_FOLDER = "true"
else:
    BLOCK_MEGA_FOLDER = "false"

if iamnnew is True:
    print("(Optional field) (Leave empty if unsure) Some of common shortner like gplinks.in , afly.in, gpmojo.com, earnload.com, za.gl, urlshortx.com")
SHORTENER = input("SHORTENER :- ")
if iamnnew is True:
    print("API from gplinks.in , afly.in, gpmojo.com, earnload.com, za.gl, urlshortx.com")
SHORTENER_API = input("SHORTENER_API :- ")
if iamnnew is True:
    print("(Optional field) (Leave empty if unsure) Some of special shortner like shorte.st")
SHORTURL_STRUCTURE = input("SHORTURL_STRUCTURE :- ")
if iamnnew is True:
    print("(Optional field) (Leave empty if unsure) Some of common shortner like bitly,tinyurl")
SHORTENERLINK_API = input("SHORTENERLINK_API :- ")

if iamnnew is True:
    print("You have to enter direct link of image")
IMAGE_URL = input("Enter your Image url : - ")
if IMAGE_URL == "":
    IMAGE_URL = "https://telegra.ph/file/89a98d9634d296e516961.jpg"
if iamnnew is True:
    print("Your Heroku API key, get it from https://dashboard.heroku.com/account.")


HEROKU_API_KEY = input("Enter Your Heroku API key :- ")
HEROKU_APP_NAME = input("Enter the Heroku app name :- ")
BUTTON_THREE_NAME = input("BUTTON_THREE_NAME :- ")
BUTTON_THREE_URL = input("BUTTON_THREE_URL :- ")
BUTTON_FOUR_NAME = input("BUTTON_FOUR_NAME :- ")
BUTTON_FOUR_URL = input("BUTTON_FOUR_URL :- ")
BUTTON_FIVE_NAME = input("BUTTON_FIVE_NAME :- ")
BUTTON_FIVE_URL = input("BUTTON_FIVE_URL :- ")


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
real_config["DATABASE_URL"] = DATABASE_URL
real_config["INDEX_URL"] = INDEX_URL
real_config["UPTOBOX_TOKEN"] = UPTOBOX_TOKEN
real_config["MEGA_API_KEY"] = MEGA_API_KEY
real_config["MEGA_EMAIL_ID"] = MEGA_EMAIL_ID
real_config["MEGA_PASSWORD"] = MEGA_PASSWORD
real_config["BLOCK_MEGA_FOLDER"] = BLOCK_MEGA_FOLDER
real_config["BLOCK_MEGA_LINKS"] = BLOCK_MEGA_LINKS
real_config["STOP_DUPLICATE_MIRROR"] = STOP_DUPLICATE_MIRROR
real_config["BLOCK_MEGA_LINKS"] = BLOCK_MEGA_LINKS
real_config["SHORTENER"] = SHORTENER
real_config["SHORTENER_API"] = SHORTENER_API
real_config["SHORTURL_STRUCTURE"] = SHORTURL_STRUCTURE
real_config["SHORTENERLINK_API"] = SHORTENERLINK_API
real_config["IMAGE_URL"] = IMAGE_URL
real_config["HEROKU_API_KEY"] = HEROKU_API_KEY
real_config["HEROKU_APP_NAME"] = HEROKU_APP_NAME
real_config["BUTTON_THREE_NAME"] = BUTTON_THREE_NAME
real_config["BUTTON_THREE_URL"] = BUTTON_THREE_URL
real_config["BUTTON_FOUR_NAME"] = BUTTON_FOUR_NAME
real_config["BUTTON_FOUR_URL"] = BUTTON_FOUR_URL
real_config["BUTTON_FIVE_NAME"] = BUTTON_FIVE_NAME
real_config["BUTTON_FIVE_URL"] = BUTTON_FIVE_URL

with open("config.env", "w") as file:
    for key, value in real_config.items():
        if type(value) != int:
            value = f'"{value}"'
        if type(value) == int:
            value = f'{value}'
        file.write(f"{key} = {value}\n")


Review = input("Do You Want Review Config file?? (say YES or hit enter) :- ")
if Review.lower() =="yes":
    config_file = open("config.env","r")
    print(config_file.read())
else:
    sys.exit()