from telethon import TelegramClient, events
import logging
from telethon.sessions import StringSession
from telethon.tl.types import InputMediaPhoto,InputMediaPhotoExternal
import socks
import os
import logging
import json


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)
APP_ID = 'your-app-id-here' # make sure it is an integer after you change the value
API_HASH = "your-api-hash-here"
SESSION = input("please input your SESSION that copied from Telegram Saved Messages/User’s PM :")
# host = "192.168.137.1"
# port = 7890
# proxy = (socks.SOCKS5, host, port)
client = TelegramClient(StringSession(SESSION), APP_ID, API_HASH)
# please use proxy to skip GFW if necessary
# client = TelegramClient(StringSession(SESSION), APP_ID, API_HASH, proxy = proxy)
async def main():
    entity = await client.get_entity(777000)
    async for message in client.iter_messages(entity,1):
        print(message.raw_text)
with client:
    client.loop.run_until_complete(main())