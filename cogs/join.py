import discord
from discord.ext import commands

class Join(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        
    @client.event
    async def on_memeber_join(member):
        print(f"Terrific 😃{member} has joined the server!")

    @client.event
    async def on_member_join(member):(
        print(f"Sadly,🥺 {member} has left the server.")


def setup(client):
    client.add_cog(Join(client))