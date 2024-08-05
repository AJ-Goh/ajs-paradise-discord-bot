# List of commands here:
# 1. stats
# 2. cashin
# 3. cashout
# 4. decadice
# 5. blackjack

import discord, json, random
from discord import app_commands
from discord.ext import commands
from datetime import datetime
from misc.emoji import DICE, CARDS

# LOW BET EMBED

def lowbetembed(bet):
  e = discord.Embed(
    title= "Bet Too Low",
    description= f"You must bet at least 1 chip.",
  	colour= 0xff0000)
  e.set_footer(text= f"Your Bet: {bet} Chips")
  return e

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
  if bet <= 0:
    e = lowbetembed(bet)
    await interaction.response.send_message(embed=e)
    return False
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

# DECADICE COMBINATIONS

def num_decadice(dice:list[int], nums:list[int]) -> bool:
  if len(dice) < 10:
    return False
  for die in dice:
    if die not in nums:
      return False
  return True
def num_of_a_kind(dice:list[int], num:int) -> bool:
  if len(dice) < num:
    return False
  counts = [0] * 7  # Index 0 is unused
  for die in dice:
    counts[die] += 1
  for item in counts:
    if item >= num:
      return True
  return False
def little_red_dot(dice: list[int]) -> bool:
  count_of_ones = dice.count(1)
  return count_of_ones == 1
def sequence_straight(dice:list[int], sequence:list[int]) -> bool: # Sliding window approach
  reverse = sequence[::-1]
  length = len(sequence)
  for i in range(len(dice) - length + 1): # Check each consecutive sublist of length len(dice)
    sublist = dice[i:i + length]
    if sublist == sequence or sublist == reverse:
      return True
  return False
def all_paired_up(dice: list[int]) -> bool:
  if len(dice) < 10:
    return False
  counts = [0] * 7 # Index 0 is unused
  for die in dice:
    counts[die] += 1
  return all(count in [0, 2] for count in counts[1:])

# DECADICE DICE ASSESSMENT FUNCTION

def decadice_assess(dice: list[int]) -> list[str, int]:
  if num_decadice(dice, [6]):
    return ["DecaDice Gold", 100]
  elif num_decadice(dice, [1]):
    return ["DecaDice Red", 90]
  elif num_of_a_kind(dice, 10):
    return ["DecaDice", 75]
  elif num_of_a_kind(dice, 9):
    return ["Nine-of-a-Kind", 50]
  elif num_of_a_kind(dice, 8):
    return ["Eight-of-a-Kind", 40]
  elif sequence_straight(dice, [1,2,3,4,5,6]):
    return ["Full Straight", 30]
  elif num_decadice(dice, [4,5,6]):
    return ["High Rolls", 25]
  elif num_decadice(dice, [1,2,3]):
    return ["Low Rolls", 25]
  elif num_decadice(dice, [2,4,6]):
    return ["Even Rolls", 20]
  elif num_decadice(dice, [1,3,5]):
    return ["Odd Rolls", 20]
  elif num_of_a_kind(dice, 7):
    return ["Seven-of-a-Kind", 14]
  elif num_of_a_kind(dice, 6):
    return ["Six-of-a-Kind", 6]
  elif all_paired_up(dice):
    return ["All Paired Up", 5]
  elif num_decadice(dice, [2,3,4,5]):
    return ["All Black", 5]
  elif num_of_a_kind(dice, 5):
    return ["Five-of-a-Kind", 3]
  elif sequence_straight(dice, [4,5,6]):
    return ["High Straight", 1]
  elif sequence_straight(dice, [1,2,3]):
    return ["Low Straight", 1]
  elif little_red_dot(dice):
    return ["Little Red Dot", 1]
  elif num_of_a_kind(dice, 4):
    return ["Four-of-a-Kind", 1]
  else:
    return ["None", 0]

# DECADICE COMBINATION EMBED FIELDS

