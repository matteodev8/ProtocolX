# Copyright matteodev 2022
# ------------------------

import interactions
import dotenv
import os

dotenv.load_dotenv()

bot = interactions.Client(token=os.environ["TOKEN"])

@bot.event
async def on_ready():
    print("Ready.")

bot.start()