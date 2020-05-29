"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet."

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**`Abe! Jinda Hun. ψ(*_*)ψ`**\n"

                     "` ❤️ Loving GF :`@Dead_Girl_Here ❤️\n"
                     "` 🔥 Sabh Sahi Chalra Hai:` **Chill Kar 👌!**\n"
                    f"` 🔥 My Legendry Owner`: {DEFAULTUSER}")

