# List of commands here:
# 1. stats
# 2. cashin
# 3. cashout
# 4. decadice
# 5. blackjack

import discord, json
from discord import app_commands
from discord.ext import commands
from datetime import datetime
from misc.emoji import DICE, CARDS

# INSUFFICIENT BALANCE EMBED

def balanceembed(balance):
  e = discord.Embed(
    title= "Insufficient Balance",
    description= f"Chat to earn message levels and cash in more chips with the </cashin:1268938561416335513> command.",
  	colour= 0xff0000)
  e.set_footer(text= f"Your Balance: {balance} Chips")
  return e

# COMMAND LIMIT EMBED

def limitembed(limit):
  e = discord.Embed(
    title= "Daily Limit Reached",
    description= f"You have reached the daily limit for this command; try again tomorrow.",
  	colour= 0xff0000)
  e.set_footer(text= f"Daily Limit: {limit}")
  return e

# COMMAND ERROR EMBED

def errorembed(error):
  e = discord.Embed(
    title= "Error",
    description= f"An error has occured: `{error}`",
  	colour= 0xff0000)
  return e

# COMMAND LIMIT CHECK

def check(user, cmd, limit):
  with open('data/data_chance_cd.json', mode='r') as infile:
    data = json.load(infile)
  # Check if the date has changed and reset if necessary
  if data.get("date") != datetime.now().strftime("%D"):
    data = {"date": datetime.now().strftime("%D")}
  try:
    if data[str(user)][cmd] == limit:
      return [False,"Limit"]
    elif data[str(user)][cmd] < limit:
      data[str(user)][cmd] += 1
      with open("data/data_chance_cd.json", mode="w") as outfile:
        json.dump(data, outfile, indent=2)
      return [True,"Pass"]
    elif type(data[str(user)][cmd]) == int:
      return [False, f"(Invalid integer value) data['{user}']['{cmd}'] = {data[str(user)][cmd]}"]
    else:
      return [False, f"(Invalid data type) data['{user}']['{cmd}'] = {data[str(user)][cmd]}"]
  except KeyError:
    data[str(user)] = {cmd: 1}
    with open("data/data_chance_cd.json", mode="w") as outfile:
      json.dump(data, outfile, indent=2)
    return [True,"Pass"]
  except Exception as e:
    return [False, str(e)]

# COMMAND ACCESS CHECK

async def access(interaction: discord.Interaction, cmd: str, limit: int, bet: int):
  Check = check(interaction.user.id, cmd, limit)
  if Check[0]:
    with open('data/data_chance.json', mode='r') as infile:
      data = json.load(infile)
    
    # Initialize userdata if it's None
    if str(interaction.user.id) not in data:
      data[str(interaction.user.id)] = {"Chips": [0, 0, 0], "Games": {}}
      with open("data/data_chance.json", mode="w") as outfile:
        json.dump(data, outfile, indent=2)
      with open('data/data_chance_cd.json', mode='r') as infile:
        data = json.load(infile)
      data[str(interaction.user.id)][cmd] -= 1
      with open("data/data_chance_cd.json", mode="w") as outfile:
        json.dump(data, outfile, indent=2)
      e = balanceembed(0)
      await interaction.response.send_message(embed=e)
      return False
    
    userdata = data[str(interaction.user.id)]

    # Check if the user has enough chips
    if userdata["Chips"][0] < bet:
      e = balanceembed(userdata["Chips"][0])
      await interaction.response.send_message(embed=e)
      with open('data/data_chance_cd.json', mode='r') as infile:
        data = json.load(infile)
      data[str(interaction.user.id)][cmd] -= 1
      with open("data/data_chance_cd.json", mode="w") as outfile:
        json.dump(data, outfile, indent=2)
      return False

    # Initialize game data if necessary
    if cmd not in userdata["Games"]:
      userdata["Games"][cmd] = [1, 0, 0]
    else:
      userdata["Games"][cmd][0] += 1
    
    userdata["Chips"][0] -= bet

    # Save the updated data
    with open("data/data_chance.json", mode="w") as outfile:
      json.dump(data, outfile, indent=2)

    return True

  else:
    if Check[1] == "Limit":
      e = limitembed(limit)
      await interaction.response.send_message(embed=e)
    else:
      e = errorembed(Check[1])
      await interaction.response.send_message(embed=e, ephemeral=True)
    return False

# GAME WIN FUNCTION

def win(interaction, cmd, chips):
  with open('data/data_chance.json', mode='r') as infile:
    data = json.load(infile)
  userdata = data[str(interaction.user.id)]
  userdata["Chips"][0] += chips
  userdata["Games"][cmd][1] += 1
  userdata["Games"][cmd][2] += chips
  with open("data/data_chance.json", mode="w") as outfile:
    json.dump(data, outfile, indent=2)

# CHANCE GROUPCOG

class SlashCmd_Chance(commands.GroupCog, group_name="chance"):
  def __init__(self, bot):
      self.bot = bot
  
  @app_commands.command(name="stats", description="View a user's chance statistics.")
  @app_commands.describe(user="Input the target user.")
  async def stats(self, interaction: discord.Interaction, user:discord.User=None):
    if user == None:
      user = interaction.user
    with open('data/data_chance.json', mode='r') as infile:
      data = json.load(infile)
    # Initialize userdata if it's None
    if str(interaction.user.id) not in data:
      data[str(interaction.user.id)] = {"Chips": [0, 0, 0], "Games": {}}
      with open("data/data_chance.json", mode="w") as outfile:
        json.dump(data, outfile, indent=2)
    userchips = data[str(interaction.user.id)]["Chips"]
    usergames = ""
    for key,val in data[str(interaction.user.id)]["Games"].items():
      usergames += f"- /{key}: **{val[0]}** Plays, **{val[1]}** Wins (**{val[2]}** Chips)\n"
    e = discord.Embed(
    		title=f"{interaction.user.name}'s chance statistics",
    		description=f"Username: {interaction.user.global_name} (@{interaction.user.name})\n User ID: ||`{interaction.user.id}`||",
    		colour=0xffcc00)
    e.add_field(
    		name="Chips",
    		value=f"- Balance: **{userchips[0]}**\n- Winnings: **{userchips[0]-userchips[1]+userchips[2]}**\n- Cashed In: **{userchips[1]}**\n- Cashed Out: **{userchips[2]}**")
    e.add_field(
    		name="Games",
    		value=usergames)
    await interaction.response.send_message(embed=e)

  @app_commands.command(name="decadice", description="Roll 10 dice and get special combinations. (Daily limit: 3)")
  @app_commands.describe(bet="State the number of chips you want to bet.")
  async def decadice(self, interaction: discord.Interaction, bet:int):

    Access = await access(interaction, "decadice", 3, bet)
    if not Access: return

    with open('data/data_chance_cd.json', mode='r') as infile:
      data1 = json.load(infile)
    with open('data/data_chance.json', mode='r') as infile:
      data2 = json.load(infile)
    await interaction.response.send_message(str(data1)+"\n \n"+str(data2))



async def setup(bot):
  await bot.add_cog(SlashCmd_Chance(bot))