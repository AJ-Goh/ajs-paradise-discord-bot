import discord, os, asyncio, time, random, shutil
from discord import app_commands
from discord.ext import commands
from discord.ui import View
from discord.app_commands import Choice
from datetime import datetime, timedelta
from dotenv import load_dotenv
from misc.keep_alive import keep_alive
from misc.messages import WELCOME_MESSAGE, WELCOME_MESSAGE_STAFF, WELCOME_MESSAGE_NONE, NINETYNINE_DESC, SERVER_RULES
from misc.images import RULEBOOK, NINETYNINE

# INTENTS AND TOKEN

bot = commands.Bot(command_prefix="!aj ", intents = discord.Intents.all())

load_dotenv()
BOT_TOKEN = os.environ['TOKEN']

# KEEP ALIVE

keep_alive()

# LOAD COGS

async def load():
  for filename in os.listdir("./commands"):
    if filename.endswith(".py"):
      await bot.load_extension(f"commands.{filename[:-3]}")
      print(f"✅ Loaded cog: {filename}")

# DEFINE MAIN

async def main():
  async with bot:
    await load()
    await bot.start(BOT_TOKEN)

# DEFINE KEYWORDS

def keywords(message: str, keywords: list):
  return any(message.startswith(f"{item} ") or message.endswith(f" {item}") or f" {item} " in message or item == message for item in keywords)

# DEFINE BACKUP

def backup(source_path, destination_folder):
  try:
    # Get current date and time
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # Create a destination file name with timestamp
    destination_file = f"{destination_folder}/backup_{timestamp}.json"
    # Copy the file
    shutil.copy(source_path, destination_file)
    print(f"💟 JSON file backed up successfully to {destination_file}")
  except FileNotFoundError:
    print("Source file not found.")
  except Exception as e:
    print(f"An error occurred: {e}")

def files_check(directory, condition):
  try:
    # List all files in the directory
    files = os.listdir(directory)
    if not files:
      print(f"🆘 No files found in the directory: {directory}")
      return False
    for file in files:
      if condition in file:
        return True
    return False
  except FileNotFoundError:
    print(f"🆘 Directory not found: {directory}")
    return False
  except Exception as e:
    print(f"🆘 An error occurred: {e}")
    return False

# ON MESSAGE

@bot.event
async def on_message(msg):

  if msg.author == bot.user:
    a = str(msg.author)[:-5]
  else:
    a = str(msg.author)

  if msg.content != "":
    if len(a) > 15:
      print(f"💬 @{a[:12]+'...  '}"+ msg.content)
    else:
      print(f"💬 @{a + (17-len(a))*' '}"+ msg.content)

  TIME_TODAY = datetime.now().strftime("%Y-%m-%d")
  DATE_TODAY = datetime.now().strftime("%d")

  if (int(DATE_TODAY)%2==1) and not files_check("data/backup_messages", TIME_TODAY):
    backup("data/data_messages.json", "data/backup_messages")
