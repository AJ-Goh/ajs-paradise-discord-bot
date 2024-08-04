# List of commands here:
# 1. test
# 2. ping
# 3. changelog
# 4. messagefilecheck
# 5. emojifilecheck

import discord, misc.messages, misc.emoji
from discord import app_commands
from discord.ext import commands

Administrators = [
    641724025780830220,
    832811319957651457
]

def fList(l):
    formatted_list = "{\n"
    for item in l:
        formatted_list += f'"{item}",\n'
    formatted_list += "}"
    return formatted_list

def fDict(d):
    formatted_dict = "{\n"
    for key, value_list in d.items():
        formatted_dict += f"  {key}: [\n"
        formatted_dict += ",\n".join(f"    {item}" for item in value_list)
        formatted_dict += "\n  ],\n"
    formatted_dict += "}"
    return formatted_dict

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
    e = discord.Embed(title=misc.messages.CHANGELOG_LIST[0],
                      description=misc.messages.CHANGELOG_LIST[3],
                      colour=0xFFCC00)
    e.set_author(name=f"{self.bot.user}")
    e.set_footer(text=misc.messages.CHANGELOG_LIST[1] + " · " + misc.messages.CHANGELOG_LIST[2] + " GMT")
    await interaction.response.send_message(embed=e)
  
  @app_commands.command(
    name="messagefilecheck",
    description="(Administrator Only) Checks the contents of the bot's misc/messages.py file.")
  @app_commands.describe(
    item = "Input the desired item of the file.")
  @app_commands.choices(item = [
    app_commands.Choice(name= "CHANGELOG_LIST", value= "c"),
    app_commands.Choice(name= "WELCOME_MESSAGE", value= "w"),
    app_commands.Choice(name= "WELCOME_MESSAGE_STAFF", value= "s"),
    app_commands.Choice(name= "WELCOME_MESSAGE_NONE", value= "n"),
    app_commands.Choice(name= "GOODBYE_MESSAGE", value= "g"),
    app_commands.Choice(name= "NINETYNINE_DESC", value= "d"),
    app_commands.Choice(name= "HIGHLOWINF_DESC", value= "h"),
    app_commands.Choice(name= "SERVER_RULES", value= "r"),
    app_commands.Choice(name= "STAFF_APPS_QNS (mod, modp)", value= "q1"),
    app_commands.Choice(name= "STAFF_APPS_QNS (com, comp)", value= "q2"),
    app_commands.Choice(name= "STAFF_APPS_QNS (acm, acmp)", value= "q3"),
    app_commands.Choice(name= "STAFF_APPS_QNS (sem, semp)", value= "q4")
  ])
  async def messagefilecheck(self, interaction: discord.Interaction, item: str):
    if interaction.user.id not in Administrators:
      Embed = discord.Embed(description="You are not an administrator.", color=0xff0000)
      await interaction.response.send_message(embed=Embed)
      return
    if item == "c":
      await interaction.response.send_message(f"```py\n{fList(misc.messages.CHANGELOG_LIST)}\n```")
    elif item == "w":
      await interaction.response.send_message(f'```py\n"""\n{misc.messages.WELCOME_MESSAGE}\n"""\n```')
    elif item == "s":
      await interaction.response.send_message(f'```py\n"""\n{misc.messages.WELCOME_MESSAGE_STAFF}\n"""\n```')
    elif item == "n":
      await interaction.response.send_message(f'```py\n"""\n{misc.messages.WELCOME_MESSAGE_NONE}\n"""\n```')
    elif item == "g":
      await interaction.response.send_message(f'```py\n"""\n{misc.messages.GOODBYE_MESSAGE}\n"""\n```')
    elif item == "d":
      await interaction.response.send_message(misc.messages.NINETYNINE_DESC)
    elif item == "h":
      await interaction.response.send_message(misc.messages.HIGHLOWINF_DESC)
    elif item == "r":
      await interaction.response.send_message(f'```py\n"""\n{misc.messages.SERVER_RULES}\n"""\n```')
    elif item in ["q1", "q2", "q3", "q4"]:
      if item == "q1":
        t = f"```py\n{fList(misc.messages.STAFF_APPS_QNS['mod'])}\n``` "+f"```py\n{fList(misc.messages.STAFF_APPS_QNS['modp'])}\n```"
      elif item == "q2":
        t = f"```py\n{fList(misc.messages.STAFF_APPS_QNS['com'])}\n``` "+f"```py\n{fList(misc.messages.STAFF_APPS_QNS['comp'])}\n```"
      elif item == "q3":
        t = f"```py\n{fList(misc.messages.STAFF_APPS_QNS['acm'])}\n``` "+f"```py\n{fList(misc.messages.STAFF_APPS_QNS['acmp'])}\n```"
      elif item == "q4":
        t = f"```py\n{fList(misc.messages.STAFF_APPS_QNS['sem'])}\n``` "+f"```py\n{fList(misc.messages.STAFF_APPS_QNS['semp'])}\n```"
      else:
        t = "Error: STAFF_APPS_QNS dictionary key not found."
      await interaction.response.send_message(t)
    else:
      await interaction.response.send_message("Error: item not found.")

  @app_commands.command(
    name="emojifilecheck",
    description="(Administrator Only) Checks the contents of the bot's misc/emoji.py file.")
  @app_commands.describe(
    item = "Input the desired item of the file.")
  @app_commands.choices(item = [
    app_commands.Choice(name= "DICE", value= "d"),
    app_commands.Choice(name= "CARDS", value= "c")
  ])
  async def emojifilecheck(self, interaction: discord.Interaction, item: str):
    resend = False
    if interaction.user.id not in Administrators:
      Embed = discord.Embed(description="You are not an administrator.", color=0xff0000)
      await interaction.response.send_message(embed=Embed)
      return
    t = ""
    if item == "d":
      for i in misc.emoji.DICE.values():
        t += i
    elif item == "c":
      for i in misc.emoji.CARDS.values():
        if type(i) == str:
          t += i
        elif type(i) == dict:
          for j in i.values():
            t += j
        else:
          t = "Error: misc.emoji.CARDS.values() does not return str or dict types."
          break
    else:
      t = "Error: item not found."
    await interaction.response.send_message(t)

async def setup(bot):
  await bot.add_cog(SlashCmd_Bot(bot))