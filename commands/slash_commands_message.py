# List of commands here:
# 1. setlevel
# 2. setxp
# 3. setmulti
# 4. stats
# 5. leaderboard
# 6. addclaim

import discord, json, random
from discord.ext import commands
from discord import app_commands

# << Data >> #

MultiXP = 1
FooterText = "Redeem 400 R$ for every 10 levels!"

Administrators = [
    641724025780830220,
    832811319957651457
]

LevelRoles = {
  #    1: 1134514598960189491,
  #    5: 1134514656069828639,
  #   10: 1134514703670972466,
  #   25: 1134981247907667999,
  #   50: 1134981290995744818,
} # Note: Level roles currently not in use.

class SlashCmds_Message(commands.GroupCog, group_name="message"):  
    def __init__(self, bot):
        self.bot = bot

    # << Fetch User >> #
    def GetUser(self, user: discord.Member):
        with open('data/data_messages.json', mode='r') as infile:
            LevelData = json.load(infile)

        if LevelData.get(str(user.id), None) == None:
            LevelData[user.id] = {'Level': 1, 'Exp': 0, 'GoalExp': 200, 'Claims': 0}
            with open("data/data_messages.json", mode="w") as outfile:
                json.dump(LevelData, outfile, indent=2)
      
    # << Set The Level >> #
    @app_commands.command(name="setlevel", description="(Administrator Only) Sets the current message level of a user.")
    @app_commands.describe(user="Input the target user.", level="Input the level (integer).")
    async def SetLevel(self, interaction: discord.Interaction, user: discord.Member, level: int):
        if interaction.user.id not in Administrators:
            Embed = discord.Embed(description="You are not an administrator.", color=0xff0000)
            await interaction.response.send_message(embed=Embed)
            return
        if not isinstance(user, discord.Member) and not type(level) == int:
            Embed = discord.Embed(description="Invalid user and level.", color=0xff0000)
            await interaction.response.send_message(embed=Embed)
        else:
            if not isinstance(user, discord.Member):
                Embed = discord.Embed(description="Invalid user.", color=0xff0000)
                await interaction.response.send_message(embed=Embed)
            elif not type(level) == int:
                Embed = discord.Embed(description="Invalid level.", color=0xff0000)
                await interaction.response.send_message(embed=Embed)
            else:
                self.GetUser(user)

                with open('data/data_messages.json', mode='r') as infile:
                    LevelData = json.load(infile)

                try:
                    LevelData[str(user.id)]['Level'] = level
                    LevelData[str(user.id)]['GoalExp'] = LevelData[str(user.id)]['Level'] * 200

                    with open('data/data_messages.json', mode='w') as outfile:
                        json.dump(LevelData, outfile, indent=2)

                    Embed = discord.Embed(description=f"Successsfully set level for **{user.name}**.", color=0x00ff00)
                    await interaction.response.send_message(embed=Embed)

                    # Assign role based on level
                    member = user
                    roles = sorted(LevelRoles.items(), key=lambda x: x[0])
                    member_role_ids = [role.id for role in member.roles]
                    for level, role_id in roles:
                        role = interaction.guild.get_role(role_id)
                        if LevelData[str(member.id)]['Level'] >= level:
                            if role_id not in member_role_ids:
                                await member.add_roles(role)
                        else:
                            if role_id in member_role_ids and role_id in LevelRoles.values():
                                await member.remove_roles(role)

                except Exception as e:
                    Embed = discord.Embed(description=f"An unexpected error occured: {e}", color=0xff0000)
                    await interaction.response.send_message(embed=Embed)

    # << Set The XP >> #
    @app_commands.command(name="setxp", description="(Administrator Only) Sets the current message XP of a user.")
    @app_commands.describe(user="Input the target user.", xp="Input the XP (integer).")
    async def SetXP(self, interaction: discord.Interaction, user: discord.Member, xp: int):
        if interaction.user.id not in Administrators:
            Embed = discord.Embed(description="You are not an administrator.", color=0xff0000)
            await interaction.response.send_message(embed=Embed)
            return
        if not isinstance(user, discord.Member) and not type(xp) == int:
            Embed = discord.Embed(description="Invalid user and XP.", color=0xff0000)
            await interaction.response.send_message(embed=Embed)
        else:
            if not isinstance(user, discord.Member):
                Embed = discord.Embed(description="Invalid user.", color=0xff0000)
                await interaction.response.send_message(embed=Embed)
            elif not type(xp) == int:
                Embed = discord.Embed(description="Invalid XP.", color=0xff0000)
                await interaction.response.send_message(embed=Embed)
            else:
                self.GetUser(user)

                with open('data/data_messages.json', mode='r') as infile:
                    LevelData = json.load(infile)

                try:
                    LevelData[str(user.id)]['Exp'] = xp
                    LevelData[str(user.id)]['GoalExp'] = LevelData[str(user.id)]['Level'] * 200

                    with open('data/data_messages.json', mode='w') as outfile:
                        json.dump(LevelData, outfile, indent=2)

                    Embed = discord.Embed(description=f"Successsfully set XP for **{user.name}**.", color=0x00ff00)
                    await interaction.response.send_message(embed=Embed)

                except Exception as e:
                    Embed = discord.Embed(description=f"An unexpected error occured: {e}", color=0xff0000)
                    await interaction.response.send_message(embed=Embed)

    # << Sets the XP Multiplier >> #
    @app_commands.command(name="setmulti", description="(Administrator Only) Sets the current message XP multiplier.")
    @app_commands.describe(multiplier="Input the XP multiplier (integer).")
    async def SetMulti(self, interaction: discord.Interaction, multiplier: int):
      global MultiXP # Note: this declares MultiXP as a global variable
      if interaction.user.id not in Administrators:
        Embed = discord.Embed(description="You are not an administrator.", color=0xff0000)
        await interaction.response.send_message(embed=Embed)
        return
      else:
        MultiXP = multiplier
        Embed = discord.Embed(description=f"Successfully set the message XP multiplier to **{MultiXP}**.", color=0x00ff00)
        await interaction.response.send_message(embed=Embed)

    # << Slash Command To Check Player Level And Stuff >> #
    @app_commands.command(name="stats", description="Checks a user's message statistics.")
    @app_commands.describe(user="Input the target user.")
    async def CheckUser(self, interaction: discord.Interaction, user: discord.Member):
        if not isinstance(user, discord.Member):
            Embed = discord.Embed(description="Invalid user.", color=0xff0000)
            await interaction.response.send_message(embed=Embed)
        else:
            with open('data/data_messages.json', mode='r') as infile:
                LevelData = json.load(infile)
            Embed = discord.Embed(title=f"{user}'s message statistics", description=f'```Level  {LevelData[str(user.id)]["Level"]}\nXP     {LevelData[str(user.id)]["Exp"]}/{LevelData[str(user.id)]["GoalExp"]}```', color=0xffcc00)
            if LevelData[str(user.id)]['Claims'] == 1:
                time = "time"
            else:
                time = "times"
            Embed.set_footer(text=FooterText+f" (Claimed {LevelData[str(user.id)]['Claims']} {time})")
            await interaction.response.send_message(embed=Embed)

    # << Message Leaderboard >> #
    @app_commands.command(name="leaderboard", description="View the message leaderboard of the top 10 users.")
    async def leaderboard(self, interaction: discord.Interaction):
        with open('data/data_messages.json', mode='r') as infile:
            LevelData: dict = json.load(infile)

        # Sort the data by level in descending order
        sorted_data = sorted(LevelData.items(), key=lambda x: x[1]['Level'], reverse=True)

        # Take the top 10 players
        top_10 = sorted_data[:10]

        # Create a list of tuples with the user id and level
        result = [(user_id, data['Level']) for user_id, data in top_10]
        rank = 0
        result_with_usernames = []
        for user_id, level in result:
            rank += 1
            result_with_usernames.append((user_id, level, rank))

        formatted_string = '\n'.join(f'{rank}. <@{user_id}> • Level **{level}**' for user_id, level, rank in result_with_usernames)
        Embed = discord.Embed(title="Message Leaderboard", description=f"Displaying the top 10 users in the server as follows.\n\n{formatted_string}", colour=0xffcc00)
        Embed.set_footer(text=FooterText)

        await interaction.response.send_message(embed=Embed)

    # << Record prize claim >> #
    @app_commands.command(name="addclaim", description="(Administrator Only) Log a prize claim of a user.")
    @app_commands.describe(user="State the user of the claim log increase.", quantity= "State the number of claims to increase the log by.")
    async def addclaim(self, interaction: discord.Interaction, user: discord.User, quantity: int):
        if interaction.user.id not in Administrators:
            Embed = discord.Embed(description="You are not an administrator.", color=0xff0000)
            await interaction.response.send_message(embed=Embed)
            return
        else:
            with open('data/data_messages.json', mode='r') as infile:
                data = json.load(infile)
            data[str(user.id)]['Claims'] += quantity
            with open('data/data_messages.json', mode='w') as outfile:
                json.dump(data, outfile, indent=2)
            await interaction.response.send_message(embed=discord.Embed(description=f"Successfully increased <@{str(user.id)}>'s prize claim log from {data[str(user.id)]['Claims']-quantity} to {data[str(user.id)]['Claims']}.", color=0x00ff00))
  
    # << On Message >> #
    @commands.Cog.listener()
    async def on_message(self, ctx: discord.Message):
        if ctx.author.bot:
            return
        else:
            self.GetUser(ctx.author)
            with open('data/data_messages.json', mode='r') as infile:
                LevelData = json.load(infile)
            
            if len(ctx.content) <= 250:
                LevelData[str(ctx.author.id)]['Exp'] += (len(ctx.content)*MultiXP)//random.randint(12,15)
            elif len(ctx.content) > 250:
                LevelData[str(ctx.author.id)]['Exp'] += random.randint(16*MultiXP,20*MultiXP)

            if LevelData[str(ctx.author.id)]['Exp'] >= LevelData[str(ctx.author.id)]['GoalExp']:
                LevelData[str(ctx.author.id)]['Level'] += 1
                LevelData[str(ctx.author.id)]['GoalExp'] = LevelData[str(ctx.author.id)]['Level'] * 200
                LevelData[str(ctx.author.id)]['Exp'] = 0
                Embed = discord.Embed(title=f"✨  {ctx.author} has leveled up!  ✨", description=f"Level {LevelData[str(ctx.author.id)]['Level']-1} → Level {LevelData[str(ctx.author.id)]['Level']}", color=0xffcc00)
                if LevelData[str(ctx.author.id)]['Claims'] == 1:
                    time = "time"
                else:
                    time = "times"
                Embed.set_footer(text=FooterText+f" (Claimed {LevelData[str(ctx.author.id)]['Claims']} {time})")
                await ctx.channel.send(content=f"<@{ctx.author.id}>", embed=Embed)

            with open('data/data_messages.json', mode='w') as outfile:
                json.dump(LevelData, outfile, indent=2)

            # Assign role based on level
            member = ctx.author
            roles = sorted(LevelRoles.items(), key=lambda x: x[0])
            member_role_ids = [role.id for role in member.roles]

            for level, role_id in roles:
                role = ctx.guild.get_role(role_id)
                if LevelData[str(member.id)]['Level'] >= level:
                    if role_id not in member_role_ids:
                        await member.add_roles(role)
                else:
                    if role_id in member_role_ids and role_id in LevelRoles.values():
                        await member.remove_roles(role)

async def setup(bot):
    await bot.add_cog(SlashCmds_Message(bot))