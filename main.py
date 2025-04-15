# main.py
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from octopus_core import TELEGRAM_BOT_TOKEN, BOT_USERNAME, verify_tokens
from features.AI import summarize_text, talk_back
from features.mention import mention_all

# Commands

async def start(update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"Hey {user.first_name} 💖 I'm *Minji*, your adorable assistant powered by Cohere AI and your bestie, Set Yoak Lay🐙✨\nYou can chat with me, get text summaries, or just vibe. Try typing something or use /help to see what I can do for you!"
    )

async def help(update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """Here's what I can do for you right now 🌟:

        /start – Say hi to me! I’m always here 🥺✨  
        /help – Shows this very helpful help message 😎  
        /summarize [text] – I’ll turn long messages into bite-sized summaries 🍰  
        (You can also reply to a message with /summarize!)

    More features coming soon… maybe even spicy ones 👀 Stay tuned 💕
    """)

async def summarize_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.reply_to_message:
        # Case 1: User replied to a message
        original_text = update.message.reply_to_message.text
    else:
        # Case 2: User passed the text directly
        args = context.args
        if not args:
            await update.message.reply_text("Please either reply to a message or add the text like:\n`/summarize your text here`", parse_mode="Markdown")
            return
        original_text = " ".join(args)

    print(original_text)
    await update.message.reply_text("🔍 Summarizing, please wait...")
    summary = await summarize_text(original_text)
    await update.message.reply_text(f"📚 Summary:\n{summary}")




async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    
    print(f'User({update.message.chat.id}) in {message_type}: "{text}"')
    
    if message_type in ["group", "supergroup"]:
        print(text)
        if BOT_USERNAME in text:
            new_text = text.replace(BOT_USERNAME, '').strip()
            response: str = await talk_back(new_text)
        else:
            return
    else:
        if update.message.chat.id in [7817075515, 5610609862]:
            response: str = await talk_back(text)
        else:
            response: str = "Sorry! I only talk to My Octopus in DM."
    
    print('Bot1:', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

# 7817075515
# 5610609862
# === Main app ===
def main():
    verify_tokens()

    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    # Add command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("summarize", summarize_command))
    app.add_handler(CommandHandler("mention", mention_all))


    # Add more handlers like these:
    # app.add_handler(CommandHandler("mention", mention_all))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)
    
    print("🤖 MinjiBot is running... waiting for messages 💌")
    
    app.run_polling(poll_interval=5)

# === Run the bot ===
if __name__ == "__main__":
    main()