DECADICE = {
  "Misc":f"""
- **0X** No Combinations
- **1X** Little Red Dot {DICE[1]}
- **5X** All Black {DICE[2]} {DICE[3]} {DICE[4]} {DICE[5]} ...
- **5X** All Paired Up {DICE[1]} {DICE[1]} {DICE[3]} {DICE[3]} {DICE[4]} {DICE[4]} {DICE[5]} {DICE[5]} {DICE[6]} {DICE[6]}
  """,
  "Straights":f"""
- **1X** Low Straight {DICE[1]} {DICE[2]} {DICE[3]}
- **1X** High Straight {DICE[4]} {DICE[5]} {DICE[6]}
- **30X** Full Straight {DICE[1]} {DICE[2]} {DICE[3]} {DICE[4]} {DICE[5]} {DICE[6]}
  """,
  "Rolls":f"""
- **20X** Odd Rolls {DICE[1]} {DICE[3]} {DICE[5]} ...
- **20X** Even Rolls {DICE[2]} {DICE[4]} {DICE[6]} ...
- **25X** Low Rolls {DICE[1]} {DICE[2]} {DICE[3]} ...
- **25X** High Rolls {DICE[4]} {DICE[5]} {DICE[6]} ...
  """,
  "N-of-a-Kind":f"""
- **1X** Four-of-a-Kind {DICE[2]} {DICE[2]} {DICE[2]} ... ×4
- **3X** Five-of-a-Kind {DICE[4]} {DICE[4]} {DICE[4]} ... ×5
- **6X** Six-of-a-Kind {DICE[3]} {DICE[3]} {DICE[3]} ... ×6
- **14X** Seven-of-a-Kind {DICE[5]} {DICE[5]} {DICE[5]} ... ×7
- **40X** Eight-of-a-Kind {DICE[3]} {DICE[3]} {DICE[3]} ... ×8
- **50X** Nine-of-a-Kind {DICE[4]} {DICE[4]} {DICE[4]} ... ×9
  """,
  "DecaDice":f"""
- **75X** DecaDice {DICE[3]} {DICE[3]} {DICE[3]} ... ×10
- **90X** DecaDice Red {DICE[1]} {DICE[1]} {DICE[1]} ... ×10
- **100X** DecaDice Gold {DICE[6]} {DICE[6]} {DICE[6]} ... ×10
  """
}

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

  @app_commands.command(name="decadice", description="Roll 10 dice and get special combinations. (Daily limit: 2)")
  @app_commands.describe(bet="State the number of chips you want to bet.")
  async def decadice(self, interaction: discord.Interaction, bet:int):

    Access = await access(interaction, "decadice", 2, bet)
    if not Access: return

    with open('data/data_chance_cd.json', mode='r') as infile:
      limit = json.load(infile)
    tries = "tries"
    if limit[str(interaction.user.id)]['decadice'] == 2:
      tries = "try"
    footer = f"{3-(limit[str(interaction.user.id)]['decadice'])} {tries} remaining"
    title = f"DecaDice: {interaction.user.name}"
    e = discord.Embed(
      title= title,
      colour= 0xffcc00)
    e.set_footer(text=footer)
    for key,val in DECADICE.items():
      e.add_field(name=key, value=val, inline=False)
    await interaction.response.send_message(embed=e)
    
    dice = []
    for _ in range(10):
      dice.append(random.randint(1,6))
    desc = "#"
    for i in dice:
      desc += " "+DICE[i]
      e = discord.Embed(
        title= title,
        description= desc,
        colour= 0xffcc00)
      e.set_footer(text=footer)
      for key,val in DECADICE.items():
        e.add_field(name=key, value=val, inline=False)
      await interaction.edit_original_response(embed=e)
    best = decadice_assess(dice)
    desc += f" \n Best Combination: {best[0]} (**{best[1]*bet}** Chips)"
    e = discord.Embed(
      title= title,
      description= desc,
      colour= 0xffcc00)
    e.set_footer(text=footer)
    for key,val in DECADICE.items():
      e.add_field(name=key, value=val, inline=False)
    if best[1] != 0:
      win(interaction, "decadice", best[1]*bet)
    await interaction.edit_original_response(embed=e)

async def setup(bot):
  await bot.add_cog(SlashCmd_Chance(bot))