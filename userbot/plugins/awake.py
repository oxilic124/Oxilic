"""
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
MADE BY @LEGENDX22 dont kang this plugin
CREDITS = @LEGENDX22 @PROBOYX @alain_champion
Special thanks @alain_champion for this modified version
if you kang then keep credits
"""
import os
import time
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from userbot import ALIVE_NAME, legendversion, StartTime, CMD_HELP
from . import legend
from userbot.legend import BOT
from userbot.utils import admin_cmd
from telethon import version
from math import ceil
import json
import random
import re
from telethon import events, errors, custom
import io
from platform import python_version, uname

ALIVE_PHOTTO = Config.ALIVE_PHOTTO
if ALIVE_PHOTTO is None:
  ALIVE_PHOTTO = "https://telegra.ph/file/1a521001683a360053b32.jpg"


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "π³ππππ"

global ghanti
        
#make by LEGEND X bht mehnat lag gayi yrr but banhi gaya π           
#@command(outgoing=True, pattern="^.awake$")
@borg.on(admin_cmd(pattern=r"awake"))
async def amireallyalive(awake):
   """ For .awake command, check if the bot is running.  """
   tag = borg.uid
   uptm = await legend.get_readable_time((time.time() - StartTime))
   ALIVE_MESSAGE= f" β‘οΈ {BOT} β‘οΈ  IS ON π₯ FIRE π₯"
   ALIVE_MESSAGE += "\n\n"
   ALIVE_MESSAGE += "π πππππ΄πΌ πππ°πππ π\n\n"
   ALIVE_MESSAGE += "βοΈ ππ΄π»π΄ππ·πΎπ½ ππ΄πππΈπΎπ½ βοΈ : 1.19.5\n\n"
   ALIVE_MESSAGE += "πΆ π³π΄ππΈπ» ππ΄πππΈπΎπ½ πΆ :   2.8\n\n"
   ALIVE_MESSAGE += f"π· ππΏππΈπΌπ΄ π· : {uptm}\n\n"
   ALIVE_MESSAGE += f"π  πΌπ π±πΎππ π : [{DEFAULTUSER}](tg://user?id={tag})\n\n"
   ALIVE_MESSAGE += "π° πΆππΎππΏ π° : [SUPPORT](https://t.me/deviluserbot)\n\n"
   ALIVE_MESSAGE += f"π  [π³π΄πΏπ»πΎπ](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Flucifeermorningstar%2FDevil&template=https%3A%2F%2Fgithub.com%2Flucifeermorningstar%2FDevil) ππΎππ πΎππ½ πΎπΏ [{BOT}](http://github.com/lucifeermorningstar/Devil)  π \n"   
   await awake.delete() 
   await borg.send_file(awake.chat_id, ALIVE_PHOTTO,caption=ALIVE_MESSAGE)

CMD_HELP.update(
    {
        "awake": "Plugin : awake\
    \n\nSyntax : .awake\
    \nFunction : you can set here costom alive pic .set var ALIVE_PHOTTO (Telegraph link)"
    }
)
