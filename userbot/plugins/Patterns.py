"""Available Commands:

.kavya
.akku
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
            "Crackexy",
            "Is",
            "Best",
            "Friend" ,
            "Of",
            "Kavya",
            "❣️",
            "Swear it is the Truth🔥",
            "Crackexy Is Best Friend Of Kavya ❣️\n Swear it is the Truth🔥"
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

    if input_str == "akku":

        await event.edit(input_str)

        animation_chars = [
            "Crackexy",
            "Only",
            "Loves❣️",
            "Akku🔥" ,
            "Untill",
            "He",
            "Dies",
            "😁",
            "Crackexy Only Loves❣️ Akku🔥 Untill He Dies 😁"
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
            "Crackexy",
            "Se Agar",
            "Liya" ,
            "Panga😡",
            "To",
            "Ho Jayega",
            "Danga😒",
            "Crackexy Se Agar Liya Panga😡 To Ho Jayega Danga😒"
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
            "Luvvvvvvvvvvvvvvvvvvvv😍😍😍😍",
            "Youuuuuuuuuuuuuuuuuuuuuuuuuu🥰" ,
            "Tooooooo",
            "ooooooooooooooo",
            "Myyyyyyyyyyyy😍😍",
            "Jaaaannnnnnnnnñ😍😍😍😍😍😍😍",
            "I🔥 Luvvvvvvvvvvvvvvvvv😍😍😍😍 Youuuuuuuuuuuuuuuuuuuuuuuuuuuuuu😍 Toooooooooo Myyyyyyyyyyyyyyyyyy😍😍😍😍 Jaannnnnnnnnnnnnnn😍😍😍😍😍😍"
        ]

        for i in animation_ttl:


            await event.edit(animation_chars[i % 8])
            await asyncio.sleep(animation_interval)                                
