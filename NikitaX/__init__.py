from NikitaX.core.bot import NikitaXBot
from NikitaX.core.dir import dirr
from NikitaX.core.git import git
from NikitaX.core.userbot import Userbot
from NikitaX.misc import dbb, heroku, sudo

from .logging import LOGGER


dirr()

git()

dbb()

heroku()

sudo()

# Clients
app = NikitaXBot()
userbot = Userbot()


from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
