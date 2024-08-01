# List of commands here:
# 1. rng
# 2. rps
# 3. 8ball
# 4. roast
# 5. rizz
# 6. truthordare
# 7. ninetynine
# 8. highlowinf

import discord, time, random
from discord import app_commands
from discord.ext import commands
from discord.ui import View
from discord.app_commands import Choice
from misc.images import NINETYNINE, NINETYNINE_LOGO, HIGHLOWINF, HIGHLOWINF_LOGO
from misc.messages import NINETYNINE_DESC, HIGHLOWINF_DESC
from misc.truthordare import TOD_TRUTHS, TOD_DARES

# NINETYNINE [5]

# 1. Stores the game
Games = {}

# 2. Function to add the values
def Add(UserID, Num):
    Games[UserID]['Turn'] += 1

    if Num == 1:
        Value = Games[UserID]['Decrease1']
        Games[UserID]['Current'] -= Value
        if Games[UserID]['Current'] < 0:
            Games[UserID]['Current'] = Games[UserID]['Goal'] + Games[UserID]['Current'] + 1
    elif Num == 2:
        Value = Games[UserID]['Decrease2']
        Games[UserID]['Current'] -= Value
        if Games[UserID]['Current'] < 0:
            Games[UserID]['Current'] = Games[UserID]['Goal'] + Games[UserID]['Current'] + 1

    elif Num == 3:
        Value = Games[UserID]['Increase1']
        Games[UserID]['Current'] += Value
        if Games[UserID]['Current'] > Games[UserID]['Goal']:
            Games[UserID]['Current'] -= Games[UserID]['Goal'] + 1     

    elif Num == 4:
        Value = Games[UserID]['Increase2']
        Games[UserID]['Current'] += Value
        if Games[UserID]['Current'] > Games[UserID]['Goal']:
            Games[UserID]['Current'] -= Games[UserID]['Goal'] + 1     

    elif Num == 5:
        Value = Games[UserID]['Increase3']
        Games[UserID]['Current'] += Value
        if Games[UserID]['Current'] > Games[UserID]['Goal']:
            Games[UserID]['Current'] -= Games[UserID]['Goal'] + 1     
    
# 3. Function to disable all the buttons
def DisableAll(self, interaction):
    self.children[0].label = "-" + str(Games[interaction.user.id]['Decrease1'])
    self.children[0].disabled = True
    self.children[1].label = "-" + str(Games[interaction.user.id]['Decrease2'])
    self.children[1].disabled = True
    self.children[2].label = "+" + str(Games[interaction.user.id]['Increase1'])
    self.children[2].disabled = True
    self.children[3].label = "+" + str(Games[interaction.user.id]['Increase2'])
    self.children[3].disabled = True
    self.children[4].label = "+" + str(Games[interaction.user.id]['Increase3'])
    self.children[4].disabled = True  
    Win = True 
    return Win

