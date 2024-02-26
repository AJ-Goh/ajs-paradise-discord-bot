# ajs-paradise-discord-bot
The GitHub repository for AJ's Paradise Discord Bot, by AJ Goh.

## Bot Information

- Bot Name: AJ's Paradise
- Bot Birth: 15 July 2023 03:00 GMT
- Bot ID: 1129602728050565311
- Bot Token: (Check .env file "TOKEN")


## Other Information

- Application ID: 1129602728050565311

- AJ Goh User ID: 832811319957651457
- AJ's Paradise Server ID: 940996562715291748
- AJ's Paradise Staff Team Server ID: 1123598807985303664

- AJ's Paradise Invite Link: https://discord.gg/ZZNrbbH33U
- AJ Goh YouTube Channel Link: https://www.youtube.com/@ajgoh
- AJ Goh Music YouTube Channel Link: https://www.youtube.com/@ajgohmusic
- AJ Goh Instagram Profile Link: https://instagram.com/aj.goh

- Replit Dashboard Link: https://replit.com/
- UptimeRobot Dashboard Link: https://uptimetobot.com


## Tutorial Links

- Begin with Javascript: https://youtu.be/KZ3tIGHU314
- Begin with Python: https://youtu.be/SPTfmiYiuok
- Hosting on Pylex: https://www.youtube.com/watch?v=jzA_jvE9Rzo
- Hosting Alternatives: https://www.youtube.com/watch?v=MusIvEKjqsc


## Versions

In "Version X.Y.Z":
- X = Big updates, revamps or overhauls
- Y = Regular updates and additions
- Z = Minor updates and bug fixes

## Change Log

VERSION 0.0.0 (15 JULY 2023 1630 GMT)

- Created the AJ's Paradise#7500 Bot
- Added text trigger: @1129602728050565311
  - Tests whether the bot is online

VERSION 0.1.0 (16 JULY 2023 1530 GMT)

- Added different DM-on-join messages for each of the following:
  - AJ's Paradise
  - AJ's Paradise Staff Team
  - None of the above