# if (int(DATE_TODAY)%2==1) and not files_check("data/backup_mm", TIME_TODAY):
#   backup("data/data_mm.json", "data/backup_mm")

  if msg.author == bot.user:
    return
    
  m = msg.content.lower()
  reply_type = None
  reply_content = None
  
  # Hello
  if keywords(m, ["hi", "hello", "sup", "wsg", "wsp", "yo"]):
    reply_type = "text"
    reply_content = "Hello!"
    
  # Goodbye
  elif keywords(m, ["bye", "cya"]):
    reply_type = "text"
    reply_content = "Goodbye!"
    
  # Subscribe
  elif keywords(m, ["sub", "subs", "subbing", "subscribe", "subscriber", "subscribers", "subscribing"]):
    e = discord.Embed(description="Subscribe to the AJ Goh YouTube channel to earn exclusive perks in the server! Feel free to proceed to <#972449159867138048> to learn more about those perks, and to <#972449220328046642> to get them!", colour=0xffcc00)
    e.set_footer(text="This embed was sent due to the 'subscribe' trigger.")
    reply_type = "embed"
    reply_content = e
    
  # Boost
  elif keywords(m, ["boost", "booster", "boosters", "boosting"]):
    e = discord.Embed(description="Boost this Discord server to earn epic rewards! Feel free to proceed to <#1137638418071957564> to learn more about them!", colour=0xffcc00)
    e.set_footer(text="This embed was sent due to the 'boost' trigger.")
    reply_type = "embed"
    reply_content = e
    
  # Giveaway
  elif keywords(m, ["gw", "giveaway", "giveaways"]):
    e = discord.Embed(description="Every 2 weeks, a giveaway for **400 Robux** is hosted in AJ's Paradise!\n \nSimply head to <#957854693688746004> to join the current giveaway. Take note that you need to send **20 messages** in the server to be **eligible** to join one, so if you have not yet met that requirement, feel free start or join a conversation in <#940996564384628767>!", colour=0xffcc00)
    e.set_footer(text="This embed was sent due to the 'giveaway' trigger.")
    reply_type = "embed"
    reply_content = e
    
  # Message
  elif keywords(m, ["msg", "msgs", "message", "messages"]):
    e = discord.Embed(description="Redeem **400 Robux** for every 20 message levels!\n \nChat in this server to increase your message level! You may use the </message stats:1139339144787673281> command in <#940996564384628768> to check your message level.", colour=0xffcc00)
    e.set_footer(text="This embed was sent due to the 'message' trigger.")
    reply_type = "embed"
    reply_content = e
    
  # Sponsor
  elif keywords(m, ["sponsor", "sponsors", "sponsored"]):
    e = discord.Embed(description="Host and announce a sponsored item in AJ's Paradise! Be it a giveaway, an event, a mini game, or any sort of item, simply use </reqsponsor:1140139050934743181> in <#940996564384628768> to request to host a sponsored item in the server!\n \nYou may also view past and upcoming sponsored items in <#1100423394526240778>.", colour=0xffcc00)
    e.set_footer(text="This embed was sent due to the 'sponsor' trigger.")
    reply_type = "embed"
    reply_content = e

  # Reply
  if reply_type == None:
    return
  if reply_type == "text":
    reply_msg = await msg.reply(reply_content)
  if reply_type == "embed":
    reply_msg = await msg.reply(embed=reply_content, delete_after=10.0)

  # Wait for reactions (300s)
  def check(reaction, user):
    return user == msg.author and reaction.message.id == reply_msg.id

  try:
    reaction, user = await bot.wait_for('reaction_add', timeout=300.0, check=check)
  except asyncio.TimeoutError:
    pass # No reaction within the timeout
  else:
    await reply_msg.delete() # Deletes the original message
    
  # REQUIRED: Checks afterwards if message is a command
  await bot.process_commands(msg)

# DM ON JOIN

@bot.event
async def on_member_join(mbr):
  # AJ's Paradise
  if mbr.guild.id == 940996562715291748:
    msg = WELCOME_MESSAGE.format(mbr)
    clr = "🟡"
  # AJ's Paradise Staff Team
  elif mbr.guild.id == 1123598807985303664:
    msg = WELCOME_MESSAGE_STAFF.format(mbr)
    clr = "🟠"
  # None of the Above
  else:
    msg = WELCOME_MESSAGE_NONE.format(mbr)
    clr = "🟢"
  
  await mbr.create_dm()
  await mbr.dm_channel.send(msg)
  
  aj_user = bot.get_user(832811319957651457)
  await aj_user.create_dm()
  await aj_user.dm_channel.send(f"## {clr} Member Join\n- **ORDER**  {mbr.guild.member_count}\n- **USER**  {mbr.name}\n- **ID**  ||`ID: {mbr.id}`||\n- **SERVER**  {mbr.guild.name}")
  
  general = bot.get_channel(940996564384628767)
  join_channel = bot.get_channel(1203190503844216893)
  if mbr.guild.id == 940996562715291748:
    await general.send(f"Welcome {mbr.mention} to AJ's Paradise!")
    await join_channel.send(f"## 🔺 Member Join\n- **ORDER**  {mbr.guild.member_count}\n- **USER**  {mbr.name}\n- **ID**  ||`ID: {mbr.id}`||\n- **SERVER**  {mbr.guild.name}")

# DM ON LEAVE

