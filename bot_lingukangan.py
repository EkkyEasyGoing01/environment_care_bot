#Class bot
import discord
from discord.ext import commands
import random, os

intents = discord.Intents.default()
intents.message_content = True

#kenalkan bot-nya
bot = commands.Bot(command_prefix='$', intents=intents)

#buat reaksi si bot
@bot.event #agar bot bereaksi jika bot siap!
async def on_ready():
    print("Bot telah siap!")

@bot.command()
async def idesampah(ctx):
    img_name = random.choice(os.listdir("kerajinan"))
    with open (f'kerajinan/{img_name}', 'rb') as gambar: #membuka file gambar dan disimpan di variavbel
        picture = discord.File(gambar)
    await ctx.send(file = picture)

bot.run('your token here') #masukkan token-mu disini
