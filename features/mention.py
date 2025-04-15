from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ParseMode

async def mention_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Mention all admins with usernames in a Telegram group.
    """
    try:
        chat = update.effective_chat
        if chat.type not in ["group", "supergroup"]:
            await update.message.reply_text("This command only works in group chats.")
            return

        # Get the list of chat administrators
        admins = await context.bot.get_chat_administrators(chat.id)

        # Extract usernames
        mention_list = [f"@{admin.user.username}" for admin in admins if admin.user.username]

        if not mention_list:
            await update.message.reply_text("No admins with usernames found to mention 😅")
            return

        mention_string = " ".join(mention_list)
        await update.message.reply_text(
            f"Hey besties, roll call! 🫡\n{mention_string}",
            parse_mode=ParseMode.MARKDOWN,
        )

    except Exception as e:
        print("Mention Error:", e)
        await update.message.reply_text(f"Oops! Something went wrong: {e}")