- Added DM-on-leave message (won't be used)
- Added slash command: test
  - Tests whether the bot is online
- Added slash command: ping
  - Tests the latency of the bot in miliseconds

VERSION 0.2.0 (17 JULY 2023 0000 GMT)

- Successfully fixed slash commands (they work now)
- Added command prefix: !aj
- Removed text trigger: @1129602728050565311
- Added text trigger: hello, hi
  - Bot responds with: Hello!
- Added text command: test
  - Tests whether the bot is online
- Added slash command: changelog
  - Shows the updates for the latest version of the bot

VERSION 0.3.0 (17 JULY 2023 0800 GMT)

- Implemented use of cogs in the code
- Added text trigger: goodbye, bye
  - Bot responds with: Goodbye!
- Added slash command: 8ball
  - Generates a random response to a question input

VERSION 0.3.1 (18 JULY 2023 1200 GMT)

- Fixed slash command: 8ball
  - Problem was at: interaction.response.send_Message()
  - This problem cost me my sanity for an entire day; all I had to do was change an uppercase "M" to a lowercase "m" :(

VERSION 0.4.0 (18 JULY 2023 1730 GMT)

- Added text command: afk
  - Sets an AFK status, which will show when @mentioned

VERSION 0.5.0 (19 JULY 2023 1700 GMT)

- Added slash command: rng
  - Generates a random integer between 2 integer inputs

VERSION 0.6.0 (25 JULY 2023 1500 GMT)

- Added slash command: ninetynine
  - Starts the game 'ninetynine' by AJ Goh

VERSION 0.7.0 (14 AUGUST 2023 0300 GMT)

- Added slash command: reqsponsor
  - Sends a request to host a sponsored item in AJ's Paradise
- Added message levelling system
  - Added slash command: setlevel
    - (Administrator Only) Sets a user's message level
  - Added slash command: setxp
    - (Administrator Only) Sets a user's message XP
  - Added slash command: stats
    - Fetches a user's message level and XP
  - Added slash command: leaderboard
    - Fetches a list of the top 10 users with the highest message level
- Implemented use of group cogs in the code
  - Group cog "bot": test, ping, changelog
  - Group cog "fun": rng, 8ball
  - Group cog "message": setlevel, setxp, stats, leaderboard
  - Group cog "mm" is empty for now

VERSION 0.8.0 (16 AUGUST 2023 1400 GMT)

- Added slash command: reqfeature
  - Sends a request to add a feature to the server bot.
- Added Mini-Matches' advanced score calculation system
  - Added slash command: mm stats
    - Fetches a user's mini-matches' statistics
  - Added slash command: mm leaderboard
    - Fetches a list of the top 5 users with the highest personal scores, as well as a list of all the teams and their combined scores
  - Added slash command: mm setteam
    - Sets a user's team
  - Added slash command: mm addpoints
    - (Administrator Only) Adds points to a user's score
  - Added slash command: mm syncpoints
    - (Administrator Only) Synchronises the team scores with the personal scores
  - Added slash command: mm grandreset
    - (Administrator Only) Resets all users' and teams' scores

VERSION 0.9.0 (23 AUGUST 2023 1200 GMT)

- Added slash command: rules
  - Sends an embed with the first 10 rules of AJ's Paradise, along with a button linked to the full list of rules
- Added slash command: fun rps
  - Starts a game of Rock-Paper-Scissors with the bot
- Added slash command: fun roast
  - Generates a random roast for you or your (non-existent) friends
- Added slash command: message addclaim
  - Logs a prize claim for a user (10 message levels = prize)
- Added "Nine nines" difficulty for ninetynine
  - Max value (Goal) for this difficulty is 999999999

VERSION 1.0.0 (31 AUGUST 2023 1400 GMT)

- Officially released AJ's Paradise server bot to the AJ's Paradise Discord server

VERSION 1.1.0 (3 SEPTEMBER 2023 1415 GMT)

- Added text trigger: hello, hi, sup
  - Bot responds with: Hello!
- Added text trigger: goodbye, bye, cya
  - Bot responds with: Goodbye!
- Added text trigger: subscribe
  - Bot responds with an embed about subscriber perks
- Added text trigger: boost
  - Bot responds with an embed about booster rewards
- Added text trigger: giveaway
  - Bot responds with an embed about fortnightly giveaways
- Added text trigger: message
  - Bot responds with an embed about message rewards
- Added text trigger: sponsor
  - Bot responds with an embed about sponsor requests
- Added slash command: fun rizz
  - Generates a random pickup line
- Added slash command: timestamp
  - Sends the timestamp for a date and time input

VERSION 1.2.0 (27 SEPTEMBER 2023 1630 GMT)

- Added slash command: message setmulti
  - (Administrator Only) Sets the message XP multiplier
- Added logging system via json file for the following commands:
  - mm setteam
  - mm addpoints
  - mm syncpoints
  - mm grandreset

VERSION 1.3.0 (20 NOVEMBER 2023 1330 GMT)

- Fixed text triggers
- Added text trigger react-to-delete feature:
  - React with any emoji to a triggered reply to delete it
  - Only reacts from the user who triggered the reply will be detected
  - Cooldown of 60 seconds after reply is triggered
- Updated on-join welcome message
- Updated rules embed

VERSION 1.4.0 (11 DECEMBER 2023 1415 GMT)

- Added slash command: dm
  - (Administrator Only) DMs a user
- Updated slash command: timestamp
  - Added keywords in "date" field: yesterday, ytd, today, tdy, tomorrow, tmr
  - Added keywords in "time" field: now

VERSION 2.0.0 (6 JANUARY 2024 0900 GMT)

- Successfully migrated from Replit to Pylex for bot hosting
  - Replit no longer offering free hosting from 2024
  - Also transferred code to GitHub just in case
- Created a separate file to contain image links
  - Images hosted by Google Photos
- Added backup system for databases: message, mm
  - Backups occur every 48 hours

VERSION 2.0.1 (26 FEBRUARY 2024 1600 GMT)

- Added slash command: msg
  - (Administrator Only) Sends a message
- Added group cog: request
  - Added slash command: request feature
    - Requests a feature to be added to this bot
  - Added slash command: request drop
    - Requests to host a sudden drop in AJ's Paradise
  - Added slash command: request sponsor
    - Requests to host a sponsored item in AJ's Paradise
- Increased text trigger react-to-delete timeout countdown from 60.0s to 300.0s