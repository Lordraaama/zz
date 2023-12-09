from pyrogram import Client, filters
from pyrogram.types import InputFile
from watermark_bot import add_watermark
from db import Database
import os

API_ID = 27327455
API_HASH = "0b60d99056b4d168b1bd717aeb7a699b"
BOT_TOKEN = "6884087876:AAExZncJ6v6WumKpQ5OD2oIEngTQNKknKPE"
MONGODB_URL = "mongodb+srv://mswpresents01:O1mAmjU4SHgEergF@cluster0.swcwpvm.mongodb.net/?retryWrites=true&w=majority"  # Replace with your actual MongoDB URL
FORCE_SUB_CHANNEL = "mswpresents"  # Replace with your force subscription channel username

app = Client("video_watermark_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
db = Database(MONGODB_URL)

# Add your event handlers here...

def main() -> None:
    app.run()

if __name__ == '__main__':
    main()
