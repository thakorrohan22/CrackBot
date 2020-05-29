"""Available Commands:

.cia
.love
.panga
.love

@CRACKEXY"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd





@borg.on(admin_cmd("(.*)"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5
    

    animation_ttl = range(0, 9)

    input_str = event.pattern_match.group(1)

    if input_str == "kavya":

        await event.edit(input_str)

        animation_chars = [
            "DEADBOY",
            "Is",
            "BIGGGGESST❤️",
            "FAN" ,
            "Of",
            "CIARA",
            "❤️❤️❤️",
            "Swear it is the Truth🔥",
            "DEADBOY IS BIGGGGESST❤️ FAN OF CIARA ❤️❤️❤️\n Swear it is the Truth🔥"
        ]

        for i in animation_ttl:


            await event.edit(animation_chars[i % 9])
            await asyncio.sleep(animation_interval)
            
@borg.on(admin_cmd("(.*)"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5
    

    animation_ttl = range(0, 9)

    input_str = event.pattern_match.group(1)

    if input_str == "love":

        await event.edit(input_str)

        animation_chars = [
            "DeadBoy",
            "Only",
            "Loves❣️",
            "DeadGirl🔥" ,
            "Untill",
            "He",
            "Dies",
            "😁",
            "DeadBoy Only Loves❣️ DeadGirl🔥 Untill He Dies 😁"
        ]

        for i in animation_ttl:


            await event.edit(animation_chars[i % 9])
            await asyncio.sleep(animation_interval) 
            
@borg.on(admin_cmd("(.*)"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5
    

    animation_ttl = range(0, 8)

    input_str = event.pattern_match.group(1)

    if input_str == "panga":

        await event.edit(input_str)

        animation_chars = [
            "DeadBoy",
            "Se Agar",
            "Liya" ,
            "Panga😡",
            "To",
            "Ho Jayega",
            "Danga😒",
            "DeadBoy Se Agar Liya Panga😡 To Ho Jayega Danga😒"
        ]

        for i in animation_ttl:


            await event.edit(animation_chars[i % 8])
            await asyncio.sleep(animation_interval)  
            
@borg.on(admin_cmd("(.*)"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5
    

    animation_ttl = range(0, 8)

    input_str = event.pattern_match.group(1)

    if input_str == "love":

        await event.edit(input_str)

        animation_chars = [
            "I🔥",
            "Luvvv😍😍😍😍",
            "Youuuuuuuu🥰" ,
            "Myyyyyyyy😍😍",
            "Jaaaannnnnnnnnñ😍😍😍😍😍😍😍",
            "I🔥 Luvvv😍😍😍😍 Youuuuuuuu😍 Myyyyyyyy😍😍😍😍 Jaannnnnnnn😍😍😍😍😍😍"
        ]

        for i in animation_ttl:


            await event.edit(animation_chars[i % 8])
            await asyncio.sleep(animation_interval)                                
