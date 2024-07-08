# List of messages so far:
# 1. CHANGELOG_LIST
# 2. WELCOME_MESSAGE
# 3. WELCOME_MESSAGE_STAFF
# 4. WELCOME_MESSAGE_NONE
# 5. GOODBYE_MESSAGE
# 6. NINETYNINE_DESC
# 7. SERVER_RULES
# 8. STAFF_APPS_QNS

CHANGELOG_LIST = [
  "Version 2.3.0", # VERSION NUMBER (X.Y.Z)
  "28 June 2024", # DATE (FULL)
  "1700", # TIME (24HR, GMT)
  """

- Rereated a separate file to contain image links
  - Images hosted by ImgBB
  - Added thumbnail to rules command
  - Added image to ninetynine command
  - Added images to message commands
- Reworked how message XP is gained from each message
- Added slash command: message xpdrop
  - (Administrator Only) Summon an XP drop
- Added slash command: message xpcollect
  - Collect an XP drop

"""]

WELCOME_MESSAGE = """

# Welcome to AJ's Paradise!

Hello {0.mention} (Member **#{0.guild.member_count}**), and welcome to **AJ's Paradise**!

AJ's Paradise is a welcoming hub for gamers, music lovers, and all sorts of people looking to connect, unwind, and have a blast together. Engage in lively conversations, dive into epic gaming sessions, make a new friend or two, or simply unwind with the cool community.

To the (Roblox) gamers, there are many perks to enjoy and rewards to earn! Robux giveaways are hosted in the server **every 2 weeks**; join and stand to win at least **400 Robux** from each giveaway! You also stand to earn rewards simply by chatting in the server: **400 Robux** for every 20 message levels (no spamming)!

To learn more about the server, feel free to watch this video: https://www.youtube.com/watch?v=ZVREJBOaSEg

Please view the list of rules in <#940996563789025313>, lest you get unknowingly punished for an accidental offense. If you have any suggestions or reports, you may proceed to <#1169516956811014144> or <#941002010088587295> respectively, or send a direct message to **@ajgoh** (on Discord).

I also have a YouTube channel ([**@AJGoh**](<https://www.youtube.com/@ajgoh>)) where I post weekly Roblox content, as well as another YouTube channel ([**@AJGohMusic**](<https://www.youtube.com/@ajgohmusic>)) where I showcase my music creations. Consider subscribing to them to support me and gain additional perks in the server, as stated in <#972449159867138048>.

With that all said, I hope you will have a good time in the server. Take care and have fun!

Best regards,
AJ Goh, Owner of AJ's Paradise

"""

WELCOME_MESSAGE_STAFF = """

# Welcome to **{0.guild.name}**!

Hello {0.mention} (Member **#{0.guild.member_count}**), and welcome to **{0.guild.name}**!

If you have made it into the server, you have probably joined for the following 2 reasons:
1. You have been successfully hired as a Staff Team member of the AJ's Paradise Discord server.
2. You have been invited here by some random person for no apparent reason.

If you are not a Staff Team member of AJ's Paradise, please kindly leave the Discord server immediately as you are not supposed to be in there.

If you are a Staff Team member of AJ's Paradise, you may begin work whenever you are ready, and you may contact any of the other staff if you need any assistance or guidance.

Besides that, take care and have fun!

Yours sincerely,
AJ Goh, Owner of AJ's Paradise

"""

WELCOME_MESSAGE_NONE = """

# Hi... How did I get here...?

It appears that this bot has joined a server it isn't supposed to, and is DMing new members like you. If you receive this message, please take a screenshot of this and send it to **@ajgoh** (on Discord). Thanks!

Yours sincerely,
AJ Goh (@ajgoh).

"""

