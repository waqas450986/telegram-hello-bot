TOKEN = '7618187747:AAHcyRyYV6B6N4RA64IpS3qwKltz8zVu6NI'

def start(update, context):
    update.message.reply_text('Hello World')

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if _name_ == '_main_':
    main()