# 4. Class for the buttons
class Buttons(View):
    def __init__(self, message, UserID) -> None:
        super().__init__()
        self.message = message
        self.UserID = UserID

    @discord.ui.button(label="-", custom_id="Minus1", style=discord.ButtonStyle.red)
    async def Minus1_callback(self, interaction: discord.Interaction, button):
        if interaction.user.id != self.UserID:
            return
        await interaction.response.defer()
        Add(interaction.user.id, 1)

        if Games[interaction.user.id]['Current'] == Games[interaction.user.id]['Goal']:
            Win = DisableAll(self=self, interaction=interaction)
            embed = discord.Embed(
                title=f"{Games[interaction.user.id]['Current']}",
                description=f"Congratulations! You won in **{Games[interaction.user.id]['Turn']}** turns.",
                color=0xaaaaff
            )
            embed.set_author(name="ninetynine", icon_url=NINETYNINE_LOGO)
            embed.set_footer(text="Created by AJ Goh")
        else:
            Win = False
            embed = discord.Embed(
                title=f"{Games[interaction.user.id]['Current']}",
                description=f"Get the number above to **{Games[interaction.user.id]['Goal']}** to win. This is turn **#{Games[interaction.user.id]['Turn']}**.",
                color=0xffaaaa
            )
            embed.set_author(name="ninetynine", icon_url=NINETYNINE_LOGO)
            embed.set_footer(text="Created by AJ Goh")
        await interaction.edit_original_response(embed=embed, view=self)
        if Win == True:
            del Games[interaction.user.id]

    @discord.ui.button(label="-", custom_id="Minus2", style=discord.ButtonStyle.red)
    async def Minus2_callback(self, interaction: discord.Interaction, button):
        if interaction.user.id != self.UserID:
            return
        await interaction.response.defer()
        Add(interaction.user.id, 2)

        if Games[interaction.user.id]['Current'] == Games[interaction.user.id]['Goal']:
            Win = DisableAll(self=self, interaction=interaction)           
            embed = discord.Embed(
                title=f"{Games[interaction.user.id]['Current']}",
                description=f"Congratulations! You won in **{Games[interaction.user.id]['Turn']}** turns.",
                color=0xaaaaff
            )
            embed.set_author(name="ninetynine", icon_url=NINETYNINE_LOGO)
            embed.set_footer(text="Created by AJ Goh")
        else:
            Win = False
            embed = discord.Embed(
                title=f"{Games[interaction.user.id]['Current']}",
                description=f"Get the number above to **{Games[interaction.user.id]['Goal']}** to win. This is turn **#{Games[interaction.user.id]['Turn']}**.",
                color=0xffaaaa
            )
            embed.set_author(name="ninetynine", icon_url=NINETYNINE_LOGO)
            embed.set_footer(text="Created by AJ Goh")
        await interaction.edit_original_response(embed=embed, view=self)
        if Win:
            del Games[interaction.user.id]
    
    @discord.ui.button(label="+", custom_id="Plus1", style= discord.ButtonStyle.blurple)
    async def Plus1_callback(self, interaction: discord.Interaction, button):
        if interaction.user.id != self.UserID:
            return
        
        await interaction.response.defer()
        Add(interaction.user.id, 3)

        if Games[interaction.user.id]['Current'] == Games[interaction.user.id]['Goal']:
            Win = DisableAll(self=self, interaction=interaction) 
            embed = discord.Embed(
                title=f"{Games[interaction.user.id]['Current']}",
                description=f"Congratulations! You won in **{Games[interaction.user.id]['Turn']}** turns.",
                color=0xaaaaff
            )
            embed.set_author(name="ninetynine", icon_url=NINETYNINE_LOGO)
            embed.set_footer(text="Created by AJ Goh")
        else:
            Win = False
            embed = discord.Embed(
                title=f"{Games[interaction.user.id]['Current']}",
                description=f"Get the number above to **{Games[interaction.user.id]['Goal']}** to win. This is turn **#{Games[interaction.user.id]['Turn']}**.",
                color=0xffaaaa
            )
            embed.set_author(name="ninetynine", icon_url=NINETYNINE_LOGO)
            embed.set_footer(text="Created by AJ Goh")
        await interaction.edit_original_response(embed=embed, view=self)
        if Win:
            del Games[interaction.user.id]

    @discord.ui.button(label="+", custom_id="Plus2", style= discord.ButtonStyle.blurple)
    async def Plus2_callback(self, interaction: discord.Interaction, button):
        if interaction.user.id != self.UserID:
            return
        await interaction.response.defer()
        Add(interaction.user.id, 4)

        if Games[interaction.user.id]['Current'] == Games[interaction.user.id]['Goal']:
            Win = DisableAll(self=self, interaction=interaction)
            embed = discord.Embed(
                title=f"{Games[interaction.user.id]['Current']}",
                description=f"Congratulations! You won in **{Games[interaction.user.id]['Turn']}** turns.",
                color=0xaaaaff
            )
            embed.set_author(name="ninetynine", icon_url=NINETYNINE_LOGO)
            embed.set_footer(text="Created by AJ Goh")
        else:
            Win = False
            embed = discord.Embed(
                title=f"{Games[interaction.user.id]['Current']}",
                description=f"Get the number above to **{Games[interaction.user.id]['Goal']}** to win. This is turn **#{Games[interaction.user.id]['Turn']}**.",
                color=0xffaaaa
            )
            embed.set_author(name="ninetynine", icon_url=NINETYNINE_LOGO)
            embed.set_footer(text="Created by AJ Goh")
        await interaction.edit_original_response(embed=embed, view=self)
        if Win:
            del Games[interaction.user.id]

    @discord.ui.button(label="+", custom_id="Plus3", style= discord.ButtonStyle.blurple)
    async def Plus3_callback(self, interaction: discord.Interaction, button):
        if interaction.user.id != self.UserID:
            return
        await interaction.response.defer()
        Add(interaction.user.id, 5) 

        if Games[interaction.user.id]['Current'] == Games[interaction.user.id]['Goal']:
            Win = DisableAll(self=self, interaction=interaction)
            embed = discord.Embed(
                title=f"{Games[interaction.user.id]['Current']}",
                description=f"Congratulations! You won in **{Games[interaction.user.id]['Turn']}** turns.",
                color=0xaaaaff
            )
            embed.set_author(name="ninetynine", icon_url=NINETYNINE_LOGO)
            embed.set_footer(text="Created by AJ Goh")
        else:
            Win = False
            embed = discord.Embed(
                title=f"{Games[interaction.user.id]['Current']}",
                description=f"Get the number above to **{Games[interaction.user.id]['Goal']}** to win. This is turn **#{Games[interaction.user.id]['Turn']}**.",
                color=0xffaaaa
            )
            embed.set_author(name="ninetynine", icon_url=NINETYNINE_LOGO)
            embed.set_footer(text="Created by AJ Goh")

        await interaction.edit_original_response(embed=embed, view=self)
        if Win:
            del Games[interaction.user.id]

