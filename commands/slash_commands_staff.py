# List of commands here:
# 1. application

import discord, traceback
from discord import app_commands, ui
from discord.ext import commands
from misc.messages import STAFF_APPS_QNS

class modModal(ui.Modal, title="Server Moderator Application"):
   a1 = ui.TextInput(
      label=STAFF_APPS_QNS["mod"][0],
      placeholder=STAFF_APPS_QNS["modp"][0],
      style=discord.TextStyle.paragraph,
      max_length=1000,
      required=True
      )
   a2 = ui.TextInput(
      label=STAFF_APPS_QNS["mod"][1],
      placeholder=STAFF_APPS_QNS["modp"][1],
      style=discord.TextStyle.paragraph,
      max_length=1000,
      required=True
      )
   a3 = ui.TextInput(
      label=STAFF_APPS_QNS["mod"][2],
      placeholder=STAFF_APPS_QNS["modp"][2],
      style=discord.TextStyle.paragraph,
      max_length=1000,
      required=True
      )
   a4 = ui.TextInput(
      label=STAFF_APPS_QNS["mod"][3],
      placeholder=STAFF_APPS_QNS["modp"][3],
      style=discord.TextStyle.paragraph,
      max_length=1000,
      required=True
      )
   a5 = ui.TextInput(
      label=STAFF_APPS_QNS["mod"][4],
      placeholder=STAFF_APPS_QNS["modp"][4],
      style=discord.TextStyle.paragraph,
      max_length=1000,
      required=False
      )
   async def on_submit(self, interaction: discord.Interaction):
      a = [i.value for i in [self.a1,self.a2,self.a3,self.a4,self.a5]]
      apps_channel = interaction.client.get_channel(1249035682706493510)
      d = f"- Username: **{interaction.user.name}**\n- User ID: ||**`{interaction.user.id}`**||"
      e = discord.Embed(title=f"Application for Server Moderator", description=d, colour=0xe74c3c)
      e.set_footer(text="AJ's Paradise Staff Applications")
      q = STAFF_APPS_QNS["mod"]
      for i, j in zip(q, a):
         e.add_field(name=i, value=j, inline=False)
      await apps_channel.send(embed=e)
      await interaction.response.send_message(f"- Username: **{interaction.user.name}**\n- User ID: ||**`{interaction.user.id}`**||\n\n_Your application for the **Server Moderator** role has been submitted and a copy of your responses will be sent to your DMs. You will be notified within the next 48 hours if your application has been approved._", ephemeral=True)
      apps_user = interaction.client.get_user(interaction.user.id)
      await apps_user.create_dm()
      await apps_user.dm_channel.send(embed=e)
   async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message('Oops! Something went wrong.')
        # Make sure we know what the error actually is
        traceback.print_exception(type(error), error, error.__traceback__)

