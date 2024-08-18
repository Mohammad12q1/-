# from telegram import Update # type: ignore
# from telegram.ext import Updater, CommandHandler, CallbackContext # type: ignore

# # قائمة القنوات والمجموعات التي يجب الانضمام إليها
# CHANNELS = ["https://t.me/Zzznourman028", "https://t.me/shehabe125"]

# # التحقق من عضوية المستخدم في القنوات والمجموعات
# def check_membership(user_id, bot):
#     for channel in CHANNELS:
#         try:
#             status = bot.get_chat_member(chat_id=channel, user_id=user_id).status
#             if status not in ['member', 'administrator', 'creator']:
#                 return False
#         except:
#             return False
#     return True

# # دالة الرد على الأمر /start
# def start(update: Update, context: CallbackContext):
#     user_id = update.message.from_user.id
#     bot = context.bot

#     if check_membership(user_id, bot):
#         update.message.reply_text("مرحباً! شكراً لانضمامك. يمكنك الآن استخدام البوت.")
#     else:
#         channels = "\n".join([f"{channel}" for channel in CHANNELS])
#         update.message.reply_text(f"يرجى الانضمام إلى القنوات والمجموعات التالية أولاً:\n{channels}")

# # الوظيفة الرئيسية لبدء البوت
# def main():
#     # استبدل YOUR_API_TOKEN برمز API الخاص بك
#     updater = Updater("7372070684:AAEXKtQIp_0q8IoyqDr4hNNL6yfF4kSZuA8", use_context=True)

#     dp = updater.dispatcher

#     # ربط الأمر /start بالدالة start
#     dp.add_handler(CommandHandler("start", start))

#     # بدء الاستماع للأوامر
#     updater.start_polling()

#     # الحفاظ على تشغيل البوت حتى يتم إيقافه
#     updater.idle()

# if __name__ == '_main_':
#     main()

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, ConversationHandler
 -*- coding: utf-8 -*-

# قائمة القنوات
channels = {
    'Channel 1': 'https://t.me/shehabe125',
    'Channel 2': 'https://t.me/channel2_link',
}

# قائمة الملفات (تقوم بتوجيه المستخدم إلى روابط تحميل الملفات بعد الاشتراك)
files = {
    'File 1': 'https://example.com/file1.pdf',
    'File 2': 'https://example.com/file2.pdf',
}

# ثابت لتعريف المراحل في ConversationHandler
CHECK_SUBSCRIPTION = 1

# دالة لبدء البوت
def start(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user

    # عرض قائمة القنوات
    keyboard = [[InlineKeyboardButton(channel, url=link)] for channel, link in channels.items()]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        'مرحبًا! من فضلك انضم إلى القنوات التالية للوصول إلى الملفات:',
        reply_markup=reply_markup
    )

    # رسالة توجيهية للخطوة التالية
    update.message.reply_text(
        'بعد الانضمام، اكتب /check للتأكد من اشتراكك، أو /files للحصول على الملفات.'
    )

    return CHECK_SUBSCRIPTION

# دالة للتحقق من الاشتراك
def check_subscription(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data

    # نفترض أن المستخدم اشترك (يمكن تحسين هذه النقطة باستخدام التحقق الفعلي من الاشتراك)
    user_data['subscribed'] = True

    update.message.reply_text('تم التحقق من اشتراكك! يمكنك الآن الحصول على الملفات باستخدام الأمر /files.')
    return ConversationHandler.END

# دالة لعرض الملفات بعد التأكد من الاشتراك
def send_files(update: Update, context: CallbackContext) -> None:
    user_data = context.user_data

    if user_data.get('subscribed'):
        keyboard = [[InlineKeyboardButton(file_name, url=file_link)] for file_name, file_link in files.items()]
        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text(
            'إليك الملفات المتاحة:',
            reply_markup=reply_markup
        )
    else:
        update.message.reply_text('يجب عليك الاشتراك في القنوات أولاً! استخدم الأمر /start للبدء.')

# دالة لإظهار المساعدة
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "استخدام البوت:\n"
        "/start - لبدء الاشتراك في القنوات.\n"
        "/check - للتحقق من الاشتراك.\n"
        "/files - للحصول على الملفات بعد الاشتراك.\n"
        "/help - لعرض هذه الرسالة."
    )

def main():
    # قم بإضافة توكن البوت الخاص بك هنا
    updater = Updater("7445452011:AAE22bzvwg1rLxRiWXxiMBY9vFkTwnjrQIo", use_context=True)

    dispatcher = updater.dispatcher

    # ربط الأوامر بالدوال
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            CHECK_SUBSCRIPTION: [CommandHandler("check", check_subscription)],
        },
        fallbacks=[CommandHandler("start", start)],
    )

    dispatcher.add_handler(conv_handler)
    dispatcher.add_handler(CommandHandler("files", send_files))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # بدء البوت
    updater.start_polling()
    updater.idle()

if name == 'main':
    main() 