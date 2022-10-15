import nextcord
from nextcord.ext import commands
from nextcord.ui import Button, View
import os, asyncio, random
from dotenv import load_dotenv

# import env & assign to TOKEN variable
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# assign intents for discord
intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

toggler = False

@bot.command(name="color_off")
async def sevenOffCommand(ctx):
    global toggler
    toggler = False
    colorful_role_id = 1030579061585629214
    colorful_role = ctx.author.get_role(colorful_role_id)
    await colorful_role.edit(color=nextcord.Color.from_rgb(255, 0, 0))
    await ctx.send("Colorful Role Deactivated")

@bot.command(name="color_on")
async def sevenCommand(ctx):
    if ctx.author.discriminator != "8000":
        return
    global toggler
    toggler = True
    num = 0
    rainbow = [
        nextcord.Color.from_rgb(255, 0, 0),
        nextcord.Color.orange(),
        nextcord.Color.yellow(),
        nextcord.Color.green(),
        nextcord.Color.blue(),
        nextcord.Color.purple(),
        nextcord.Color.fuchsia()
    ]
    colorful_role_id = 1030579061585629214
    colorful_role = ctx.author.get_role(colorful_role_id)
    await ctx.send("Colorful Role Activated")
    while toggler:
        thisColor = rainbow[num%len(rainbow)]
        await colorful_role.edit(color=thisColor)
        await asyncio.sleep(0.3)
        num += 1

if __name__ == '__main__':
    bot.run(TOKEN)