class comModal(ui.Modal, title="Community Manager Application"):
   a1 = ui.TextInput(
      label=STAFF_APPS_QNS["com"][0],
      placeholder=STAFF_APPS_QNS["comp"][0],
      style=discord.TextStyle.paragraph,
      max_length=1000,
      required=True
      )
   a2 = ui.TextInput(
      label=STAFF_APPS_QNS["com"][1],
      placeholder=STAFF_APPS_QNS["comp"][1],
      style=discord.TextStyle.paragraph,
      max_length=1000,
      required=True
      )
   a3 = ui.TextInput(
      label=STAFF_APPS_QNS["com"][2],
      placeholder=STAFF_APPS_QNS["comp"][2],
      style=discord.TextStyle.paragraph,
      max_length=1000,
      required=True
      )
   a4 = ui.TextInput(
      label=STAFF_APPS_QNS["com"][3],
      placeholder=STAFF_APPS_QNS["comp"][3],
      style=discord.TextStyle.paragraph,
      max_length=1000,
      required=True
      )
   a5 = ui.TextInput(
      label=STAFF_APPS_QNS["com"][4],
      placeholder=STAFF_APPS_QNS["comp"][4],
      style=discord.TextStyle.paragraph,
      max_length=1000,
      required=False
      )
   async def on_submit(self, interaction: discord.Interaction):
      a = [i.value for i in [self.a1,self.a2,self.a3,self.a4,self.a5]]
      apps_channel = interaction.client.get_channel(1249035682706493510)
      d = f"- Username: **{interaction.user.name}**\n- User ID: ||**`{interaction.user.id}`**||"
      e = discord.Embed(title=f"Application for Community Manager", description=d, colour=0x9b59b6)
      e.set_footer(text="AJ's Paradise Staff Applications")
      q = STAFF_APPS_QNS["com"]
      for i, j in zip(q, a):
         e.add_field(name=i, value=j, inline=False)
      await apps_channel.send(embed=e)
      await interaction.response.send_message(f"- Username: **{interaction.user.name}**\n- User ID: ||**`{interaction.user.id}`**||\n\n_Your application for the **Community Manager** role has been submitted and a copy of your responses will be sent to your DMs. You will be notified within the next 48 hours if your application has been approved._", ephemeral=True)
      apps_user = interaction.client.get_user(interaction.user.id)
      await apps_user.create_dm()
      await apps_user.dm_channel.send(embed=e)
   async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message('Oops! Something went wrong.')
        # Make sure we know what the error actually is
        traceback.print_exception(type(error), error, error.__traceback__)

class acmModal(ui.Modal, title="AJ Clan Manager Application"):
   a1 = ui.TextInput(
      label=STAFF_APPS_QNS["acm"][0],
      placeholder=STAFF_APPS_QNS["acmp"][0],
      style=discord.TextStyle.paragraph,
      max_length=1000,
      required=True
      )
   a2 = ui.TextInput(
      label=STAFF_APPS_QNS["acm"][1],
      placeholder=STAFF_APPS_QNS["acmp"][1],
      style=discord.TextStyle.paragraph,
      max_length=1000,
      required=True
      )
   a3 = ui.TextInput(
      label=STAFF_APPS_QNS["acm"][2],
      placeholder=STAFF_APPS_QNS["acmp"][2],
      style=discord.TextStyle.paragraph,
      max_length=1000,
      required=True
      )
   a4 = ui.TextInput(
      label=STAFF_APPS_QNS["acm"][3],
      placeholder=STAFF_APPS_QNS["acmp"][3],
      style=discord.TextStyle.paragraph,
      max_length=1000,
      required=True
      )
   a5 = ui.TextInput(
      label=STAFF_APPS_QNS["acm"][4],
      placeholder=STAFF_APPS_QNS["acmp"][4],
      style=discord.TextStyle.paragraph,
      max_length=1000,
      required=False
      )
   async def on_submit(self, interaction: discord.Interaction):
      a = [i.value for i in [self.a1,self.a2,self.a3,self.a4,self.a5]]
      apps_channel = interaction.client.get_channel(1249035682706493510)
      d = f"- Username: **{interaction.user.name}**\n- User ID: ||**`{interaction.user.id}`**||"
      e = discord.Embed(title=f"Application for AJ Clan Manager", description=d, colour=0xe91e63)
      e.set_footer(text="AJ's Paradise Staff Applications")
      q = STAFF_APPS_QNS["acm"]
      for i, j in zip(q, a):
         e.add_field(name=i, value=j, inline=False)
      await apps_channel.send(embed=e)
      await interaction.response.send_message(f"- Username: **{interaction.user.name}**\n- User ID: ||**`{interaction.user.id}`**||\n\n_Your application for the **AJ Clan Manager** role has been submitted and a copy of your responses will be sent to your DMs. You will be notified within the next 48 hours if your application has been approved._", ephemeral=True)
      apps_user = interaction.client.get_user(interaction.user.id)
      await apps_user.create_dm()
      await apps_user.dm_channel.send(embed=e)
   async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message('Oops! Something went wrong.')
        # Make sure we know what the error actually is
        traceback.print_exception(type(error), error, error.__traceback__)

