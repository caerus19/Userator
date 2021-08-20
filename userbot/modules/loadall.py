from userbot.events import register
from userbot import bot, TEMP_DOWNLOAD_DIRECTORY
import asyncio
import os

@register(pattern=".loadall",outgoing=True)
async def loadall(event)
    curruser = getuser()
    command = "cd userbot/modules && git clone https://github.com/caerus19/UseratorPlugins"
    process = await asyncio.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await process.communicate()
    result = str(stdout.decode().strip()) \
        + str(stderr.decode().strip())

