#!/usr/bin/env python3
# Copyright (C) @ZauteKm
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
import os
import re
import heroku3
from dotenv import load_dotenv
from helpers.log import LOGGER

load_dotenv()

YSTREAM=False
STREAM=os.environ.get("STARTUP_STREAM", "https://www.youtube.com/watch?v=36YnV9STBqc")
regex = r"^(?:https?:\/\/)?(?:www\.)?youtu\.?be(?:\.com)?\/?.*(?:watch|embed)?(?:.*v=|v\/|\/)([\w\-_]+)\&?"
match = re.match(regex,STREAM)
if match:
    YSTREAM=True
    finalurl=STREAM
    LOGGER.warning("Starting Startup Stream From YouTube!")
else:
    finalurl=STREAM
    LOGGER.warning("Starting Startup Stream From Link!")

class Config:

    # Mendatory Variables

    ADMIN = os.environ.get("AUTH_USERS", "784985038")
    ADMINS = [int(admin) for admin in (ADMIN).split()]
    API_ID = int(os.environ.get("API_ID", "7797142"))
    API_HASH = os.environ.get("API_HASH", "d3b04868e54c17687f2391f6acc36742")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "2014531683:AAHOl--8LiXXtDpMP1Z-y1MCt5OX68tAT-Q")     
    SESSION = os.environ.get("SESSION_STRING", "BQBzClvBmpeSxB-UrMKClcoNlEFFTc-921zAi2t3aJi_j8Z1oXc8hGJcElq6X3JM3-TT2NzNCe7YcwuV_NxOGT1PL1Y9Re0F9eK1MBUHJ1tONw2u9KXUjAUt6yt0zp_Qb6YXPO02LbdWc6tbkP3WTEH2p1iuaqa7PKkQwtzlLkeUihbJNqCF-kvBPOis0AUWTIK6lOW4Zelud2U9KC8XaGB2zfIXBsYNqkPzDVfmWurt7WoG3CRc8Qo3TmJIlrIW-OPhLAJAvAbZbmeTuMVvbqJhGfY41X8hRBQicnFcmBc2w9VXWzYhKbGsHje17O4p5C4_v0TmjUd-ubj-GM0qmRkAaTX8fQA")
    CHAT_ID = int(os.environ.get("CHAT_ID", "-1001546083133"))

    # Optional Variables

    LOG_GROUP=os.environ.get("LOG_GROUP", "")
    if LOG_GROUP:
        LOG_GROUP=int(LOG_GROUP)
    else:
        LOG_GROUP=None
    BOT_USERNAME=None
    STREAM_URL=finalurl
    YSTREAM=YSTREAM
    SHUFFLE=bool(os.environ.get("SHUFFLE", True))
    ADMIN_ONLY=os.environ.get("ADMIN_ONLY", "False")
    REPLY_MESSAGE=os.environ.get("REPLY_MESSAGE", None)
    if REPLY_MESSAGE:
        REPLY_MESSAGE=REPLY_MESSAGE
        LOGGER.warning("Reply Message Found, Enabled PM Guard !")
    else:
        REPLY_MESSAGE=None
    EDIT_TITLE=os.environ.get("EDIT_TITLE", True)
    if EDIT_TITLE=="False":
        EDIT_TITLE=None
        LOGGER.warning("VC Title Editing Turned OFF !")
    IS_NONSTOP_STREAM=os.environ.get("IS_NONSTOP_STREAM", True)
    if IS_NONSTOP_STREAM=="False":
        IS_NONSTOP_STREAM=None
        LOGGER.warning("Nonstop 24x7 Live Stream Disabled !")
    THUMB_LINK=os.environ.get("THUMB_LINK", "https://telegra.ph/file/117de96dbfbfea2ce59a6.png")

    # Extra Variables ( For Heroku )

    API_KEY = os.environ.get("HEROKU_API_KEY", None)
    APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    if not API_KEY or \
       not APP_NAME:
       HEROKU_APP=None
    else:
       HEROKU_APP=heroku3.from_key(API_KEY).apps()[APP_NAME]

    # Database Variables ( Don't Touch )

    msg = {}
    playlist=[]
    DUR={}
    DATA={}
    GET_FILE={}
    STREAM_END={}
    FFMPEG_PROCESSES={}
    PAUSE=False
    MUTED=False
    STREAM_LINK=False
    ADMIN_CACHE=False
    CALL_STATUS=False