@bot.event
async def on_member_remove(mbr):
  # AJ's Paradise
  if mbr.guild.id == 940996562715291748:
    c = "🟨"
  # AJ's Paradise Staff Team
  elif mbr.guild.id == 1123598807985303664:
    c = "🟧"
  # None of the Above
  else:
    c = "🟩"

  aj_user = bot.get_user(832811319957651457)
  await aj_user.create_dm()
  await aj_user.dm_channel.send(f"## {c} Member Leave\n- **ORDER**  {mbr.guild.member_count}\n- **USER**  {mbr.name}\n- **ID**  ||`ID: {mbr.id}`||\n- **SERVER**  {mbr.guild.name}")

  leave_channel = bot.get_channel(1203190717673902241)
  if mbr.guild.id == 940996562715291748:
    await leave_channel.send(f"## 🔻 Member Leave\n- **ORDER**  {mbr.guild.member_count}\n- **USER**  {mbr.name}\n- **ID**  ||`ID: {mbr.id}`||\n- **SERVER**  {mbr.guild.name}")

# SERVER RULES

class RulesView(discord.ui.View):
  def __init__(self):
    super().__init__()
    self.value = None

@bot.tree.command(name="rules", description="View the rules and guidelines of AJ's Paradise.")
async def rules(interaction: discord.Interaction):
  embed = discord.Embed(
    title = "AJ's Paradise Server Rules",
    description = SERVER_RULES,
    colour = 0xffcc00
  )
  embed.set_thumbnail(url=RULEBOOK)
  view = RulesView()
  view.add_item(discord.ui.Button(
    label = "View All Rules",
    style = discord.ButtonStyle.link,
    url = "https://sites.google.com/view/ajgoh/discord-server/server-rules"
  ))
  await interaction.response.send_message(embed=embed, view=view)

# TIMESTAMP GENERATOR

@bot.tree.command(name="timestamp", description="Get the timestamp for a date and time input.")
@app_commands.describe(
  date = "Input the desired date in the format: ddmmYYYY",
  time = "Input the desired time (in GMT+08 for AJ's convenience) in the format: HHMMSS",
  type = "Input the desired type of the timestamp."
)
@app_commands.choices(type = [
  app_commands.Choice(name= "Short Time", value= "t"),
  app_commands.Choice(name= "Long Time", value= "T"),
  app_commands.Choice(name= "Short Date", value= "d"),
  app_commands.Choice(name= "Long Date", value= "D"),
  app_commands.Choice(name= "Long Date and Time", value= "f"),
  app_commands.Choice(name= "Long Date, Time and Weekday", value= "F"),
  app_commands.Choice(name= "Relative to Current Time", value= "R")
])
async def timestamp(interaction: discord.Interaction, date: str, time: str, type: str):
  
  if date.lower() in ['today', 'tdy']:
    target_date = datetime.now().date()
  elif date.lower() in ['tomorrow', 'tmr']:
    target_date = datetime.now().date() + timedelta(days=1)
  elif date.lower() in ['yesterday', 'ytd']:
    target_date = datetime.now().date() - timedelta(days=1)
  else:
    try:
        target_date = datetime.strptime(date, "%d%m%Y").date()
    except ValueError:
        await interaction.response.send_message("Error: Invalid date format.")
        return

  now_time = False
  if time.lower() == 'now':
    now_time = True
    current_time = datetime.now().time()
  else:
    try:
        current_time = datetime.strptime(time, "%H%M%S").time()
    except ValueError:
        await interaction.response.send_message("Error: Invalid time format.")
        return

  input_string = target_date.strftime("%d%m%Y") + current_time.strftime("%H%M%S")

  def convert_to_timestamp(i):
    try:
        date_format = "%d%m%Y%H%M%S"
        datetime_obj = datetime.strptime(i, date_format)
        timestamp = int(datetime_obj.timestamp())
        if now_time:
          return f"<t:{timestamp}:{type}>"
        else:
          return f"<t:{timestamp-28800}:{type}>"
    except ValueError:
        return "Error: Invalid input format."

  timestamp = convert_to_timestamp(input_string)
  await interaction.response.send_message(timestamp)

# DM COMMAND

