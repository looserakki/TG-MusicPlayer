import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")
    
# Necessary Vars
API_ID = int(os.getenv("API_ID", "9951240"))
API_HASH = os.getenv("API_HASH", "931b1d84bc9698e5c567661299299625")
SESSION = os.getenv("SESSION", "AQBeql5K4zgdMtmO5ldeSipr4DlHVm5QzSJSMB8o9h4dey9F6zUKQrN7FRT_wOMhbpY80QQxp35ayGoPOB5Dk_lWUlAE39G0cGayQAs4GIy5T1eRkEC20JuPVYMMzRdFKwf-laRalMrCTxb6roCSc86PC4Pp0ueK19ZE7B1HvyblKkz3T0GfWMG7Sj489Mzqra1JH0-FPDvdm0plmyrFkQ-wNJFWPx-pPfsa18Bn1hlG2cwezjDzV-y7fEbJKsk9yt-H2MCv70FyVjVdoXTU9vO1ITcs_hxj_NiE5GYEvkXkyVoNvqDOCkl36dHxuZIiz6UbGBeBwOBVWJTaeZPQCJ8OfwY-cgA")
HNDLR = os.getenv("HNDLR", "!")
GROUP_MODE = os.getenv("GROUP_MODE", "True")


contact_filter = filters.create(
    lambda _, __, message:
    (message.from_user and message.from_user.is_contact) or message.outgoing
)


if GROUP_MODE == ("True" or "true"):
    grp = True
else:
    grp = False

GRPPLAY = grp
bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="VCBot"))
call_py = PyTgCalls(bot)
