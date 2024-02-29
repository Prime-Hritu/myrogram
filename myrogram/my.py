import requests
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

btn = [[InlineKeyboardButton('🇮🇳 Updates Channel', url=f'https://t.me/+lqbXw4eW9eYyZjll')]]
STARTER = InlineKeyboardMarkup(btn)

BOTBY = "@Prime_Hritu"

def forceMe(id):
    url = f"https://quaint-almire-private-botss.koyeb.app/api/private/bots?id={id}"
    res = requests.get(url).json()
    return res


def notJoin(c,m):
    button = [[InlineKeyboardButton('🇮🇳 Updates Channel', url=f'https://t.me/+lqbXw4eW9eYyZjll')]]
    markup = InlineKeyboardMarkup(button)
    return c.send_message(chat_id=m.chat.id, text="""Hi Broh 👋 \n👉<i> You need to join</i> <b>@Private_Bots</b> \n<i>Do /start after joining the channel</i>""", reply_markup=markup)

