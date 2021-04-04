import shutil, psutil
import signal
import pickle

from os import execl, path, remove
from sys import executable
import time

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError

from telegram.ext import CommandHandler, run_async
from bot import dispatcher, updater, botStartTime, SHORTENER, SHORTENER_API, SHORTENERLINK_API
from bot.helper.ext_utils import fs_utils
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.telegram_helper.message_utils import *
from .helper.ext_utils.bot_utils import get_readable_file_size, get_readable_time
from .helper.telegram_helper.filters import CustomFilters
from .modules import authorize, list, cancel_mirror, mirror_status, mirror, clone, watch, delete , speedtest


@run_async
def stats(update, context):
    currentTime = get_readable_time((time.time() - botStartTime))
    total, used, free = shutil.disk_usage('.')
    total = get_readable_file_size(total)
    used = get_readable_file_size(used)
    free = get_readable_file_size(free)
    sent = get_readable_file_size(psutil.net_io_counters().bytes_sent)
    recv = get_readable_file_size(psutil.net_io_counters().bytes_recv)
    cpuUsage = psutil.cpu_percent(interval=0.5)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    stats = f'<b>Bot Uptime:</b> {currentTime}\n' \
            f'<b>Total disk space:</b> {total}\n' \
            f'<b>Used:</b> {used}  ' \
            f'<b>Free:</b> {free}\n\n' \
            f'📊Data Usage📊\n<b>Upload:</b> {sent}\n' \
            f'<b>Down:</b> {recv}\n\n' \
            f'<b>🖥️CPU:</b> {cpuUsage}% ' \
            f'<b>📝RAM:</b> {memory}% ' \
            f'<b>📀DISK:</b> {disk}%'
    sendMessage(stats, context.bot, update)


@run_async
def start(update, context):
    start_string = f'''
This is a bot which can mirror all your links to Google drive!
👲 Moded By: @kjuned007
Type /{BotCommands.HelpCommand} to get a list of available commands
'''
    sendMessage(start_string, context.bot, update)

def gen_chlog(repo, diff):
    ch_log = ''
    d_form = "%d/%m/%y"
    for c in repo.iter_commits(diff):
        ch_log += f'• [{c.committed_datetime.strftime(d_form)}]: {c.summary} <{c.author}>\n'
    return ch_log


# --- Reference: https://github.com/jagrit007/tgUserBot/blob/master/userbot/modules/updater.py

@run_async
def repo(update, context):
    bot.send_message(update.message.chat_id,
    reply_to_message_id=update.message.message_id,
    text="*Repo*: `https://github.com/junedkh/Torrent-Mirror-V1.1`", parse_mode="Markdown")

@run_async
def update(update, context):
    branches = ["stable"]
    text = update.effective_message.text
    msg = sendMessage("Fetching Updates....", context.bot, update)
    repo_url = "https://github.com/junedkh/Torrent-Mirror-V1.1.git"
    try:
        repo = Repo()
    except NoSuchPathError as error:
        msg.edit_text(f'`directory {error} is not found`', parse_mode="Markdown")
        return
    except InvalidGitRepositoryError as error:
        msg.edit_text(f'`directory {error} does not seems to be a git repository`', parse_mode="Markdown")
        return
    except GitCommandError as error:
        msg.edit_text(f'`Early failure! {error}`', parse_mode="Markdown")
        return
    except:
        msg.edit_text("Something's Wrong, Please manually pull.")
    branch = repo.active_branch.name
    if branch not in branches:
        msg.edit_text("Seems like you are using a custom branch!")
        return
    try:
        repo.create_remote('upstream', repo_url)
    except:
        pass
    remote = repo.remote('upstream')
    remote.fetch(branch)
    clogs = gen_chlog(repo, f'HEAD..upstream/{branch}')

    if not clogs:
        msg.edit_text(f"Bot up-to-date with *{branch}*", parse_mode="Markdown")
        return
    if not "now" in text:
        msg.edit_text(f"*New Update Available*\nCHANGELOG:\n\n{clogs}\n\n\nDo `/update now` to Update BOT.", parse_mode="Markdown")
        return
    try:
        remote.pull(branch)
        msg.edit_text(f"*Successfully Updated BOT, Attempting to restart!*", parse_mode="Markdown")
        _restart(msg)

    except GitCommandError:
        remote.git.reset('--hard')
        msg.edit_text(f"*Successfully Updated BOT, Attempting to restart!*", parse_mode="Markdown")
        _restart(msg)


