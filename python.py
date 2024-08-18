from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# قائمة القنوات والمجموعات التي يجب الانضمام إليها
CHANNELS = ["https://t.me/Zzznourman028", "https://t.me/shehabe125"]

# التحقق من عضوية المستخدم في القنوات والمجموعات
def check_membership(user_id, bot):
    for channel in CHANNELS:
        try:
            status = bot.get_chat_member(chat_id=channel, user_id=user_id).status
            if status not in ['member', 'administrator', 'creator']:
                return False
        except:
            return False
    return True

# دالة الرد على الأمر /start
def start(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    bot = context.bot

    if check_membership(user_id, bot):
        update.message.reply_text("مرحباً! شكراً لانضمامك. يمكنك الآن استخدام البوت.")
    else:
        channels = "\n".join([f"{channel}" for channel in CHANNELS])
        update.message.reply_text(f"يرجى الانضمام إلى القنوات والمجموعات التالية أولاً:\n{channels}")

# الوظيفة الرئيسية لبدء البوت
def main():
    # استبدل YOUR_API_TOKEN برمز API الخاص بك
    updater = Updater("7350253287:AAGQryNfeRJwK5yW-X4a5Nx44dFSGGIUI_U", use_context=True)

    dp = updater.dispatcher

    # ربط الأمر /start بالدالة start
    dp.add_handler(CommandHandler("start", start))

    # بدء الاستماع للأوامر
    updater.start_polling()

    # الحفاظ على تشغيل البوت حتى يتم إيقافه
    updater.idle()

if _name_ == '_main_':
    main()