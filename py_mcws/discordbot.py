import discord
from discord.ext import commands, tasks


class discord_bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=command_prefix,
            activity=discord.Activity(
                name="py-mcws", type=discord.ActivityType.watching
            ),
        )