# 5. Class for deletion message Yes/No
class YesNo(View):
    def __init__(self, message, UserID) -> None:
        super().__init__()
        self.message = message
        self.UserID = UserID

    @discord.ui.button(label="Yes", custom_id="Yes", style=discord.ButtonStyle.green)
    async def Yes_callback(self, interaction: discord.Interaction, button):
        if interaction.user.id != self.UserID:
            return
        await interaction.response.defer()
        Embed = discord.Embed(description="Deleting session..", color=0xffaaaa)
        Embed.set_author(name="ninetynine", icon_url=NINETYNINE_LOGO)
        Embed.set_footer(text="Created by AJ Goh")
        await interaction.edit_original_response(embed=Embed, view=None)

        ChannelID = Games[interaction.user.id]['Channel']
        Channel = interaction.guild.get_channel(ChannelID)

        MessageID = Games[interaction.user.id]['Message']
        Message = await Channel.fetch_message(MessageID)
        await Message.delete()

        del Games[interaction.user.id]
        Embed = discord.Embed(description="Successfully deleted the previous session. You may proceed to run the command again to start a new game session.", color=0xffaaaa)
        Embed.set_author(name="ninetynine", icon_url=NINETYNINE_LOGO)
        Embed.set_footer(text="Created by AJ Goh")
        Message = await interaction.edit_original_response(embed=Embed, view=None)

        time.sleep(3)
        await Message.delete()

    @discord.ui.button(label="No", custom_id="No", style= discord.ButtonStyle.red)
    async def No_callback(self, interaction: discord.Interaction, button):
        if interaction.user.id != self.UserID:
            return
        await interaction.response.defer()
        Embed = discord.Embed(description="Action cancelled.", color=0xaaaaff)
        Embed.set_author(name="ninetynine", icon_url=NINETYNINE_LOGO)
        Embed.set_footer(text="Created by AJ Goh")
        Message = await interaction.edit_original_response(embed=Embed, view=None)
        time.sleep(3)
        await Message.delete()

# HIGHLOWINF [5]

# 1. Stores the game
HLGames = {}

# 2. Function to compare the numbers
def HLCompare(UserID, Input):
    HLGames[UserID]['Turn'] += 1

    if Input == "h":
      if HLGames[UserID]['N'] > HLGames[UserID]['G']:
        HLGames[UserID]['Min'] = HLGames[UserID]['G']
        return 2
    	else:
        return 0
    elif Input == "l":
        if HLGames[UserID]['N'] < HLGames[UserID]['G']:
        HLGames[UserID]['Max'] = HLGames[UserID]['G']
        return 2
    	else:
        return 0
    elif Input == "e":
        if HLGames[UserID]['N'] == HLGames[UserID]['G']:
        return 1
    	else:
        return 0
        
# 3. Functions to disable all the buttons
def HLEnd(self, interaction):
  	self.children[0].disabled = True
    self.children[1].disabled = True
    self.children[2].disabled = True
    End = True 
    return End

