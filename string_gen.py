try:

    from telethon.sessions import StringSession

    from telethon.sync import TelegramClient

except BaseException:

    print("Telethon Not Found. Installing Now.")

    import os

    os.system("pip3 install telethon")

    from telethon.sessions import StringSession

    from telethon.sync import TelegramClient

ok = """ ____  ____  __  ____   __   _  _

@I_AM_DIK

"""

print(ok)

APP_ID = int(input("Enter APP ID here: \n"))

API_HASH = input("Enter API HASH here: \n")

client = TelegramClient(StringSession(), APP_ID, API_HASH)

with client:

    session_str = client.session.save()

    client.send_message("me", f"`{session_str}`")

    client.send_message(

        "THIS IS YOUR STRING SESSION \nJoin https://t.me/fafda_jalebi_updates for More Support."

    )

    print("⬆ Please Check Your Telegram Saved Message For Your String.")
