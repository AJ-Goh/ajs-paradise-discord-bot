# List of commands here:
# 1. rng
# 2. rps
# 3. 8ball
# 4. roast
# 5. rizz

import discord, random
from discord import app_commands
from discord.ext import commands

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

async def setup(bot):
  await bot.add_cog(SlashCmd_Fun(bot))