# 4. Class for the buttons
class HLButtons(View):
    def __init__(self, message, UserID) -> None:
      super().__init__()
      self.message = message
      self.UserID = UserID

    @discord.ui.button(label="Higher", custom_id="hi", style=discord.ButtonStyle.green)
    async def hi_callback(self, interaction: discord.Interaction, button):
        if interaction.user.id != self.UserID:
            return
        await interaction.response.defer()
        Win = HLCompare(interaction.user.id, "h")

        if Win == 0:
            End = HLEnd(self=self, interaction=interaction)
            embed = discord.Embed(
                title=f"The number is __{HLGames[interaction.user.id]['N']}__",
                description=f"Sorry, you lost! You survived for **{HLGames[interaction.user.id]['Turn']}** turns.",
                color=0xffaaaa
            )
            embed.set_author(name="HighLow Infinite", icon_url=HIGHLOW_LOGO)
            embed.set_footer(text="Created by AJ Goh")
        elif Win == 1:
            End = HLEnd(self=self, interaction=interaction)
            embed = discord.Embed(
                title=f"The number is __{HLGames[interaction.user.id]['N']}__",
                description=f"Congratulations! You won in **{HLGames[interaction.user.id]['Turn']}** turns.",
                color=0xaaffaa
            )
            embed.set_author(name="HighLow Infinite", icon_url=HIGHLOW_LOGO)
            embed.set_footer(text="Created by AJ Goh")
        else:
            End = False
            HLGames[interaction.user.id]['G'] = random.randint(HLGames[interaction.user.id]['Min'], HLGames[interaction.user.id]['Max'])
            embed = discord.Embed(
                description=f"(Turn **#{HLGames[interaction.user.id]['Turn']}**)\nI am thinking of a number between **1** and **{HLGames[interaction.user.id]['R']}** inclusive.\n# Is it higher than, lower than, or equal to __{HLGames[interaction.user.id]['G']}__?",
                color=0xaaffaa
            )
            embed.set_author(name="HighLow Infinite", icon_url=HIGHLOWINF_LOGO)
            embed.set_footer(text="Created by AJ Goh")
        await interaction.edit_original_response(embed=embed, view=self)
        if End:
            del HLGames[interaction.user.id]

    @discord.ui.button(label="Lower", custom_id="lo", style=discord.ButtonStyle.green)
    async def hi_callback(self, interaction: discord.Interaction, button):
        if interaction.user.id != self.UserID:
            return
        await interaction.response.defer()
        Win = HLCompare(interaction.user.id, "l")

        if Win == 0:
            End = HLEnd(self=self, interaction=interaction)
            embed = discord.Embed(
                title=f"The number is __{HLGames[interaction.user.id]['N']}__",
                description=f"Sorry, you lost! You survived for **{HLGames[interaction.user.id]['Turn']}** turns.",
                color=0xffaaaa
            )
            embed.set_author(name="HighLow Infinite", icon_url=HIGHLOW_LOGO)
            embed.set_footer(text="Created by AJ Goh")
        elif Win == 1:
            End = HLEnd(self=self, interaction=interaction)
            embed = discord.Embed(
                title=f"The number is __{HLGames[interaction.user.id]['N']}__",
                description=f"Congratulations! You won in **{HLGames[interaction.user.id]['Turn']}** turns.",
                color=0xaaffaa
            )
            embed.set_author(name="HighLow Infinite", icon_url=HIGHLOW_LOGO)
            embed.set_footer(text="Created by AJ Goh")
        else:
            End = False
            HLGames[interaction.user.id]['G'] = random.randint(HLGames[interaction.user.id]['Min'], HLGames[interaction.user.id]['Max'])
            embed = discord.Embed(
                description=f"(Turn **#{HLGames[interaction.user.id]['Turn']}**)\nI am thinking of a number between **1** and **{HLGames[interaction.user.id]['R']}** inclusive.\n# Is it higher than, lower than, or equal to __{HLGames[interaction.user.id]['G']}__?",
                color=0xaaffaa
            )
            embed.set_author(name="HighLow Infinite", icon_url=HIGHLOWINF_LOGO)
            embed.set_footer(text="Created by AJ Goh")
        await interaction.edit_original_response(embed=embed, view=self)
        if End:
            del HLGames[interaction.user.id]

    @discord.ui.button(label="Equal", custom_id="eq", style=discord.ButtonStyle.green)
    async def hi_callback(self, interaction: discord.Interaction, button):
        if interaction.user.id != self.UserID:
            return
        await interaction.response.defer()
        Win = HLCompare(interaction.user.id, "e")

        if Win == 0:
            End = HLEnd(self=self, interaction=interaction)
            embed = discord.Embed(
                title=f"The number is __{HLGames[interaction.user.id]['N']}__",
                description=f"Sorry, you lost! You survived for **{HLGames[interaction.user.id]['Turn']}** turns.",
                color=0xffaaaa
            )
            embed.set_author(name="HighLow Infinite", icon_url=HIGHLOW_LOGO)
            embed.set_footer(text="Created by AJ Goh")
        elif Win == 1:
            End = HLEnd(self=self, interaction=interaction)
            embed = discord.Embed(
                title=f"The number is __{HLGames[interaction.user.id]['N']}__",
                description=f"Congratulations! You won in **{HLGames[interaction.user.id]['Turn']}** turns.",
                color=0xaaffaa
            )
            embed.set_author(name="HighLow Infinite", icon_url=HIGHLOW_LOGO)
            embed.set_footer(text="Created by AJ Goh")
        else:
            End = False
            HLGames[interaction.user.id]['G'] = random.randint(HLGames[interaction.user.id]['Min'], HLGames[interaction.user.id]['Max'])
            embed = discord.Embed(
                description=f"(Turn **#{HLGames[interaction.user.id]['Turn']}**)\nI am thinking of a number between **1** and **{HLGames[interaction.user.id]['R']}** inclusive.\n# Is it higher than, lower than, or equal to __{HLGames[interaction.user.id]['G']}__?",
                color=0xaaffaa
            )
            embed.set_author(name="HighLow Infinite", icon_url=HIGHLOWINF_LOGO)
            embed.set_footer(text="Created by AJ Goh")
        await interaction.edit_original_response(embed=embed, view=self)
        if End:
            del HLGames[interaction.user.id]

