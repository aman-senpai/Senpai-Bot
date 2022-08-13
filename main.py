import discord
import random
import os
import json
from discord.ext import commands, tasks
from itertools import cycle
token = os.environ["Senpai_bot"]

def get_prefix(client, message):
    with open('prefixes.json', "r") as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix=get_prefix)
status = cycle(["Online", "AFK", "Busy not Giving fuck"])


# Events
@client.event
async def on_guild_join(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    
    prefixes[str(guild.id)] = "."

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)


@client.event
async def on_guild_remove(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    
    prefixes.pop(str(guild.id))

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)

@client.command()
async def change_prefix(ctx, prefix):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    
    prefixes[str(ctx.guild.id)] = prefix

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)
    
    await ctx.send(f"Prefix changed to {prefix}")

@client.event
async def on_ready():
    change_status.start()

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid command used!")
    if isinstance(error, commands.errors.MissingPermissions):
        await ctx.send("You don't have the permission!")

def is_it_me(ctx):
    return ctx.author.id == 452519901798727716

@client.command()
@commands.check(is_it_me)
async def example(ctx):
    await ctx.send(f"I'm the {ctx.author}")


@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please specify the amount of messages to be deleted.")


@tasks.loop(seconds= 10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"{extension} liberary loaded")

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    await ctx.send(f"{extension} liberary unloaded")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run(token)
