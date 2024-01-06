# List of messages so far:
# 1. CHANGELOG_LIST
# 2. WELCOME_MESSAGE
# 3. WELCOME_MESSAGE_STAFF
# 4. WELCOME_MESSAGE_NONE
# 5. GOODBYE_MESSAGE
# 6. NINETYNINE_DESC
# 7. SERVER_RULES

CHANGELOG_LIST = [
  "Version 2.0.0", # VERSION NUMBER (X.Y.Z)
  "6 January 2024", # DATE (FULL)
  "0900", # TIME (24HR, GMT)
  """

- Successfully migrated from Replit to Pylex for bot hosting
  - Replit no longer offering free hosting from 2024
  - Also transferred code to GitHub just in case
- Created a separate file to contain image links
  - Images hosted by Google Photos

"""]

WELCOME_MESSAGE = """

# Welcome to **{0.guild.name}**!

Hello {0.mention} (Member **#{0.guild.member_count}**), and welcome to **{0.guild.name}**!

{0.guild.name} is a welcoming hub for gamers, music lovers, and all sorts of people looking to connect, unwind, and have a blast together. Engage in lively conversations, dive into epic gaming sessions, make a new friend or two, or simply unwind with the cool community.

You also stand to earn rewards simply by chatting in the server: **400 Robux** for every 10 message levels (no spamming)!

To learn more about the server, feel free to watch this video: https://www.youtube.com/watch?v=ZVREJBOaSEg

Please view the list of rules in <#940996563789025313>, lest you get unknowingly punished for an accidental offense. If you have any suggestions or reports, you may proceed to <#1169516956811014144> or <#941002010088587295> respectively, or send a direct message to **@ajgoh** (on Discord).

I also have a YouTube channel ([**@AJGoh**](<https://www.youtube.com/@ajgoh>)) where I post weekly Roblox content, as well as another YouTube channel ([**@AJGohMusic**](<https://www.youtube.com/@ajgohmusic>)) where I showcase my music creations. Consider subscribing to them to support me and gain additional perks in the server, as stated in <#972449159867138048>.

With that all said, I hope you will have a good time in the server. Take care and have fun!

Best regards,
AJ Goh, Owner of {0.guild.name}.

"""

WELCOME_MESSAGE_STAFF = """

# Welcome to **{0.guild.name}**!

Hello {0.mention} (Member **#{0.guild.member_count}**), and welcome to **{0.guild.name}**!

If you have made it into the server, you have probably joined for the following 2 reasons:
1. You have been successfully hired as a Staff Team member of the AJ's Paradise Discord server.
2. You have been invited here by some random person for no apparent reason.

If you are not a Staff Team member of AJ's Paradise, please kindly leave the Discord server immediately as you are not supposed to be in there.

If you are a Staff Team member of AJ's Paradise, you may begin work whenever you area ready, and you may contact any of the other staff if you need any assistance or guidance.

Besides that, take care and have fun!

Yours sincerely,
AJ Goh, Owner of {0.guild.name}.

"""

WELCOME_MESSAGE_NONE = """

# Hi... How did I get here...?

It appears that this bot has joined a server it isn't supposed to, and is DMing new members like you. If you receive this message, please take a screenshot of this and send it to **@ajgoh** (on Discord). Thanks!

Yours sincerely,
AJ Goh (@ajgoh).

"""

GOODBYE_MESSAGE = """

# We're sorry to see you go...

Perhaps you lost interest in {0.guild.name}, or maybe you forgot what it was about...

{0.guild.name} is a Discord server where gamers come together to connect, game, and hang out together, while participating in fortnightly Robux giveaways and fun events for attractive prizes.

If you wish, you can always rejoin here: https://discord.gg/ZZNrbbH33U

Check out my YouTube channel here: https://www.youtube.com/c/ajgoh

You may rejoin anytime you like, or even invite your friends over too! But until then, we wish you all the best and hope to see you again sometime.

Well wishes,
{0.guild.name}.

"""

NINETYNINE_DESC = """

Welcome to ninetynine, a number game designed to challenge your brain...

To start playing, choose a difficulty and select its respective option. You will then be shown a number and 5 buttons: 2 red and 3 blue.

The number shown at the start vary from 0 to the max value of the current difficulty. The red buttons decrease the number by a certain value, while the blue buttons increase it. Each button's values are randomised upon the start of each game, and range from 1 to half the max value. The number shown will also get randomised at the start of each game, ranging from 0 to 1 less than the max value. The max values for each difficulty are shown below:

```Easy Difficulty   →  Max Value 9\nMedium Difficulty →  Max Value 99\nHard Difficulty   →  Max Value 999```

You are to to press the provided buttons to increase or decrease the number shown. When a number drops below 0 or exceeds the max value, the number will loop over (i.e.: number increase from 99 to 0, and vice versa). The buttons' values are hidden at first, and will be revealed when you win.

The objective of this game is to use the buttons to change the number to show exactly the max value, while using the fewest number of moves. Good luck and enjoy!

"""

SERVER_RULES = """

Below are a few rules and guidelines of this server. Please make sure to follow them, in order to keep this server a safe and welcoming community!

1. Maintain a clean server profile.
2. No intentionally impersonating server members.
3. No spamming or flooding text channels.
4. No abusing voice channels.
5. No misusing channels.
6. No toxicity; no bullying or threatening server members.
7. No excessive vulgarities, slurs, racist remarks, or mature content.
8. No raiding, or attempting to raid, in any form.
9. No seeking or sharing of personal information.
10. No participating in other forms of malicious activity.

Upon committing a violation of any of the server rules, you will be punished accordingly, usually through warnings. Note that accumulating warnings will result in the punishments stated below (based on the warnings from the last 120 days):

- 3 warnings: 1 hour mute
- 6 warnings: 1 day mute
- 10 warnings: 7 day mute
- 15 warnings: 3 day ban
- 20 warnings: 7 day ban
- 25 warnings: 15 day ban
- 30 warnings: 30 day ban
- Another 30 days added to the ban duration for every 5 additional warnings.

Feel free to click the button below to view the full list of rules, along with their punishments and other information about them.

"""