# 5. Class for deletion message Yes/No
class YesNo(View):
    def __init__(self, message, UserID) -> None:
        super().__init__()
        self.message = message
        self.UserID = UserID

    @discord.ui.button(label="Yes", custom_id="Yes", style=discord.ButtonStyle.green)
    async def Yes_callback(self, interaction: discord.Interaction, button):
        if interaction.user.id != self.UserID:
            return
        await interaction.response.defer()
        Embed = discord.Embed(description="Deleting session..", color=0xffaaaa)
        Embed.set_author(name="HighLow Infinite", icon_url=HIGHLOWINF_LOGO)
        Embed.set_footer(text="Created by AJ Goh")
        await interaction.edit_original_response(embed=Embed, view=None)

        ChannelID = HLGames[interaction.user.id]['Channel']
        Channel = interaction.guild.get_channel(ChannelID)

        MessageID = HLGames[interaction.user.id]['Message']
        Message = await Channel.fetch_message(MessageID)
        await Message.delete()

        del HLGames[interaction.user.id]
        Embed = discord.Embed(description="Successfully deleted the previous session. You may proceed to run the command again to start a new game session.", color=0xaaffaa)
        Embed.set_author(name="HighLow Infinite", icon_url=HIGHLOWINF_LOGO)
        Embed.set_footer(text="Created by AJ Goh")
        Message = await interaction.edit_original_response(embed=Embed, view=None)

        time.sleep(3)
        await Message.delete()

    @discord.ui.button(label="No", custom_id="No", style= discord.ButtonStyle.red)
    async def No_callback(self, interaction: discord.Interaction, button):
        if interaction.user.id != self.UserID:
            return
        await interaction.response.defer()
        Embed = discord.Embed(description="Action cancelled.", color=0xaaffaa)
        Embed.set_author(name="HighLow Infinite", icon_url=HIGHLOWINF_LOGO)
        Embed.set_footer(text="Created by AJ Goh")
        Message = await interaction.edit_original_response(embed=Embed, view=None)
        time.sleep(3)
        await Message.delete()

# FUN GROUPCOG

