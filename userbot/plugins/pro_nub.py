"""Available Commands:

.kavya
.akku
.panga
.mepro

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
            "Panga😒",
            "Crackexy Se Agar Liya Panga😡 To Ho Jayega Panga😒"
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

    if input_str == "mepro":

        await event.edit(input_str)

        animation_chars = [
            "EvErYbOdY",
            "Was",
            "Pro" ,
            "uNtiL",
            "i",
            "aRriVed",
            "😈",
            "EvErYbOdY was Pro uNtiL i aRriVed 😈"
        ]

        for i in animation_ttl:


            await event.edit(animation_chars[i % 8])
            await asyncio.sleep(animation_interval)                                
