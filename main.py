from telegram.ext import Updater, CommandHandler
from telegram.ext.dispatcher import run_async
import requests
import re
import settings


def start(update, context):
    update.message.reply_text("Hi!:) If you are feeling down, let me try to help you with some cute doggos!"
                              " Send /dog and let's begin")


def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url


def get_image_url():
    allowed_extension = ['jpg', 'jpeg', 'png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$", url).group(1).lower()
    return url


run_async


def dog(update, context):
    url = get_image_url()
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)


def main():
    updater = Updater(settings.TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler('dog', dog))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

