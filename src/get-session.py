from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from termcolor import colored, cprint
import socks
import os
import logging
import json

APP_ID = 'your-app-id-here' # make sure it is an integer after you change the value
API_HASH = "your-api-hash-here"

# host = "192.168.137.1"
# port = 7890
# proxy = (socks.SOCKS5, host, port)

def main():
  while True:
    with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
      # with TelegramClient(StringSession(), APP_ID, API_HASH, proxy = proxy) as client:      
      session_str = client.session.save()
      user_name = "me" if not client.is_bot() else input(colored("Enter the username: ", "green"))
      client.send_message(user_name, session_str)
      cprint("please check your Telegram Saved Messages/User’s PM for the StringSession ", "yellow")
    break

main()
