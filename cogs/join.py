import discord
from discord.ext import commands

class Join(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f"Terrific 😃{member} has joined the server!")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f"Sadly,🥺 {member} has left the server.")


async def setup(client):
    await client.add_cog(Join(client))