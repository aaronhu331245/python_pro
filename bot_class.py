import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hai fatto l\'accesso come {bot.user}')
    

@bot.command()
async def ciao(ctx):
    await ctx.send(f'Ciao! Sono un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def somma(ctx, a = 5):
    await ctx.send(a+1)

@bot.command()
async def somma_param(ctx, numero : int):
    await ctx.send(numero + 123322048482)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def come_stai(ctx):
    await ctx.send(f'bene. faccioi la vita da bot.\U0001f642')

@bot.command()
async def arrivederci(ctx):
    await ctx.send("arrivederci! \U0001f642")

bot.run("inserisci qui il token del tuo bot")
