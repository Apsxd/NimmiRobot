from Nimmirobot.modules.disable import DisableAbleCommandHandler
from Nimmirobot import dispatcher

from telegram.ext import CallbackContext, Filters, CommandHandler

__help__ = """
*Available commands:*\n
*Movie information:*
 • `/imdb <movie name>`: does a movie search in Imdb site\n
*Lyrics:*
 • `/lyrics <song name>`: does a lyric search for a given song name\n
*Image reverse:*
 • `/reverse`: does a *reverse image search* of the media which it was replied to\n
*Text to speech:*
 • `/tts <text>`: convert text to speech\n
*Songs:*
 • `/video <songname artist(optional)>`: uploads the video song in sd quality (480p) as mp4 \
• `/song <songname>(optional)>`:uploads the song
"""

__mod_name__ = "MEDIA"
__command_list__ = ["reverse", "tts", "video"]
