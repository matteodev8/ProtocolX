# Copyright matteodev 2022
# ------------------------

import interactions
import dotenv
import os

dotenv.load_dotenv()

bot = interactions.Client(token=os.environ["TOKEN"])
gID = int(os.environ["DEV_GUILD"])

@bot.event
async def on_ready():
    print("Ready.")

# I'll move this to a different folder later
@bot.command(
    name="ping",
    description="Replies with the current latency.",
    scope=gID,
)
async def ping(ctx: interactions.CommandContext):
    await ctx.send(f"Pong! {round(bot.latency)}ms")

bot.start()