class semModal(ui.Modal, title="Server Events Manager Application"):
   a1 = ui.TextInput(
      label=STAFF_APPS_QNS["sem"][0],
      placeholder=STAFF_APPS_QNS["semp"][0],
      style=discord.TextStyle.paragraph,
      max_length=1000,
      required=True
      )
   a2 = ui.TextInput(
      label=STAFF_APPS_QNS["sem"][1],
      placeholder=STAFF_APPS_QNS["semp"][1],
      style=discord.TextStyle.paragraph,
      max_length=1000,
      required=True
      )
   a3 = ui.TextInput(
      label=STAFF_APPS_QNS["sem"][2],
      placeholder=STAFF_APPS_QNS["semp"][2],
      style=discord.TextStyle.paragraph,
      max_length=1000,
      required=True
      )
   a4 = ui.TextInput(
      label=STAFF_APPS_QNS["sem"][3],
      placeholder=STAFF_APPS_QNS["semp"][3],
      style=discord.TextStyle.paragraph,
      max_length=1000,
      required=True
      )
   a5 = ui.TextInput(
      label=STAFF_APPS_QNS["sem"][4],
      placeholder=STAFF_APPS_QNS["semp"][4],
      style=discord.TextStyle.paragraph,
      max_length=1000,
      required=False
      )
   async def on_submit(self, interaction: discord.Interaction):
      a = [i.value for i in [self.a1,self.a2,self.a3,self.a4,self.a5]]
      apps_channel = interaction.client.get_channel(1249035682706493510)
      d = f"- Username: **{interaction.user.name}**\n- User ID: ||**`{interaction.user.id}`**||"
      e = discord.Embed(title=f"Application for Server Events Manager", description=d, colour=0xe67e22)
      e.set_footer(text="AJ's Paradise Staff Applications")
      q = STAFF_APPS_QNS["sem"]
      for i, j in zip(q, a):
         e.add_field(name=i, value=j, inline=False)
      await apps_channel.send(embed=e)
      await interaction.response.send_message(f"- Username: **{interaction.user.name}**\n- User ID: ||**`{interaction.user.id}`**||\n\n_Your application for the **Server Events Manager** role has been submitted and a copy of your responses will be sent to your DMs. You will be notified within the next 48 hours if your application has been approved._", ephemeral=True)
      apps_user = interaction.client.get_user(interaction.user.id)
      await apps_user.create_dm()
      await apps_user.dm_channel.send(embed=e)
   async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message('Oops! Something went wrong.')
        # Make sure we know what the error actually is
        traceback.print_exception(type(error), error, error.__traceback__)

class SlashCmd_Staff(commands.GroupCog, group_name="staff"):
  def __init__(self, bot):
      self.bot = bot

  @app_commands.command(name="application", description="Apply to be a part of the staff team in AJ's Paradise!")
  @app_commands.describe(role="Select the staff role you would like to apply for.")
  @app_commands.choices(role = [
    app_commands.Choice(name="Server Moderator", value="mod"),
    app_commands.Choice(name="Community Manager", value="com"),
    app_commands.Choice(name="AJ Clan Manager", value="acm"),
    app_commands.Choice(name="Server Events Manager", value="sem")
  ])
  async def application(self, interaction: discord.Interaction, role: str):
    if role == "mod":
       try:
         await interaction.response.send_modal(modModal())
       except Exception as e:
         await interaction.response.send_message(e)
    elif role == "com":
       try:
         await interaction.response.send_modal(comModal())
       except Exception as e:
         await interaction.response.send_message(e)
    elif role == "acm":
       try:
         await interaction.response.send_modal(acmModal())
       except Exception as e:
         await interaction.response.send_message(e)
    elif role == "sem":
       try:
         await interaction.response.send_modal(semModal())
       except Exception as e:
         await interaction.response.send_message(e)

async def setup(bot):
  await bot.add_cog(SlashCmd_Staff(bot))