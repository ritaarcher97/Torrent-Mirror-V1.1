<p align="center">
<a href="https://github.com/junedkh/Torrent-Mirror-V1.1/stargazers">
<img src="https://img.shields.io/github/stars/junedkh/Torrent-Mirror-V1.1" alt="Stars">
</a>
<a href="https://github.com/junedkh/Torrent-Mirror-V1.1/fork">
<img src="https://img.shields.io/github/forks/junedkh/Torrent-Mirror-V1.1.svg" alt="Forks"/>
</a>
<img src="https://visitor-badge.laobi.icu/badge?page_id=junedkh.Torrent-Mirror-V1.1" alt="visitors" />
</p>
# Important - Read these points first
- Original repo is https://github.com/lzzy12/python-aria-mirror-bot
- I have collected some cool features from various repositories and merged them in one.
- So, credits goes to original repo holder, not to me. I have just collected them.
- This (or any custom) repo is not supported in official bot support group.
- So if you have any issue then check first that issue is in official repo or not, You are only allowed to report that issue in bot support group if that issue is also present in official repo.

# What is this repo about?

This is a telegram bot writen in python for mirroring files on the internet to our beloved Google Drive.

# 📭𝗙𝗘𝗔𝗧𝗨𝗥𝗘𝗦 𝗔𝗡𝗗 𝗦𝗨𝗣𝗣𝗢𝗥𝗧𝗘𝗗📭

