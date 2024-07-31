import discord, os, asyncio, shutil, textwrap
from discord import app_commands
from discord.ext import commands
from datetime import datetime, timedelta
from dotenv import load_dotenv
from easy_pil import Editor, Canvas, Font, utils
from misc.keep_alive import keep_alive
from misc.messages import WELCOME_MESSAGE, WELCOME_MESSAGE_STAFF, WELCOME_MESSAGE_NONE, SERVER_RULES
from misc.images import RULEBOOK, QUOTE_BG

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
  input = "Input the desired text or message ID.",
  fetch = "Select where to fetch the input from."
)
@app_commands.choices(fetch = [
  app_commands.Choice(name= "Text Input", value= "txt"),
  app_commands.Choice(name= "Message ID", value= "id")
])
async def dm(interaction: discord.Interaction, user: discord.User, input: str, fetch: str="txt"):
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
@app_commands.describe(
  input = "Input the desired text of message ID.",
  fetch = "Select where to fetch the input from. (Default: Text Input)",
  ai = "Select whether to add the GohAI subtext. (Default: False)",
  repeat = "Input the number of times to send the message. (Default: 1, Limit: 20)"
  )
@app_commands.choices(fetch = [
  app_commands.Choice(name= "Text Input", value= "txt"),
  app_commands.Choice(name= "Message ID", value= "id")
])
async def msg(interaction: discord.Interaction, input: str, fetch: str="txt", ai: bool=False, repeat: int=1):
  if interaction.user.id != 832811319957651457:
    await interaction.response.send_message("You are not authorized to use this command.", ephemeral=True)
    return
  if ai == True:
    ai_text = "\n-# This message is generated by [GohAI](<https://www.youtube.com/c/ajgoh>). Should you require any assistance or support with regard to GohAI, feel free to [request for support](https://discord.com/channels/940996562715291748/1239117004401545298)."
  else:
    ai_text = ""
  if repeat < 1:
    repeat = 1
  elif repeat > 20:
    repeat = 20
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
  for i in range(repeat):
    await interaction.channel.send(msg+ai_text)
  await interaction.response.send_message(f"Message(s) sent.", ephemeral=True)

# QUOTE COMMAND

@bot.tree.command(name="quote", description="Quote someone's message.")
@app_commands.describe(message_id="Input the ID of the desired message.")
async def quote(interaction: discord.Interaction, message_id: str):
  try:
    message = await interaction.channel.fetch_message(int(message_id))
    background = Canvas((1024, 512), color=(0, 0, 100))
    overlay_link = QUOTE_BG
    font_main = Font("misc/jack-armstrong.ttf", 24)
    font_sub = Font("misc/jack-armstrong.ttf", 12)
    text_main = message.content

    if message.author.avatar == None:
      pfp_link = utils.load_image("https://cdn.discordapp.com/embed/avatars/0.png")
    else:
      pfp_link = await utils.load_image_async(message.author.avatar.url)

    if (len(str(message.author.display_name))>=16) or (len(str(message.author.name))>=16):
      text_sub = [f"{message.author.display_name}",f"(@{message.author.name})"]
    else:
      text_sub = [f"{message.author.display_name} (@{message.author.name})"]

    editor = Editor(background.image)
    pfp = pfp_link.resize((512,512))
    overlay = utils.load_image(overlay_link)
    text = textwrap.wrap(text_main, width=32)

    editor.paste(pfp, (-64,0))
    editor.paste(overlay, (0,0))

    for i in range(len(text)):
      editor.text((700,(256-(15*len(text))+(30*i))), text=text[i], font=font_main, color=0xffffff, align="center")
    for j in range(len(text_sub)):  
      editor.text((700,(270+(15*len(text))+15*j)), text=text_sub[j], font=font_sub, color=0x808080, align="center")

    editor = editor.image.convert("L")
    editor.save(fp="misc/quote.png")
    file = discord.File("misc/quote.png")
    await interaction.response.send_message(file=file)

  except discord.NotFound:
    await interaction.response.send_message("Message not found.")
  except discord.Forbidden:
    await interaction.response.send_message("I do not have permission to read messages in that channel.")
  except discord.HTTPException as e:
    await interaction.response.send_message(f"Failed to fetch message: {e}")
  except Exception as ee:
    await interaction.response.send_message(f"An error occured: {ee}")

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