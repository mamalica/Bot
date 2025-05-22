from telegram import Update, InlineKeyboardButton, Inli>
from telegram.ext import ApplicationBuilder, CommandHan>

BOT_TOKEN = '7732703686:AAEZuFqjwJAqMZ7i3zy0_RaNyXhgocW>

ADMIN_ID = 303268652  # آی‌دی عددی خودت

CHANNEL_USERNAME = "sexulogyi"  # فقط نام کاربری بدون @

video_db = {}

async def start(update: Update, context: ContextTypes.D>
    if update.effective_user.id == ADMIN_ID:
        await update.message.reply_text("سلام عشقم، وید>
    else:
        await update.message.reply_text("سلام! منتظر لی>

async def handle_video(update: Update, context: Context>
    if update.effective_user.id != ADMIN_ID:
        return

    video = update.message.video or update.message.docu>
    if not video:
        return

    file_id = video.file_id
    message = await update.message.reply_text(
        "لینک فیلم ساخته شد!",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("دریافت فیلم", callb>
        )
    )
    video_db[file_id] = file_id

async def handle_button(update: Update, context: Contex>
    query = update.callback_query
    await query.answer()
    user = query.from_user

    chat_member = await context.bot.get_chat_member(cha>
    if chat_member.status not in ['member', 'administra>
        await query.message.reply_text("اول باید عضو کا>
        return

    file_id = query.data
    await query.message.reply_video(
        video=file_id,
        caption="به دلیل فیلترینگ شدید، ویدیو بعد از ۳۰>
    )
    await context.bot.delete_message(chat_id=query.mess>

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.VIDEO | filters.>
app.add_handler(CallbackQueryHandler(handle_button))

app.run_polling()