class SlashCmd_Fun(commands.GroupCog, group_name="fun"):
  def __init__(self, bot):
      self.bot = bot

  @app_commands.command(name="rng", description="Generates a random integer between 2 integer inputs.")
  @app_commands.describe(int_1="Input the first integer.", int_2="Input the second integer.")
  async def rng(self, interaction: discord.Interaction, int_1: int, int_2: int):
    if int_1 < int_2 or int_1 == int_2:
      await interaction.response.send_message(f"## 🎲 Random integer between {int_1} and {int_2}:\n> `{random.randint(int_1, int_2)}`")
    else:
      await interaction.response.send_message("## ⚠️ `int_1` is more than `int_2`:\n> To avoid argument errors, please ensure that when you send this command again, `int_1` is less than `int_2`.")

  @app_commands.command(name="rps", description="Play a game of Rock-Paper-Scissors against the bot.")
  @app_commands.describe(hand="Choose what hand to play.")
  @app_commands.choices(hand = [
    app_commands.Choice(name="Rock", value="Rock"),
    app_commands.Choice(name="Paper", value="Paper"),
    app_commands.Choice(name="Scissors", value="Scissors")
  ])
  async def rps(self, interaction: discord.Interaction, hand: str):
    winlose = random.randint(1,10)
    if winlose == 10:
      winner = "You win!"
      colour = 0x00ff00
      if hand == "Rock":
        bot_hand = "Scissors"
      elif hand == "Paper":
        bot_hand = "Rock"
      else:
        bot_hand = "Paper"
    elif winlose > 6:
      winner = "It's a draw!"
      colour = 0xffff00
      bot_hand = hand
    else:
      winner = "I win!"
      colour = 0xff0000
      if hand == "Rock":
        bot_hand = "Paper"
      elif hand == "Paper":
        bot_hand = "Scissors"
      else:
        bot_hand = "Rock"
    await interaction.response.send_message(embed=discord.Embed(title="Rock Paper Scissors", description=f"- You played **{hand}**\n- I played **{bot_hand}**\n\n{winner}", colour=colour))
  
  @app_commands.command(name="8ball", description="Generates a random response to a question input.")
  @app_commands.describe(question='Ask a question!')
  async def eightball(self, interaction: discord.Interaction, question: str):
    responses = [
      "It is certain. 🙆",
      "It is decidedly so. 🙆",
      "Without a doubt. 🙆",
      "Yes, definitely. 🙆",
      "You may rely on it. 🙆",
      "As I see it, yes. 🙆",
      "Most likely. 🙆",
      "Outlook good. 🙆",
      "Yes. 🙆",
      "Signs point to yes. 🙆",
      "Reply hazy, try again. 🤷",
      "Ask again later. 🤷",
      "Better not tell you now. 🤷",
      "Cannot predict now. 🤷",
      "Concentrate and ask again. 🤷",
      "Don't count on it. 🙅",
      "My reply is no. 🙅",
      "My sources say no. 🙅",
      "Outlook not so good. 🙅",
      "Very doubtful. 🙅"
    ]
    await interaction.response.send_message(f"""## "{question}"\n> {random.choice(responses)}""")

  @app_commands.command(name="roast", description="Generates a random roast or your (probably non-existent) friends.")
  async def roast(self, interaction: discord.Interaction):
    responses = [
      "I'd agree with you, but then we'd both be wrong.",
      "Do you even have a mirror at home, or do you just walk around looking like that?",
      "You're the reason the gene pool needs a lifeguard.",
      "I'd roast you, but I'm afraid your IQ might drop even lower.",
      "Is your drama going to an intermission soon, or should I grab some popcorn?",
      "Remember when I asked for your opinion? Me neither.",
      "You're like a cloud – when you disappear, it's a beautiful day.",
      "Are you always this dumb, or are you just making a special effort today?",
      "I envy everyone who hasn't met you.",
      "Roses are red, violets are blue, I have five fingers, and the middle one's for you.",
      "Your ego is so massive, it bends spacetime more than a black hole.",
      "I'd call you a genius, but then I remembered geniuses contribute positively to society.",
      "Your two brain cells are like Schrödinger's cat – simultaneously present and absent.",
      "If your IQ was on the periodic table, it'd be an element with a half-life shorter than a nanosecond.",
      "Did you learn about inertia? Because you're showing no sign of intellectual movement.",
      "If wit were a form of energy, you'd be a perpetual motion machine of disappointment.",
      "Your understanding of ethics is like dividing by zero – undefined and causing everyone around you discomfort.",
      "Are you made of dark matter? Because you're difficult to detect and have no observable impact on my life.",
      "I'd ask about your achievements, but I'm not sure counting to ten qualifies as groundbreaking research.",
      "Your arrogance is a prime example of the Dunning-Kruger effect, but I doubt you'd even understand that."
    ]
    await interaction.response.send_message(f"{random.choice(responses)}")

  @app_commands.command(name="rizz", description="Generates a random pickup line.")
  async def rizz(self, interaction: discord.Interaction):
    responses = [
      "If you were a molecule, you'd be one of a kind. You must be made of rare earth elements.",
      "Is your name Google? Because you have everything I've been searching for.",
      "You must be the square root of -1 because you can't be *real*, but I can't help but *imagine* us together.",
      "If beauty were a function, you'd be the asymptote I'd never reach but always strive for.",
      "Are you a carbon sample? Because I want to *date* you.",
      "Are you an electron? Because you're always in a state of constant motion around me.",
      "Are you a supernova? Because you're explosively attractive.",
      "Are you an angle? Because you're *acute* one.",
      "Is your name Euler? Because I'd like to introduce you to my *i*-deal partner.",
      "Are you a prime number? Because you can only be divided by one, and you've divided my heart from the rest.",
      "Are you a magician? Because whenever I look at you, everyone else disappears.",
      "Are you a campfire? Because you're hot and I want s'more.",
      "Do you believe in love at first sight, or should I walk by again?",
      "Is your name Angel? Because you must have fallen from heaven.",
      "Are you a time traveler? Because I can see you in my future.",
      "Are you a camera? Every time I look at you, I smile.",
      "Do you have a sunburn, or are you always this hot?",
      "Are you a bank loan? Because you have my interest.",
      "Is there an airport nearby or is that just my heart taking off?",
      "If beauty were a crime, you'd be serving a life sentence."
    ]
    await interaction.response.send_message(f"{random.choice(responses)}")

  @app_commands.command(name="truthordare", description="Play a game of Truth or Dare.")
  @app_commands.describe(choice = "Choose between a Truth or a Dare...")
  @app_commands.choices(choice = [
    app_commands.Choice(name= "Truth", value= "t"),
    app_commands.Choice(name= "Dare", value= "d"),
    app_commands.Choice(name= "Random", value= "r")
  ])
  async def truthordare(self, interaction: discord.Interaction, choice: str="r"):
    tod = True
    if choice == "r":
      tod = random.choice([True, False])
    elif choice == "d":
      tod = False
    if tod == True:
      n = random.randint(1,len(TOD_TRUTHS))
      t = TOD_TRUTHS[n][0]
      c = 0xaaffaa
      f = f"Truth {n}/{len(TOD_TRUTHS)} · Created by @{TOD_TRUTHS[n][1]}"
    else:
      n = random.randint(1,len(TOD_DARES))
      t = TOD_DARES[n][0]
      c = 0xffaaaa
      f = f"Dare {n}/{len(TOD_DARES)} · Created by @{TOD_DARES[n][1]}"
    e = discord.Embed(title=t,colour=c)
    e.set_footer(text=f)
    await interaction.response.send_message(interaction.user.mention,embed=e)    

  @app_commands.command(name="ninetynine", description="Play the number game 'ninetynine' created by AJ Goh.")
  @app_commands.choices(difficulty = [
    Choice(name= "How to Play", value= "Tutorial"),
    Choice(name= "Easy", value= "Easy"),
    Choice(name= "Medium", value= "Medium"),
    Choice(name= "Hard", value= "Hard"),
    Choice(name= "Nine nines", value= "Nine nines")
])
  @app_commands.describe(difficulty="Select your desired difficulty.")
  async def ninetynine(self, interaction: discord.Interaction, difficulty: str):
    if interaction.channel.type == discord.ChannelType.private:
      Embed = discord.Embed(description="Sorry, this command is not available in DMs.", color=0xffaaaa)
      Embed.set_author(name="ninetynine", icon_url=NINETYNINE_LOGO)
      Embed.set_footer(text="Created by AJ Goh")
      await interaction.response.send_message(embed=Embed)
      return
  
    if difficulty == "Tutorial":
      e = discord.Embed(
        title="Welcome to ninetynine!",
        description=NINETYNINE_DESC,
        colour=0xffffff)
      e.set_author(name="ninetynine", icon_url=NINETYNINE_LOGO)
      e.set_footer(text="Created by AJ Goh")
      e.set_image(url=NINETYNINE)
      await interaction.response.send_message(embed=e)

    else: 
      if interaction.user.id in Games:
        embed = discord.Embed(
          description="You already have an existing game session, would you like to delete it?",
          color=0xffaaaa
        )
        embed.set_author(name="ninetynine")
        embed.set_footer(text="Created by AJ Goh")
        await interaction.response.send_message(embed=embed)
        view = YesNo(message=interaction, UserID=interaction.user.id)
        await interaction.edit_original_response(view=view)
      else:
        if difficulty == "Easy":
          Games[interaction.user.id] = {}
          Games[interaction.user.id]['Goal'] = 9

        elif difficulty == "Medium":
          Games[interaction.user.id] = {}
          Games[interaction.user.id]['Goal'] = 99

        elif difficulty == "Hard":
          Games[interaction.user.id] = {}
          Games[interaction.user.id]['Goal'] = 999

        elif difficulty == "Nine nines":
          Games[interaction.user.id] = {}
          Games[interaction.user.id]['Goal'] = 999999999
        
        # Button values
        decrease_numbers = random.sample(range(1, (Games[interaction.user.id]['Goal']+1)//2 + 1), 2)
        Games[interaction.user.id]['Decrease1'] = decrease_numbers[0]
        Games[interaction.user.id]['Decrease2'] = decrease_numbers[1]

        increase_numbers = random.sample(range(1, (Games[interaction.user.id]['Goal']+1)//2 + 1), 3)
        Games[interaction.user.id]['Increase1'] = increase_numbers[0]
        Games[interaction.user.id]['Increase2'] = increase_numbers[1]
        Games[interaction.user.id]['Increase3'] = increase_numbers[2]

        # Other info
        Games[interaction.user.id]['Current'] = random.randint(0, (Games[interaction.user.id]['Goal'] - 1)/2)
        Games[interaction.user.id]['Name'] = interaction.user.name
        Games[interaction.user.id]['Turn'] = 1

        # Sends the message
        embed = discord.Embed(
          title=f"{Games[interaction.user.id]['Current']}",
          description=f"Get the number above to **{Games[interaction.user.id]['Goal']}** to win. This is turn **#{Games[interaction.user.id]['Turn']}**.",
          color=0xffaaaa
        )
        embed.set_author(name="ninetynine", icon_url=NINETYNINE_LOGO)
        embed.set_footer(text="Created by AJ Goh")
        await interaction.response.defer()
        message = await interaction.followup.send(embed=embed, wait=True)
        view = Buttons(message=message, UserID=interaction.user.id)
        await interaction.edit_original_response(view=view)

        # Record the channel and message IDs
        Games[interaction.user.id]['Channel'] = interaction.channel_id
        Games[interaction.user.id]['Message'] = message.id

  @app_commands.command(name="highlowinf", description="Play the guessing game 'HighLow Infinite' created by AJ Goh.")
  @app_commands.choices(difficulty = [
    Choice(name= "How to Play", value= "Tutorial"),
    Choice(name= "Easy", value= "Easy"),
    Choice(name= "Medium", value= "Medium"),
    Choice(name= "Hard", value= "Hard"),
    Choice(name= "Extreme", value= "Extreme")
  ])
  @app_commands.describe(difficulty="Select your desired difficulty.")
  async def highlowinf(self, interaction: discord.Interaction, difficulty: str):
    if interaction.channel.type == discord.ChannelType.private:
      Embed = discord.Embed(description="Sorry, this command is not available in DMs.", color=0xaaffaa)
      Embed.set_author(name="HighLow Infinite", icon_url=HIGHLOWINF_LOGO)
      Embed.set_footer(text="Created by AJ Goh")
      await interaction.response.send_message(embed=Embed)
      return
  
    if difficulty == "Tutorial":
      e = discord.Embed(
        title="Welcome to HighLow Infinite!",
        description=HIGHLOWINF_DESC,
        colour=0xffffff)
      e.set_author(name="HighLow Infinite", icon_url=HIGHLOWINF_LOGO)
      e.set_footer(text="Created by AJ Goh")
      e.set_image(url=HIGHLOWINF)
      await interaction.response.send_message(embed=e)

    else: 
      if interaction.user.id in HLGames:
        embed = discord.Embed(
          description="You already have an existing game session, would you like to delete it?",
          color=0xffaaaa
        )
        embed.set_author(name="HighLow Infinite", icon_url=HIGHLOWINF_LOGO)
        embed.set_footer(text="Created by AJ Goh")
        await interaction.response.send_message(embed=embed)
        view = YesNo(message=interaction, UserID=interaction.user.id)
        await interaction.edit_original_response(view=view)
      else:
        if difficulty == "Easy":
          HLGames[interaction.user.id] = {}
          HLGames[interaction.user.id]['Min'] = 1
          HLGames[interaction.user.id]['Max'] = 10

        elif difficulty == "Medium":
          HLGames[interaction.user.id] = {}
          HLGames[interaction.user.id]['Min'] = 1
          HLGames[interaction.user.id]['Max'] = 100

        elif difficulty == "Hard":
          HLGames[interaction.user.id] = {}
          HLGames[interaction.user.id]['Min'] = 1
          HLGames[interaction.user.id]['Max'] = 1000

        elif difficulty == "Extreme":
          HLGames[interaction.user.id] = {}
          HLGames[interaction.user.id]['Min'] = 1
          HLGames[interaction.user.id]['Max'] = 1000000
        
        # Game number, guess number, range
        HLGames[interaction.user.id]['N'] = random.randint(1, HLGames[interaction.user.id]['Max'])
        HLGames[interaction.user.id]['G'] = random.randint(1, HLGames[interaction.user.id]['Max'])
        HLGames[interaction.user.id]['R'] = HLGames[interaction.user.id]['Max']

        # Other info
        HLGames[interaction.user.id]['Name'] = interaction.user.name
        HLGames[interaction.user.id]['Turn'] = 1

        # Sends the message
        embed = discord.Embed(
          description=f"(Turn **#{HLGames[interaction.user.id]['Turn']}**)\nI am thinking of a number between **1** and **{HLGames[interaction.user.id]['R']}** inclusive.\n# Is it higher than, lower than, or equal to __{HLGames[interaction.user.id]['G']}__?",
          color=0xaaffaa
        )
        embed.set_author(name="HighLow Infinite", icon_url=HIGHLOWINF_LOGO)
        embed.set_footer(text="Created by AJ Goh")
        await interaction.response.defer()
        message = await interaction.followup.send(embed=embed, wait=True)
        view = HLButtons(message=message, UserID=interaction.user.id)
        await interaction.edit_original_response(view=view)

        # Record the channel and message IDs
        HLGames[interaction.user.id]['Channel'] = interaction.channel_id
        HLGames[interaction.user.id]['Message'] = message.id

async def setup(bot):
  await bot.add_cog(SlashCmd_Fun(bot))
