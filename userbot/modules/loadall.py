from userbot.events import register
from userbot import bot
import asyncio
import os
from getpass import getuser
from time import sleep
@register(pattern=".loadall",outgoing=True)
async def loadall(event):
    user = getuser()
    command = "cd userbot/modules && git clone https://github.com/caerus19/UseratorPlugins && cd UseratorPlugins && mv *.* .."
    process = await asyncio.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await process.communicate()
    result = str(stdout.decode().strip()) \
        + str(stderr.decode().strip())
    await event.edit("Hazırdır...")
    sleep(10)