@bot.tree.command(name="dm", description="(Administrator Only) DM a user.")
@app_commands.describe(
  user = "Which user to DM.",
  fetch = "Where to fetch the input from.",
  input = "Input the desired text or message ID."
)
@app_commands.choices(fetch = [
  app_commands.Choice(name= "Text Input", value= "txt"),
  app_commands.Choice(name= "Message ID", value= "id")
])
async def dm(interaction: discord.Interaction, user: discord.User, fetch: str, input: str):
  if interaction.user.id != 832811319957651457:
    await interaction.response.send_message("You are not authorized to use this command.", ephemeral=True)
    return
  if fetch == "txt":
    msg = input
  elif fetch == "id":
    try:
      channel = await bot.fetch_channel(interaction.channel_id)
      message = await channel.fetch_message(int(input))
      msg = message.content
    except ValueError:
      await interaction.response.send_message("Invalid message ID.")
      return
  await user.create_dm()
  await user.dm_channel.send(msg)
  await interaction.response.send_message(f"Message sent to {user.mention}: \n\n{msg}", ephemeral=True)

# MSG COMMAND

@bot.tree.command(name="msg", description="(Administrator Only) Send a message.")
@app_commands.describe(input = "Input the desired text.")
async def msg(interaction: discord.Interaction, input: str):
  if interaction.user.id != 832811319957651457:
    await interaction.response.send_message("You are not authorized to use this command.", ephemeral=True)
    return
  await interaction.channel.send(input)
  await interaction.response.send_message(f"Message sent.", ephemeral=True)

# NINETYNINE

# << Stores The Game >> #
Games = {}

# << Function To Add The Value >> # 
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
    
# << Function To Disable All Of The Buttons >> #
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

# << Class For The Buttons >> #
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
            embed.set_author(name="ninetynine")
            embed.set_footer(text="Created by AJ Goh")
        else:
            Win = False
            embed = discord.Embed(
                title=f"{Games[interaction.user.id]['Current']}",
                description=f"Get the number above to **{Games[interaction.user.id]['Goal']}** to win. This is turn **#{Games[interaction.user.id]['Turn']}**.",
                color=0xffaaaa
            )
            embed.set_author(name="ninetynine")
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
            embed.set_author(name="ninetynine")
            embed.set_footer(text="Created by AJ Goh")
        else:
            Win = False
            embed = discord.Embed(
                title=f"{Games[interaction.user.id]['Current']}",
                description=f"Get the number above to **{Games[interaction.user.id]['Goal']}** to win. This is turn **#{Games[interaction.user.id]['Turn']}**.",
                color=0xffaaaa
            )
            embed.set_author(name="ninetynine")
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
            embed.set_author(name="ninetynine")
            embed.set_footer(text="Created by AJ Goh")
        else:
            Win = False
            embed = discord.Embed(
                title=f"{Games[interaction.user.id]['Current']}",
                description=f"Get the number above to **{Games[interaction.user.id]['Goal']}** to win. This is turn **#{Games[interaction.user.id]['Turn']}**.",
                color=0xffaaaa
            )
            embed.set_author(name="ninetynine")
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
            embed.set_author(name="ninetynine")
            embed.set_footer(text="Created by AJ Goh")
        else:
            Win = False
            embed = discord.Embed(
                title=f"{Games[interaction.user.id]['Current']}",
                description=f"Get the number above to **{Games[interaction.user.id]['Goal']}** to win. This is turn **#{Games[interaction.user.id]['Turn']}**.",
                color=0xffaaaa
            )
            embed.set_author(name="ninetynine")
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
            embed.set_author(name="ninetynine")
            embed.set_footer(text="Created by AJ Goh")
        else:
            Win = False
            embed = discord.Embed(
                title=f"{Games[interaction.user.id]['Current']}",
                description=f"Get the number above to **{Games[interaction.user.id]['Goal']}** to win. This is turn **#{Games[interaction.user.id]['Turn']}**.",
                color=0xffaaaa
            )
            embed.set_author(name="ninetynine")
            embed.set_footer(text="Created by AJ Goh")

        await interaction.edit_original_response(embed=embed, view=self)
        if Win:
            del Games[interaction.user.id]

