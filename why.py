from telegram import Bot
from time import sleep

# Replace 'YOUR_API_TOKEN' with your bot's API token
bot = Bot(token='7588162284:AAH1Dy0A_BQW6Pc6Pa52tOxeo7lIwCt9ILo')

# Define the chat_id of the person to send the message to
chat_id = '6366780616'

# Message with both bold and italic formatting
message = "*हे {user_name} मैं अभी OFFLINE हूँ*\n🎙️ *_और यह संदेश मेरे द्वारा बनाये गये हैं!*_\n*बॉट से आया हुआ है*\n\n*मेरे आने का इंतजार करो👍*\n*PLEASE WAIT.......✅*"

# Function to send message
def send_message():
    bot.send_message(chat_id=chat_id, text=message, parse_mode="Markdown")

# Infinite loop to send messages at a specific interval
while True:
    send_message()
    sleep(10)  # Send message every 10 seconds
