class script(object):

    START_TXT = """𝙷𝙴𝙻𝙾 {},

𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 <a href=https://t.me/{}>{}</a>😌, 𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂 & 𝚆𝙴𝙱 𝚂𝙴𝚁𝙸𝙴𝚂,𝚂𝙾 𝙹𝙾𝙸𝙽 𝙼𝚈 𝙶𝚁𝙾𝚄𝙿 & 𝙴𝙽𝙹𝙾𝚈 𝙰𝙻𝙻 𝙼𝙾𝚅𝙸𝙴𝚂 𝙰𝙽𝙳 𝚆𝙴𝙱 𝚂𝙷𝙾𝚆𝚂.❤️

💥 𝙼𝚢 𝙶𝚛𝚘𝚞𝚙 :- @chat_official_sahil ⚠️

😎 𝙼𝚢 𝙾𝚠𝚗𝚎𝚛 :- @itz_sahil_official 🌟"""

    HELP_TXT = """𝙷𝙴𝚈 {}

𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""

    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}

✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/itz_sahil_official>Sahil Official</a>

✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼

✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹

✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱

✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: 𝙷𝙴𝚁𝙾𝙺𝚄

✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v1.0.1 [ 𝙱𝙴𝚃𝙰 ]"""

    SOURCE_TXT = """<b>NOTE:</b>

- This is not a open source project. 

- Source - @itz_sahil_official  

<b>DEVS:</b>

- <a href=https://t.me/chat_official_sahil>Team Sahil</a>"""

    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>

1. eva maria should have admin privillage.

2. only admins can add filters in a chat.

3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>

• /filter - <code>add a filter in chat</code>

• /filters - <code>list all the filters of a chat</code>

• /del - <code>delete a specific filter in chat</code>

• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""

    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>

1. Telegram will not allows you to send buttons without any content, so content is mandatory.

2. Eva Maria supports buttons with any telegram media type.

3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>

<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>

<code>[Button Text](buttonalert:This is an alert message)</code>"""

    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>

1. Make me the admin of your channel if it's private.

2. make sure that your channel does not contains camrips, porn and fake files.

3. Forward the last message to me with quotes.

 I'll add all the files in that channel to my db."""

    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 

- it helps to avoid spamming in groups.

<b>NOTE:</b>

1. Only admins can add a connection.

2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>

• /connect  - <code>connect a particular chat to your PM</code>

• /disconnect  - <code>disconnect from a chat</code>

• /connections - <code>list all your connections</code>"""

    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>

these are the extra features of Eva Maria

<b>Commands and Usage:</b>

• /id - <code>get id of a specified user.</code>

• /info  - <code>get information about a user.</code>

• /imdb  - <code>get the film information from IMDb source.</code>

• /search  - <code>get the film information frch

 various sources.</code>"""

    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>

This module only works for my admins

<b>Commands and Usage:</b>

• /logs - <code>to get the rescent errors</code>

• /stats - <code>to get status of files in db.</code>

• /delete - <code>to delete a specific file from db.</code>

• /users - <code>to get list of my users and ids.</code>

• /chats - <code>to get list of the my chats and ids </code>

• /leave  - <code>to leave from a chat.</code>

• /disable  -  <code>do disable a chat.</code>

• /ban  - <code>to ban a user.</code>

• /unban  - <code>to unban a user.</code>

• /channel - <code>to get list of total connected channels</code>

• /broadcast - <code>to broadcast a message to all users</code>"""

    STATUS_TXT = """𝙷𝚒𝚒..

𝙸 𝚊𝚖 𝚊 𝚜𝚞𝚙𝚎𝚛 𝙼𝚘𝚟𝚒𝚎 𝙵𝚒𝚕𝚝𝚎𝚛 𝚋𝚘𝚝 𝙱𝚢 [SAHIL OFFICIAL](https://t me/sahil_official_here/13).🍷

Currently Indexing 10 Channels.🔥

So total file are gonna to be 10 times after some days"""