- [x] Mirroring direct download links to google drive
- [x] Mirroring Mega.nz links to google drive (In development stage)
- [x] Mirror Telegram files to google drive
- [x] Mirror all youtube-dl supported links
- [x] Extract zip, rar, tar and many supported file types and uploads to google drive with password [How To](https://telegra.ph/Magneto-Python-Aria---Custom-Filename-Examples-01-20)
- [x] Copy files from someone's drive to your drive (using Rclone)
- [x] Service account support in cloning and uploading
- [x] Download progress
- [x] Upload progress
- [x] Download/upload speeds and ETAs
- [x] Docker support
- [x] Uploading To Team Drives.
- [x] Index Link support
- [x] Short Link support also with Custom `SHORTURL_STRUCTURE`
- [X]Direct links supported:

```
Racaty, Hxfile, Anonfiles,
Fembed (femax20 & layarkacaxxi), Onedrive (Only works for file not folder)
```

- [x] Custom file name support for mirror [How to](https://telegra.ph/Magneto-Python-Aria---Custom-Filename-Examples-01-20)
  - Note :- Custom Filename is not supported while mirroring torrent or magnet.

👩‍🚒 **𝗠𝗢𝗗𝗜𝗙𝗜𝗘𝗗 𝗕𝗬** : [Juned KH](https://t.me/kjuned007)

- [x] Cool and stylish Progress Bar
- [x] Change Requirment text
- [x] Now YTDL Fixed (with custom resolution and custom file name)
- [x] Fixing Minor bugs
- [x] Change Dockerfile

📭 **𝗝𝗢𝗜𝗡 𝗢𝗨𝗥 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 𝗚𝗥𝗢𝗨𝗣:** [𝗦𝗨𝗣𝗣𝗢𝗥𝗧 𝗚𝗥𝗢𝗨𝗣](https://t.me/torrent_to_drive):

## Bot commands to be set in botfather

```
mirror - Start Mirroring
tarmirror - Upload tar (zipped) file
unzipmirror - Extract files
clone - copy file/folder to drive
watch - mirror YT-DL support link
tarwatch - mirror youtube playlist link as tar
cancel - Cancel a task
cancelall - Cancel all tasks
del - Delete file from Drive
list - [query] searches files in G-Drive
status - Get Mirror Status message
stats - Bot Usage Stats
help - Get Detailed Help
speedtest - Check Speed of the host
log - Bot Log [owner only]
```

# 𝗛𝗢𝗪 𝗧𝗢 𝗗𝗘𝗣𝗟𝗢𝗬?🤔

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Deploying With Heroku Cli

<details>
<summary><b>Click here for more details</b></summary>
    
- Run the script to generate token file(token.pickle) for Google Drive:
```
python3 generate_drive_token.py
```
- Install [Heroku cli](https://devcenter.heroku.com/articles/heroku-cli)
- Login into your heroku account with command:
```
heroku login
```
- Create a new heroku app:
```
heroku create appname	
```
- Select This App in your Heroku-cli: 
```
heroku git:remote -a appname
```
- Change Dyno Stack to a Docker Container:
```
heroku stack:set container
```
- Add Heroku Postgres (only if you are deploying it for the 1st time)
```
heroku addons:create heroku-postgresql
```
- Add Private Credentials and Config Stuff:
```
git add -f credentials.json token.pickle config.env heroku.yml
```
- Commit new changes:
```
git commit -m "Added Creds."
```
- Push Code to Heroku:
```
git push heroku master --force
```
- Restart Worker by these commands:
```
heroku ps:scale worker=0
```
```
heroku ps:scale worker=1	 	
```
</details>
<br>

## Setting up config file

```
cp config_sample.env config.env
```

- Remove the first line saying:

```
_____REMOVE_THIS_LINE_____=True
```

Fill up rest of the fields. Meaning of each fields are discussed below:

- **BOT_TOKEN** : The telegram bot token that you get from @BotFather
- **GDRIVE_FOLDER_ID** : This is the folder ID of the Google Drive Folder to which you want to upload all the mirrors.
- **DOWNLOAD_DIR** : The path to the local folder where the downloads should be downloaded to
- **DOWNLOAD_STATUS_UPDATE_INTERVAL** : A short interval of time in seconds after which the Mirror progress message is updated. (I recommend to keep it 5 seconds at least)
- **OWNER_ID** : The Telegram user ID (not username) of the owner of the bot
- **AUTO_DELETE_MESSAGE_DURATION** : Interval of time (in seconds), after which the bot deletes it's message (and command message) which is expected to be viewed instantly. Note: Set to -1 to never automatically delete messages
- **IS_TEAM_DRIVE** : (Optional field) Set to "True" if GDRIVE_FOLDER_ID is from a Team Drive else False or Leave it empty.
- **USE_SERVICE_ACCOUNTS**: (Optional field) (Leave empty if unsure) Whether to use service accounts or not. For this to work see "Using service accounts" section below.
- **INDEX_URL** : (Optional field) Refer to https://github.com/maple3142/GDIndex/ The URL should not have any trailing '/'
- **API_KEY** : This is to authenticate to your telegram account for downloading Telegram files. You can get this from https://my.telegram.org DO NOT put this in quotes.
- **API_HASH** : This is to authenticate to your telegram account for downloading Telegram files. You can get this from https://my.telegram.org
- **MEGA_API_KEY**: Mega.nz api key to mirror mega.nz links. Get it from [Mega SDK Page](https://mega.nz/sdk)
- **MEGA_EMAIL_ID**: Your email id you used to sign up on mega.nz for using premium accounts (Leave th)
- **MEGA_PASSWORD**: Your password for your mega.nz account
- **STOP_DUPLICATE_MIRROR**: (Optional field) (Leave empty if unsure) if this field is set to `True` , bot will check file in drive, if it is present in drive, downloading will be stopped. (Note - File will be checked using filename, not using filehash, so this feature is not perfect yet)
  Note: You can limit maximum concurrent downloads by changing the value of MAX_CONCURRENT_DOWNLOADS in aria.sh. By default, it's set to 2
- **SHORTENER** : (Optional field) (Leave empty if unsure) Some of common shortner like `gplinks.in , afly.in, gpmojo.com, earnload.com, za.gl, urlshortx.com`
- **SHORTENER_API** : API from `gplinks.in , afly.in, gpmojo.com, earnload.com, za.gl, urlshortx.com`
- **SHORTURL_STRUCTURE** : This Will be use for like

```
shorte.st
Ex : http://api.{}/stxt/{}/{} How to use for own (1st {} for SHORTENER 2nd {} for SHORTENER_API 3rd {} Will be use for file url)

this is not necessary for gplinks.in , afly.in, gpmojo.com, earnload.com, za.gl, urlshortx.com
```

## Getting Google OAuth API credential file

- Visit the [Google Cloud Console](https://console.developers.google.com/apis/credentials)
- Go to the OAuth Consent tab, fill it, and save.
- Go to the Credentials tab and click Create Credentials -> OAuth Client ID
- Choose Desktop and Create.
- Use the download button to download your credentials.
- Move that file to the root of mirror-bot, and rename it to credentials.json
- Visit [Google API page](https://console.developers.google.com/apis/library)
- Search for Drive and enable it if it is disabled
- Finally, run the script to generate token file (token.pickle) for Google Drive:

```
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
python3 generate_drive_token.py
```

# Using service accounts for uploading to avoid user rate limit

For Service Account to work, you must set USE_SERVICE_ACCOUNTS="True" in config file or environment variables
Many thanks to [AutoRClone](https://github.com/xyou365/AutoRclone) for the scripts

## Generating service accounts

## Step 1. Generate service accounts [What is service account](https://cloud.google.com/iam/docs/service-accounts)

Let us create only the service accounts that we need.
**Warning:** abuse of this feature is not the aim of autorclone and we do **NOT** recommend that you make a lot of projects, just one project and 100 sa allow you plenty of use, its also possible that overabuse might get your projects banned by google.

```
Note: 1 service account can copy around 750gb a day, 1 project makes 100 service accounts so thats 75tb a day, for most users this should easily suffice.
```

`python3 gen_sa_accounts.py --quick-setup 1 --new-only`

A folder named accounts will be created which will contain keys for the service accounts created

NOTE: If you have created SAs in past from this script, you can also just re download the keys by running:

```
python3 gen_sa_accounts.py --download-keys project_id
```

### Add all the service accounts to the Team Drive or folder

- Run:

```
python3 add_to_team_drive.py -d SharedTeamDriveSrcID
```

# Youtube-dl authentication using .netrc file

For using your premium accounts in youtube-dl, edit the netrc file (in the root directory of this repository) according to following format:

```
machine host login username password my_youtube_password
```

where host is the name of extractor (eg. youtube, twitch). Multiple accounts of different hosts can be added each separated by a new line