GOODBYE_MESSAGE = """

# We're sorry to see you go...

Perhaps you lost interest in AJ's Paradise, or maybe you forgot what it was about...

AJ's Paradise is a Discord server where gamers come together to connect, game, and hang out together, while participating in fortnightly Robux giveaways and fun events for attractive prizes.

If you wish, you can always rejoin here: https://discord.gg/ZZNrbbH33U

Check out my YouTube channel here: https://www.youtube.com/c/ajgoh

You may rejoin anytime you like, or even invite your friends over too! But until then, we wish you all the best and hope to see you again sometime.

Well wishes,
AJ's Paradise

"""

NINETYNINE_DESC = """

Welcome to ninetynine, a number game designed to challenge your brain...

To start playing, choose a difficulty and select its respective option. You will then be shown a number and 5 buttons: 2 red and 3 blue.

The number shown at the start vary from 0 to the max value of the current difficulty. The red buttons decrease the number by a certain value, while the blue buttons increase it. Each button's values are randomised upon the start of each game, and range from 1 to half the max value. The number shown will also get randomised at the start of each game, ranging from 0 to 1 less than the max value. The max values for each difficulty are shown below:

```Easy Difficulty   →  Max Value 9\nMedium Difficulty →  Max Value 99\nHard Difficulty   →  Max Value 999```

You are to press the provided buttons to increase or decrease the number shown. When a number drops below 0 or exceeds the max value, the number will loop over (i.e.: number increase from 99 to 0, and vice versa). The buttons' values are hidden at first, and will be revealed when you win.

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

Feel free to click the button below to view the full list of rules, along with their punishments and other information about them.

"""

#   Modal label limit = 45; Modal placeholder limit = 100

#   0                                                                                                   1
#   0         1         2         3         4         5         6         7         8         9         0
#   01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
#                                                |                                                      |

STAFF_APPS_QNS = {

"mod": [
    "Share a bit about yourself...",
    "Explain a few bot commands or functions.",
    "How do you handle problems in the server?",
    "What would you do first upon getting hired?",
    "Is there anything else you want to share?"
],
"modp": [
    "Describe your strengths and weaknesses, why you want to be staff, how much experience you have...",
    "Bots, commands, features, admin, etc. List down and explain the ones you know, the more the better.",
    "What are some possible issues that may arise in the server, and how would you solve them?",
    "How will you contribute to AJ's Paradise?",
    "Is there something you would like us to know? If not, feel free to leave this field blank."
],

"com": [
    "Share a bit about yourself...",
    "How do you increase server activity?",
    "How do you grow the server?",
    "What would you do first upon getting hired?",
    "Is there anything else you want to share?"
],
"comp": [
    "Describe your strengths and weaknesses, why you want to be staff, how much experience you have...",
    "What are some ways you can engage the server community and keep the server active?",
    "How many people can you attract to the server in a week, and how are you going to achieve that?",
    "How will you contribute to AJ's Paradise?",
    "Is there something you would like us to know? If not, feel free to leave this field blank."
],

"acm": [
    "Share a bit about yourself...",
    "Which clan(s) do you want to manage, and how?",
    "How would you conduct clan tryouts?",
    "What would you do first upon getting hired?",
    "Is there anything else you want to share?"
],
"acmp": [
    "Describe your strengths and weaknesses, why you want to be staff, how much experience you have...",
    "Feel free to choose one of more clans to manage, and describe what you can do in this field.",
    "You may think about how you can test one's skills, abilities, and commitment to the clan.",
    "How will you contribute to AJ's Paradise?",
    "Is there something you would like us to know? If not, feel free to leave this field blank."
],

"sem": [
    "Share a bit about yourself...",
    "What makes an event enjoyable for players?",
    "How do you handle problems during an event?",
    "What would you do first upon getting hired?",
    "Is there anything else you want to share?"
],
"semp": [
    "Describe your strengths and weaknesses, why you want to be staff, how much experience you have...",
    "What are some key elements that make an event enjoyable, and how do you apply them into your events?",
    "What are some possible issues that may arise while hosting an event, and how would you solve them?",
    "How will you contribute to AJ's Paradise?",
    "Is there something you would like us to know? If not, feel free to leave this field blank."
]

}