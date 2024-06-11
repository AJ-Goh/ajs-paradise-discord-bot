# List of commands here:
# 1. stats
# 2. leaderboard
# 3. setteam
# 4. addpoints
# 5. syncpoints
# 6. grandreset

import discord, json
from discord.ext import commands
from discord import app_commands

GrandResetEnabled = False

TeamDict = {
  "None": 0xffffff,
  "Red": 0xffbbbb,
  "Yellow": 0xffeeaa,
  "Green": 0xbbeebb,
  "Blue": 0xbbbbff
}

Administrators = [
  641724025780830220,
  832811319957651457
]

AdminRoles = [
  1005053361265070110,
  1123610426463232010
]

class SlashCmds_MM(commands.GroupCog, group_name="mm"):

  def __init__(self, bot):
    self.bot = bot

  def GetUser(self, user: discord.Member):
    with open('data/data_mm.json', mode='r') as infile:
      data = json.load(infile)

    if data.get(str(user.id), None) == None:
      data[user.id] = {"Score": 0, "Team": "None", "Colour": TeamDict['None']}
      with open("data/data_mm.json", mode="w") as outfile:
        json.dump(data, outfile, indent=2)

  def log(self, username, userid, action, value):
    try:
      with open('data/logs_mm.json', mode='r') as infile:
        logs = json.load(infile)
    except Exception as e:
      print(f"An error occurred: {str(e)}")
    try:
      # Convert keys to integers
      int_keys = [int(k) for k in logs.keys()]
      key = max(int_keys, default=0) + 1
    except Exception as e:
      print(f"Error calculating key: {str(e)}")
    try:
      logs[key] = {"Username": username, "User ID": userid, "Action": action, "Value": value}
    except Exception as e:
      print(f"Error modifying logs dictionary: {str(e)}")
    with open('data/logs_mm.json', mode='w') as outfile:
      json.dump(logs, outfile, indent=2)

  @app_commands.command(
    name="stats", description="Checks a user's mini-matches' statistics.")
  @app_commands.describe(user="Input the target user.")
  async def stats(self, interaction: discord.Interaction,
                  user: discord.Member):
    if not isinstance(user, discord.Member):
      Embed = discord.Embed(description="Invalid user.", color=0xFF3333)
      await interaction.response.send_message(embed=Embed)
    else:
      with open('data/data_mm.json', mode='r') as infile:
        data = json.load(infile)
      if data.get(str(user.id), None) == None:
        data[user.id] = {"Score": 0, "Team": "None", "Colour": TeamDict['None']}
        with open("data/data_mm.json", mode="w") as outfile:
          json.dump(data, outfile, indent=2)
        e = discord.Embed(title=f"{user}'s mini-matches' statistics", colour=TeamDict['None'])
        e.add_field(name="Current Team", value="None", inline=True)
        e.add_field(name="Team Score", value=data['TScores']['None'], inline=True)
        e.add_field(name="Personal Score", value="0", inline=True)
        await interaction.response.send_message(embed=e)
        return
      e = discord.Embed(title=f"{user}'s mini-matches' statistics", colour=data[str(user.id)]['Colour'])
      e.add_field(name="Current Team", value=f"{data[str(user.id)]['Team']}", inline=True)
      e.add_field(name="Team Score", value=data['TScores'][data[str(user.id)]["Team"]], inline=True)
      e.add_field(name="Personal Score", value=f"{data[str(user.id)]['Score']}", inline=True)
      await interaction.response.send_message(embed=e)

  @app_commands.command(name="leaderboard", description="View the mini-matches' leaderboard of the top 5 users and each of the teams.")
  async def leaderboard(self, interaction: discord.Interaction):

    # Step 1: Read the JSON file and load its content into a dictionary
    with open("data/data_mm.json", mode="r") as infile:
      data = json.load(infile)

    # Step 2: Extract the user scores
    scores = {user_id: user_data['Score'] for user_id, user_data in data.items() if user_id != 'TScores'}
    
    # Step 3: Sort the user scores in descending order
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    # Step 4: Take the top 5 user scores
    top_scores = sorted_scores[:5]

    # Step 5: Retrieve the corresponding user IDs
    top_user_ids = [user_id for user_id, _ in top_scores]

    # Step 6: Get the user leaderboard content
    lb_users = []
    for i, user_id in enumerate(top_user_ids, start=1):
      lb_users.append(f'\n{i}. <@{user_id}> • **{scores[user_id]}** pts')

    # Step 7: Extract the team scores
    tscores = data["TScores"]
    
    # Step 8: Sort the team scores in decending order
    sorted_tscores = sorted(tscores.items(), key=lambda x: x[1], reverse=True)
     
    # Step 9: Get the team leaderboard content
    lb_teams = []
    i = 0
    for team, score in sorted_tscores:
      i += 1
      lb_teams.append(f"\n{i}. {team} • **{score}** pts")
    
    # Step 10: Convert lb_users and lb_teams to strings
    str_users = "".join([str(u) for u in lb_users])
    str_teams = "".join([str(t) for t in lb_teams])

    # Step 11: Format the strings into an embed
    e = discord.Embed(title="Mini-Matches' Leaderboard", colour=TeamDict["None"])
    e.add_field(name="Top 5 Personal Scores", value=str_users, inline=False)
    e.add_field(name="Teams' Combined Scores", value=str_teams, inline=False)
    
    # Step 12: Print the leaderboard
    await interaction.response.send_message(embed=e)

  @app_commands.command(name="setteam", description="Select a team to join.")
  @app_commands.describe(team="Input the desired team.")
  @app_commands.choices(team = [app_commands.Choice(name=j, value=j) for j in TeamDict])
  async def setteam(self, interaction: discord.Interaction, team: str):
    self.log(interaction.user.name, interaction.user.id, "setteam", team)
    with open("data/data_mm.json", "r") as infile:
      data = json.load(infile)
    user_id = str(interaction.user.id)
    if user_id in data:
      available_teams = data["TScores"].keys()
      if team in available_teams:
        data[user_id]["Team"] = team
        data[user_id]["Colour"] = TeamDict[team]
        with open("data/data_mm.json", "w") as outfile:
          json.dump(data, outfile, indent=2)
        await interaction.response.send_message(embed=discord.Embed(description=f"Team changed to {team}.", colour=TeamDict[team]))

        # Don't forget to synchronise the scores again!

        with open("data/data_mm.json", mode="r") as infile:
          data = json.load(infile)
        for team in data["TScores"]:
          data["TScores"][team] = 0
        for i in data:
          if i != "TScores":
            team = data[i]["Team"]
            score = data[i]["Score"]
            data["TScores"][team] += score
        for team in data["TScores"]:
          data["TScores"][team] = int(data["TScores"][team])
        with open("data/data_mm.json", mode="w") as outfile:
          json.dump(data, outfile, indent=2)

      else:
        await interaction.response.send_message("Invalid team colour.")
    else:
      available_teams = data["TScores"].keys()
      if team in available_teams:
        data[user_id] = {"Score": 0, "Team": str(team), "Colour": TeamDict[team]}
        with open("data/data_mm.json", "w") as outfile:
          json.dump(data, outfile, indent=2)

        # Don't forget to synchronise the scores again!

        with open("data/data_mm.json", mode="r") as infile:
          data = json.load(infile)
        for team in data["TScores"]:
          data["TScores"][team] = 0
        for i in data:
          if i != "TScores":
            team = data[i]["Team"]
            score = data[i]["Score"]
            data["TScores"][team] += score
        for team in data["TScores"]:
          data["TScores"][team] = int(data["TScores"][team])
        with open("data/data_mm.json", mode="w") as outfile:
          json.dump(data, outfile, indent=2)
        
        await interaction.response.send_message(embed=discord.Embed(description=f"Team changed to {team}.", colour=TeamDict[team]))
      else:
        await interaction.response.send_message("Invalid team colour.")

  @app_commands.command(name="addpoints", description="(Administrator Only) Add points to a user's score.")
  @app_commands.describe(user= "Input the target user.", value= "Input the number of points to be added to the user's score.")
  async def addpoints(self, interaction: discord.Interaction, user: discord.User, value: int):
    if not any(role.id in AdminRoles for role in interaction.user.roles):
      await interaction.response.send_message(embed=discord.Embed(description="You are not an administrator.", colour=0xff0000))
      return
    else:
      with open("data/data_mm.json", mode="r") as infile:
        data = json.load(infile)
      if str(user.id) in data:
        data[str(user.id)]['Score'] += value
        with open("data/data_mm.json", mode="w") as outfile:
          data = json.dump(data, outfile, indent=2)

        # Don't forget to synchronise the scores again!

        with open("data/data_mm.json", mode="r") as infile:
          data = json.load(infile)
        for team in data["TScores"]:
          data["TScores"][team] = 0
        for i in data:
          if i != "TScores":
            team = data[i]["Team"]
            score = data[i]["Score"]
            data["TScores"][team] += score
        for team in data["TScores"]:
          data["TScores"][team] = int(data["TScores"][team])
        with open("data/data_mm.json", mode="w") as outfile:
          json.dump(data, outfile, indent=2)
          
        await interaction.response.send_message(embed=discord.Embed(description=f"Successfully increased <@{user.id}>'s score by {value}.", colour=0x00ff00))
        self.log(interaction.user.name, interaction.user.id, "addpoints", {"Username":user.name, "User ID":user.id, "Points":value})
      else:
        data[user.id] = {"Score": value, "Team": "None", "Colour": TeamDict['None']}
        with open("data/data_mm.json", mode="w") as outfile:
          data = json.dump(data, outfile, indent=2)

        # Don't forget to synchronise the scores again!

        with open("data/data_mm.json", mode="r") as infile:
          data = json.load(infile)
        for team in data["TScores"]:
          data["TScores"][team] = 0
        for i in data:
          if i != "TScores":
            team = data[i]["Team"]
            score = data[i]["Score"]
            data["TScores"][team] += score
        for team in data["TScores"]:
          data["TScores"][team] = int(data["TScores"][team])
        with open("data/data_mm.json", mode="w") as outfile:
          json.dump(data, outfile, indent=2)
        
        await interaction.response.send_message(embed=discord.Embed(description=f"Successfully increased <@{user.id}>'s score by {value}.", colour=0x00ff00))
        self.log(interaction.user.name, interaction.user.id, "addpoints", {"Username":user.name, "User ID":user.id, "Points":value})

  @app_commands.command(name="syncpoints", description="(Administrator Only) Synchronise the team scores with the personal scores.")
  async def syncpoints(self, interaction: discord.Interaction):
    if interaction.user.id not in Administrators:
      await interaction.response.send_message(embed=discord.Embed(description="You are not an administrator.", colour=0xff0000))
      return
    else:
      await interaction.response.send_message(embed=discord.Embed(description="Synchronising user and team scores...", colour=0xffff00))
      with open("data/data_mm.json", mode="r") as infile:
        data = json.load(infile)
      for team in data["TScores"]:
        data["TScores"][team] = 0
      for i in data:
        if i != "TScores":
          team = data[i]["Team"]
          score = data[i]["Score"]
          data["TScores"][team] += score
      for team in data["TScores"]:
        data["TScores"][team] = int(data["TScores"][team]) # REQUIRED: This converts the team scoers from floats to integers.
      with open("data/data_mm.json", mode="w") as outfile:
        json.dump(data, outfile, indent=2)
      await interaction.edit_original_response(embed=discord.Embed(description="Synchronisation complete.", colour=0x00ff00))
      self.log(interaction.user.name, interaction.user.id, "syncpoints", "success")

  @app_commands.command(name="grandreset", description="(Administrator Only) Execute a grand reset, which resets all users' and teams' scores.")
  async def grandreset(self, interaction: discord.Interaction):
    if GrandResetEnabled:
      await interaction.response.send_message(embed=discord.Embed(description="The grand reset has been executed.", colour=0xffff00))
      with open('data/data_mm.json', 'r') as infile:
        data = json.load(infile)
      data['TScores'] = {i: 0 for i in data['TScores']}
      for i in data:
        if i != 'TScores':
          data[i]['Score'] = 0
          data[i]['Team'] = "None"
          data[i]['Colour'] = TeamDict['None']
      with open('data/data_mm.json', 'w') as outfile:
        json.dump(data, outfile, indent=2)
      await interaction.edit_original_response(embed=discord.Embed(description="The grand reset is completed.", colour=0x00ff00))
      self.log(interaction.user.name, interaction.user.id, "grandreset", "success")
    else:
      await interaction.response.send_message(embed=discord.Embed(description="The grand reset command is currently disabled. Please set the **`GrandResetEnabled`** variable in the bot's code to **`True`** to enable the grand reset.", colour=0xff0000))
  
async def setup(bot):
  await bot.add_cog(SlashCmds_MM(bot))