# << Class For The Yes/No >> #
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
        Embed.set_author(name="ninetynine")
        Embed.set_footer(text="Created by AJ Goh")
        await interaction.edit_original_response(embed=Embed, view=None)

        ChannelID = Games[interaction.user.id]['Channel']
        Channel = bot.get_channel(ChannelID)

        MessageID = Games[interaction.user.id]['Message']
        Message = await Channel.fetch_message(MessageID)
        await Message.delete()

        del Games[interaction.user.id]
        Embed = discord.Embed(description="Successfully deleted the previous session. You may proceed to run the command again to start a new game session.", color=0xffaaaa)
        Embed.set_author(name="ninetynine")
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
        Embed.set_author(name="ninetynine")
        Embed.set_footer(text="Created by AJ Goh")
        Message = await interaction.edit_original_response(embed=Embed, view=None)
        time.sleep(3)
        await Message.delete()

# << Slash Command >> #
@app_commands.choices(difficulty = [
    Choice(name= "How to Play", value= "Tutorial"),
    Choice(name= "Easy", value= "Easy"),
    Choice(name= "Medium", value= "Medium"),
    Choice(name= "Hard", value= "Hard"),
    Choice(name= "Nine nines", value= "Nine nines")
])
@bot.tree.command(name="ninetynine", description="Play the number game 'ninetynine' created by AJ Goh.")
@app_commands.describe(difficulty="Select your desired difficulty.")
async def Game(interaction: discord.Interaction, difficulty: str):
    if interaction.channel.type == discord.ChannelType.private:
        Embed = discord.Embed(description="Sorry, this command is not available in DMs.", color=0xffdddd)
        Embed.set_author(name="ninetynine")
        Embed.set_footer(text="Created by AJ Goh")
        await interaction.response.send_message(embed=Embed)
        return
    
    if difficulty == "Tutorial":
      e = discord.Embed(title="Welcome to ninetynine!",
                        description=NINETYNINE_DESC,
                        colour=0xffffff)
      e.set_author(name="ninetynine")
      e.set_footer(text="Created by AJ Goh")
      e.set_image(url=NINETYNINE)
      await interaction.response.send_message(embed=e)

    else: 
        # << Prevent Players From Having More Than 1 Games At A Time >> #
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

            # << Set The Difficulty Stuff >> #
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
            
            # << Increase/Decrease >> #
            decrease_numbers = random.sample(range(1, (Games[interaction.user.id]['Goal']+1)//2 + 1), 2)
            Games[interaction.user.id]['Decrease1'] = decrease_numbers[0]
            Games[interaction.user.id]['Decrease2'] = decrease_numbers[1]

            increase_numbers = random.sample(range(1, (Games[interaction.user.id]['Goal']+1)//2 + 1), 3)
            Games[interaction.user.id]['Increase1'] = increase_numbers[0]
            Games[interaction.user.id]['Increase2'] = increase_numbers[1]
            Games[interaction.user.id]['Increase3'] = increase_numbers[2]

            # << Other Stats >> #
            Games[interaction.user.id]['Current'] = random.randint(0, (Games[interaction.user.id]['Goal'] - 1)/2)
            Games[interaction.user.id]['Name'] = interaction.user.name
            Games[interaction.user.id]['Turn'] = 1

            # << Send The Message >> #
            embed = discord.Embed(
                title=f"{Games[interaction.user.id]['Current']}",
                description=f"Get the number above to **{Games[interaction.user.id]['Goal']}** to win. This is turn **#{Games[interaction.user.id]['Turn']}**.",
                color=0xffaaaa
            )
            embed.set_author(name="ninetynine")
            embed.set_footer(text="Created by AJ Goh")
            await interaction.response.defer()
            message = await interaction.followup.send(embed=embed, wait=True)
            view = Buttons(message=message, UserID=interaction.user.id)
            await interaction.edit_original_response(view=view)

            # << Set The Channel And Message >> #
            Games[interaction.user.id]['Channel'] = interaction.channel_id
            Games[interaction.user.id]['Message'] = message.id

# ON READY

@bot.event
async def on_ready():
  Synced = await bot.tree.sync()
  if Synced:
    print("✅ Bot commands have been synchronised successfully.")
  print(f"✅ {bot.user} (ID: {bot.user.id}) is now online.")

# MAIN

asyncio.run(main())
bot.run(token=BOT_TOKEN)