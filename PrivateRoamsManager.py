import discord
from discord.ext import commands
from discord.ext.commands import Bot 
import time

bot = commands.Bot(
    command_prefix="?",
    case_insensitive=True
)

bot.author_id = 758364478554898442

@bot.event
async def on_ready():
    print("Bot Online")
    print(bot.user)
    await bot.change_presence(status=discord.Status.idle)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Private Roams"))

@bot.command()
@commands.has_permissions(manage_messages = True)
async def Clear(ctx, amount=0):
    if amount > 0:
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"{ctx.author} Purged {amount} Messages.")
        time.sleep(2)
        await ctx.channel.purge(limit=1)
        channel = bot.get_channel(799195745903181824)
        await channel.send(f"{ctx.author} Purged {amount} Of Messages.")
    elif amount == 0:
        await ctx.send("Purge Command Requires Integer Of Messages To Purge")
        time.sleep(2)
        await ctx.channel.purge(limit=2)

@bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"{member} Kicked For {reason} by {ctx.author} ")
    time.sleep(5)
    await ctx.channel.purge(limit=2)
    channel = bot.get_channel(799195745903181824)
    await channel.send(f"{ctx.author} Kicked {member} For {reason}")

@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"{member} Banned For {reason} by {ctx.author} ")
    time.sleep(5)
    await ctx.channel.purge(limit=2)
    channel = bot.get_channel(799195745903181824)
    await channel.send(f"{ctx.author} Banned {member} For {reason}")

@bot.command()
@commands.has_permissions(kick_members = True)
async def mute(ctx, member : discord.Member, *, reason=None):
    muted_role = ctx.guild.get_role(795122242447081493)
    await member.add_roles(muted_role)
    await ctx.send(f"{ctx.author} Muted {member} for {reason}")
    time.sleep(2)
    await ctx.channel.purge(limit=2)
    channel = bot.get_channel(799195745903181824)
    await channel.send(f"{ctx.author} Muted {member} For {reason}")

@bot.command()
@commands.has_permissions(kick_members = True)
async def mute(ctx, member : discord.Member):
    muted_role = ctx.guild.get_role(795122242447081493)
    await bot.remove_roles(member, muted_role)
    await ctx.send(f"{ctx.author} Unmuted {member}")
    time.sleep(2)
    await ctx.channel.purge(limit=2)
    channel = bot.get_channel(799195745903181824)
    await channel.send(f"{ctx.author} Unmuted {member}")

bot.run("Nzk4ODY5MTY5NTQxMDg3MjMy.X_7S5A.qQ58d0DGLAzcNsViOVUF2qSc4VY")