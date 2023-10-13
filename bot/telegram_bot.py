import asyncio, requests

from aiogram import Bot, Dispatcher, types

TOKEN = '6605311117:AAFtrgzh1EscxSlHk6-dAj13rGxPG3NHNt0'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
chat_ids = ['350127605', '5058200126']
last_processed_date = ''
last_processed_date_course = ''


@dp.message_handler(commands=['start'])
async def get_orders(message: types.Message):
    url = 'http://127.0.0.1:8000/bot/'
    response = requests.get(url)

    if response.status_code == 200:
        message_text = 'Привет Валерия, я твой бот помощник и буду отправлять тебе записи клиентов =)'

        await message.reply(message_text)
    else:
        print(f'Ошибка: {response.status_code}')
        print(response.text)


async def check_for_new_records():
    global last_processed_date  # Объявляем переменную как глобальную

    while True:
        url = 'http://127.0.0.1:8000/bot/'

        response = requests.get(url)

        if response.status_code == 200:
            new_records = response.json()

            if new_records:
                response_data = new_records[-1]

                # Получение даты создания записи
                create_date = response_data['create_date']

                # Проверяем, есть ли новая запись по дате
                if create_date > last_processed_date:
                    # Получение списка выбранных услуг и их суммы
                    selected_services = []
                    total_price = 0

                    for key, value in response_data.items():
                        if key.startswith('manicure_types_service') and isinstance(value, list):
                            for service in value:
                                selected_services.append(service['name'])
                                total_price += service['price']

                    # Форматирование сообщения
                    message_text = (
                        "Новая запись\n"
                        f"Клиент - {response_data['name']} {response_data['last_name']}\n"
                        f"Номер телефона - {response_data['phone_number']}\n"
                        f"Выбранные услуги - {', '.join(selected_services)}\n"
                        f"Общая сумма - {total_price} руб."
                    )

                    for chat_id in chat_ids:
                        await bot.send_message(chat_id, message_text)

                    # Обновление last_processed_date
                    last_processed_date = create_date
        else:
            print(f'Ошибка: {response.status_code}')
            print(response.text)

        await asyncio.sleep(5)


async def check_for_new_records_courses():
    global last_processed_date_course  # Объявляем переменную как глобальную

    while True:
        url = 'http://127.0.0.1:8000/bot/course'

        response = requests.get(url)

        if response.status_code == 200:
            new_records = response.json()

            if new_records:
                response_data = new_records[-1]

                # Получение даты создания записи
                create_date = response_data['create_date']

                # Проверяем, есть ли новая запись по дате
                if create_date > last_processed_date_course:
                    # Форматирование сообщения
                    message_text = (
                        "Новая запись на КУРС\n"
                        f"Клиент - {response_data['name']} {response_data['last_name']}\n"
                        f"Номер телефона - {response_data['phone_number']}\n"
                        f"Выбранный курс - {response_data['courses']['name']}\n"
                    )

                    for chat_id in chat_ids:
                        await bot.send_message(chat_id, message_text)

                    # Обновление last_processed_date
                    last_processed_date_course = create_date
        else:
            print(f'Ошибка: {response.status_code}')
            print(response.text)

        await asyncio.sleep(5)


if __name__ == "__main__":
    from aiogram import executor

    loop = asyncio.get_event_loop()
    loop.create_task(check_for_new_records())
    loop.create_task(check_for_new_records_courses())

    executor.start_polling(dp, loop=loop)
