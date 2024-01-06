# List of commands here:
# 1. test
# 2. afk

from discord.ext import commands

class TextCommands(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.data = []
  
  @commands.command()
  async def test(self, ctx):
      await ctx.reply(f"✅ {self.bot.user} (ID: {self.bot.user.id}) is currently online.")

  @commands.command()
  async def afk(self, ctx, *args):
    msg = " ".join(args)
    self.data.append(ctx.author.id)
    self.data.append(msg)
    await ctx.channel.send(f"<@{ctx.author.id}> is now AFK.\n> {msg}")
    
  @commands.Cog.listener()
  async def on_message(self, message):
    for i in range(len(self.data)):
      if (f"<@{self.data[i]}>" in message.content) and (not message.author.bot):
        await message.channel.send(f"<@{self.data[i]}> is currently AFK.\n> {self.data[i+1]}")
        return None
        break

  @commands.Cog.listener()
  async def on_typing(self, channel, user, when):
    if user.id in self.data:
      i = self.data.index(user.id)
      self.data.remove(self.data[i+1])
      self.data.remove(user.id)
      await channel.send(f"I see you typing... Welcome back, {user.mention}!")

async def setup(bot):
    await bot.add_cog(TextCommands(bot))