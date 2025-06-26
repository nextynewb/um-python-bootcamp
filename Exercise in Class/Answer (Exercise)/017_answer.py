"""
Make a modular function for Telegram Bot
"""

API_KEY = '7710223759:AAHAsGMf4XbWxVFCaQiZrox_H6rTGgKy0lE' # Remove X

import telebot
import requests

# Initialize the bot
bot = telebot.TeleBot(API_KEY)


def get_latest_news():
    """
    Remove pass, and get the latest news from TheEdge API
    Return the news id concatenate with the base url (https://theedgemalaysia.com/node/) + nid
    """
    THE_EDGE_API = 'https://theedgemalaysia.com/api/loadMoreCategories?offset=0&categories=malaysia'
    latest_news = requests.get(THE_EDGE_API).json()
    latest_news_id  = latest_news['results'][0]['nid']
    return f"https://theedgemalaysia.com/node/{latest_news_id}"

def get_crypto_price(crypto_symbol):
    """
    Remove pass, and get the latest price of a crypto currency from Luno API
    Return the price of the crypto currency in MYR
    """
    LUNO_API = f'https://api.mybitx.com/api/1/ticker?pair={crypto_symbol}MYR'
    pass


@bot.message_handler(commands=['news'])
def handle_news(message):
    news = get_latest_news()
    bot.reply_to(message, f"The Latest news is: {news}")

@bot.message_handler(commands=['crypto'])
def handle_crypto(message):
    crypto_symbol = message.text.replace('/crypto', '').strip().upper()

    if crypto_symbol == 'BTC':
        result = get_crypto_price('XBT')
    else:
        try:
            result = get_crypto_price(crypto_symbol)
        except Exception as e:
            result = f"Invalid crypto symbol: {crypto_symbol}"
            
    bot.reply_to(message, f"The price of {crypto_symbol} is: {result}")
    
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    help_text = """
🤖 Simple Text Converter Bot!

This demonstrates modular string functions:

📝 *Available Commands:*
- '/news' - Get the latest news
- '/crypto <symbol>' - Get the current price of a crypto currency


Try: `/crypto XRP` 🚀
"""
    bot.reply_to(message, help_text, parse_mode='Markdown')

@bot.message_handler(func=lambda message: True)
def handle_other_messages(message):
    """Handles any other message"""
    bot.reply_to(message, "💡 Use `/help` to see available text conversion commands!")

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("🤖 Simple Telegram Bot")
    print("▶️ Bot is now running...")
    
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"❌ Error: {e}")
        print("🔄 Restarting bot...")
        bot.polling(none_stop=True)