def _restart(reply):
    # Save restart message object in order to reply to it after restarting
    fs_utils.clean_all()
    with open('restart.pickle', 'wb') as status:
        pickle.dump(reply, status)
    execl(executable, executable, "-m", "bot")


@run_async
def restart(update, context):
    restart_message = sendMessage("Restarting, Please wait!", context.bot, update)
    _restart(restart_message)


@run_async
def ping(update, context):
    start_time = int(round(time.time() * 1000))
    reply = sendMessage("Starting Ping", context.bot, update)
    end_time = int(round(time.time() * 1000))
    editMessage(f'{end_time - start_time} ms', reply)


@run_async
def log(update, context):
    sendLogFile(context.bot, update)


@run_async
def bot_help(update, context):
    help_string = f'''
/{BotCommands.HelpCommand}: To get this message

/{BotCommands.MirrorCommand} [download_url][magnet_link]: Start mirroring the link to google drive

/{BotCommands.UnzipMirrorCommand} [download_url][magnet_link] : starts mirroring and if downloaded file is any archive , extracts it to google drive

/{BotCommands.TarMirrorCommand} [download_url][magnet_link]: start mirroring and upload the archived (.tar) version of the download

/{BotCommands.WatchCommand} [youtube-dl supported link]: Mirror through youtube-dl. Click /{BotCommands.WatchCommand} for more help.

/{BotCommands.TarWatchCommand} [youtube-dl supported link]: Mirror through youtube-dl and tar before uploading

/{BotCommands.CancelMirror} : Reply to the message by which the download was initiated and that download will be cancelled

/{BotCommands.StatusCommand}: Shows a status of all the downloads

/{BotCommands.ListCommand} [search term]: Searches the search term in the Google drive, if found replies with the link

/{BotCommands.StatsCommand}: Show Stats of the machine the bot is hosted on

/{BotCommands.AuthorizeCommand}: Authorize a chat or a user to use the bot (Can only be invoked by owner of the bot)

/{BotCommands.LogCommand}: Get a log file of the bot. Handy for getting crash reports

/{BotCommands.UpdateCommand}: Update the BOT with git repository.

/{BotCommands.SpeedCommand}: Check Internet Speed of the Host

/{BotCommands.RepoCommand}: Get the bot repo.

'''
    sendMessage(help_string, context.bot, update)


def main():
    fs_utils.start_cleanup()
    # Check if the bot is restarting
    if path.exists('restart.pickle'):
        with open('restart.pickle', 'rb') as status:
            restart_message = pickle.load(status)
        restart_message.edit_text("Restarted Successfully!")
        remove('restart.pickle')

    start_handler = CommandHandler(BotCommands.StartCommand, start,
                                   filters=CustomFilters.authorized_chat | CustomFilters.authorized_user)
    ping_handler = CommandHandler(BotCommands.PingCommand, ping,
                                  filters=CustomFilters.authorized_chat | CustomFilters.authorized_user)
    restart_handler = CommandHandler(BotCommands.RestartCommand, restart,
                                     filters=CustomFilters.owner_filter)
    help_handler = CommandHandler(BotCommands.HelpCommand,
                                  bot_help, filters=CustomFilters.authorized_chat | CustomFilters.authorized_user)
    stats_handler = CommandHandler(BotCommands.StatsCommand,
                                   stats, filters=CustomFilters.authorized_chat | CustomFilters.authorized_user)
    log_handler = CommandHandler(BotCommands.LogCommand, log, filters=CustomFilters.owner_filter)
    update_handler = CommandHandler(BotCommands.UpdateCommand, update,
                                   filters=CustomFilters.authorized_chat | CustomFilters.owner_filter)
    repo_handler = CommandHandler(BotCommands.RepoCommand, repo,
                                   filters=CustomFilters.authorized_chat | CustomFilters.authorized_user)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(ping_handler)
    dispatcher.add_handler(update_handler)
    dispatcher.add_handler(restart_handler)
    dispatcher.add_handler(repo_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(stats_handler)
    dispatcher.add_handler(log_handler)
    updater.start_polling()
    LOGGER.info("Bot Started!")
    LOGGER.info("Shortner %s"%SHORTENER)
    LOGGER.info("Shortner API %s"%SHORTENER_API)
    LOGGER.info("BITLY API %s"%SHORTENERLINK_API)
    signal.signal(signal.SIGINT, fs_utils.exit_clean_up)


main()
