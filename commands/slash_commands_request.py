# List of commands here:
# 1. feature
# 2. sponsor
# 3. drop

import discord
from discord.ext import commands
from discord import app_commands

class SlashCmd_Request(commands.GroupCog, group_name="request"):

  def __init__(self, bot):
    self.bot = bot

  @app_commands.command(name="feature", description="Request a feature to be added to this bot.")
  @app_commands.describe(feature = "State and describe the feature you would like to request.")
  async def feature(self, interaction: discord.Interaction, feature: str):
    aj_user = self.bot.get_user(832811319957651457)
    await aj_user.create_dm()
    await aj_user.dm_channel.send(f"## 🔵 Feature Request\n- **USER**  {interaction.user.name} ||`ID: {interaction.user.id}`||\n- **REQUEST**  {feature}")
    req_channel = self.bot.get_channel(1211678134412517427)
    await req_channel.send(f"## ⚙️ Feature Request\n- **USER**  {interaction.user.name} ||`ID: {interaction.user.id}`||\n- **REQUEST**  {feature}")
    e = discord.Embed(title="Feature Request Sent ✓", description=f"- {feature}", colour=0xffcc00)
    await interaction.response.send_message(embed=e)

  @app_commands.command(name="sponsor", description="Request to host a sponsored item in AJ's Paradise.")
  @app_commands.describe(
    type = "State the type of the sponsored item.",
    details = "State the name and give details regarding your sponsored item.",
    datetime = "State the date and time of when the sponsored item is hosted.",
    prize = "State the prize(s) offered for the sponsored item.",
    numberofwinners = "State the number of winners for the sponsored item."
    )
  @app_commands.choices(type = [
    app_commands.Choice(name= "Event or Minigame", value= "Event or Minigame"),
    app_commands.Choice(name= "Giveaway or Raffle", value= "Giveaway or Raffle"),
    app_commands.Choice(name= "Other", value= "Other")
  ])
  async def sponsor(self, interaction: discord.Interaction, type: str, details: str, datetime: str, prize: str, numberofwinners: int):
    aj_user = self.bot.get_user(832811319957651457)
    await aj_user.create_dm()
    await aj_user.dm_channel.send(f"## 🟣 Sponsor Request\n- **HOST**  {interaction.user.name} ||`ID: {interaction.user.id}`||\n- **TYPE**  {type}\n- **DETAILS**  {details}\n- **DATE AND TIME**  {datetime}\n- **PRIZE**  {prize}\n- **NUMBER OF WINNERS**  {numberofwinners}")
    req_channel = self.bot.get_channel(1211678134412517427)
    await req_channel.send(f"## 💸 Sponsor Request\n- **HOST**  {interaction.user.name} ||`ID: {interaction.user.id}`||\n- **TYPE**  {type}\n- **DETAILS**  {details}\n- **DATE AND TIME**  {datetime}\n- **PRIZE**  {prize}\n- **NUMBER OF WINNERS**  {numberofwinners}")
    e = discord.Embed(title="Sponsor Request Sent ✓", description=f"- **HOST**  {interaction.user.name} ||`ID: {interaction.user.id}`||\n- **TYPE**  {type}\n- **DETAILS**  {details}\n- **DATE AND TIME**  {datetime}\n- **PRIZE**  {prize}\n- **NUMBER OF WINNERS**  {numberofwinners}", colour=0xffcc00)
    await interaction.response.send_message(embed=e)

  @app_commands.command(name="drop", description="Request to host a sudden drop in AJ's Paradise.")
  @app_commands.describe(
    details = "State the name and give details regarding your drop.",
    prize = "State the prize(s) offered for the drop.",
    numberofwinners = "State the number of winners for the drop."
    )
  async def drop(self, interaction: discord.Interaction, details: str, prize: str, numberofwinners: int):
    aj_user = self.bot.get_user(832811319957651457)
    await aj_user.create_dm()
    await aj_user.dm_channel.send(f"## 🔴 Drop Request\n- **HOST**  {interaction.user.name} ||`ID: {interaction.user.id}`||\n- **DETAILS**  {details}\n- **PRIZE**  {prize}\n- **NUMBER OF WINNERS**  {numberofwinners}")
    req_channel = self.bot.get_channel(1211678134412517427)
    await req_channel.send(f"## 💰 Drop Request\n- **HOST**  {interaction.user.name} ||`ID: {interaction.user.id}`||\n- **DETAILS**  {details}\n- **PRIZE**  {prize}\n- **NUMBER OF WINNERS**  {numberofwinners}")
    e = discord.Embed(title="Drop Request Sent ✓", description=f"- **HOST**  {interaction.user.name} ||`ID: {interaction.user.id}`||\n- **DETAILS**  {details}\n- **PRIZE**  {prize}\n- **NUMBER OF WINNERS**  {numberofwinners}", colour=0xffcc00)
    await interaction.response.send_message(embed=e)
    
async def setup(bot):
  await bot.add_cog(SlashCmd_Request(bot))