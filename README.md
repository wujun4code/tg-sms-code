# tg-sms-code

## pip install

```sh
pip install telethon
pip install pyrogram
pip install termcolor
pip install TgCrypto
pip install pyfiglet
```

## run `get-session.py`

```sh
python3 get-session.py
```

then your active device will receive a direct message from Telegram Saved Messages/User’s, it is the SESSION which is reqiued by next step.

```sh
python3 get-last-sms-code.py
```

then you will see the last message sent from Telegram Offical, here is a sample

```text
Login code: 12345. Do not give this code to anyone, even if they say they are from Telegram!

This code can be used to log in to your Telegram account. We never ask it for anything else.

If you didn't request this code by trying to log in on another device, simply ignore this message.
```