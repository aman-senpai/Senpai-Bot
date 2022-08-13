import discord
from discord.ext import commands

class Example(commands.Cog):
    
    def __init(self, client):
        self.client = client
    
    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is online!")
    
    # Commands
    @commands.command()
    async def ping(self, ctx,):
        await ctx.send(f"Pong! ")



def setup(client):
    client.add_cog(Example(client))
