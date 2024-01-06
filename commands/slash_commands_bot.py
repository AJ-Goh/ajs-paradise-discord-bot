# List of commands here:
# 1. test
# 2. ping
# 3. changelog

import discord
from discord import app_commands
from discord.ext import commands
from misc.messages import CHANGELOG_LIST
from misc.images import AJ_RAINBOW


class SlashCmd_Bot(commands.GroupCog, group_name="bot"):

  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name="test",
                        description="Tests whether the bot is online.")
  async def test_slash(self, interaction: discord.Interaction):
    await interaction.response.send_message(
      f"✅ {self.bot.user} (ID: {self.bot.user.id}) is currently online.")

  @app_commands.command(
    name="ping", description="Tests the latency of the bot in milliseconds.")
  async def ping(self, interaction: discord.Interaction):
    await interaction.response.send_message(
      f"Pong! ({round(self.bot.latency * 1000)}ms)")

  @app_commands.command(
    name="changelog",
    description="Shows the updates for the latest version of the bot.")
  async def changelog(self, interaction: discord.Interaction):
    e = discord.Embed(title=CHANGELOG_LIST[0],
                      description=CHANGELOG_LIST[3],
                      colour=0xFFCC00)
    e.set_author(
      name=f"{self.bot.user}",
      icon_url=AJ_RAINBOW)
    e.set_footer(text=CHANGELOG_LIST[1] + " · " + CHANGELOG_LIST[2] + " GMT")
    await interaction.response.send_message(embed=e)

async def setup(bot):
  await bot.add_cog(SlashCmd_Bot(bot))