import discord
import random
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık.')

@bot.command(name='bilgi', help='Botun kurucu bilgisini verir.')
async def bilgi(ctx):
    bilgi_cvp = "Bu Bot, Bor Madenci 64 tarafından yapılmıştır. Botun yapılışı için https://github.com/Abdulhamit-Ocak/discord-boru/new/main adresini ziyaret edebilirsiniz!"

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pingim : `{bot.latency * 1000}`ms')

@bot.event()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command(pass_context=True)
@bot.commands.has_permissions(manage_roles=True)
async def rolekle(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)
    await ctx.send(f"{ctx.author.name}, {user.name} isimli üyeye bir rol verdi: {role.name}")

@bot.command
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('*merhaba'):
        await message.channel.send("Selam!")
    elif message.content.startswith('*bye'):
        await message.channel.send("\\U0001f642")
    else:
        await message.channel.send(message.content)

@bot.event
async def on_ready():
    activity = discord.Game(name="!yardım")
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print("Bot çalışıyor.")

@bot.command(pass_context=True)
async def kick(ctx, member: discord.Member, *, reason="Kural Çiğneme"): # kullanıcıyı atma komutu
    await bot.kick(member) # atma
    await ctx.send(f'{member} kullanıcısı yasaklandı') # mesaj gönderme

bot.run("MTI3Njk3NTk1OTAwMTY2MTU2Mw.GduWNC.2twYa05HgVgA_YvU9ICAz_Hx9jL4uN_osWRu2c")
