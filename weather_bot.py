from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup
from dotenv import load_dotenv
import random
import os
import time
import database as db


load_dotenv()
bot = Bot(os.getenv("TOKEN"))
dp = Dispatcher(bot=bot)


button = ReplyKeyboardMarkup(resize_keyboard=True)
button.add("/help").add("/cities").add("/start")

btn_cities = {"cities": ["Новосибирск", "Москва", "Пенза", "Сургут", "Красноярск"]}
btn_help = {
    "/cities": "Доступные города",
    "/start": "Начало работы в боте",
    "/help": "описание других команд",
}


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer(
        f"{message.from_user.first_name} Bведите доступный город. Доступные города /cities!",
        reply_markup=button,
    )


@dp.message_handler(commands=["help"])
async def cmd_help(message: types.Message):
    await message.answer("\n".join("{} - {}".format(k, v) for k, v in btn_help.items()))


@dp.message_handler(commands=["cities"])
async def cmd_cities(message: types.Message):
    await message.answer("\n".join(i for i in btn_cities.get("cities")))


# Словарь лимита запросов
request_limit = {}


@dp.message_handler()
async def weather(message: types.Message):
    await db.db_start()
    try:
        limit = request_limit[message.from_user.id][1]
        if int(time.time() - limit) // 60 < 10 and limit != -1:
            await message.reply(
                f"Слишком много запросо попробуйте повторить через {10 - (int(time.time() - limit) // 60)}"
            )
            return
    except KeyError:
        pass
    if message.text.lower() in map(str.lower, btn_cities.get("cities")):
        if message.from_user.id in request_limit.keys():
            if request_limit[message.from_user.id][0] < 10:
                request_limit[message.from_user.id][0] = (
                    request_limit[message.from_user.id][0] + 1
                )
            else:
                request_limit[message.from_user.id][1] = time.time()
                request_limit[message.from_user.id][0] = 0
                await message.reply(
                    f"Слишком много запросо попробуйте повторить через {10 - (int(time.time() - request_limit[message.from_user.id][1]) // 60)}"
                )
                return
        else:
            request_limit[message.from_user.id] = [1, -1]
        # создание случайных данных.
        user_id = message.from_user.id
        name_city = message.text
        air_temperature = random.randint(0, 50)
        wind = random.choice("C СЗ З ЮЗ В ЮВ".split())
        precipitations = random.choice("солнечно дождь град ливень облачно".split())
        # добавление погодных данных в бд.
        user_data = (user_id, name_city, air_temperature, wind, precipitations)
        await db.add_weather_db(user_data)
        # ответ пользователю
        await message.reply(
            f"""В {message.text} сейчас:
            Температура воздуха: {air_temperature} °C 
            Ветер: {wind} 
            Осадки: {precipitations}"""
        )

    else:
        await message.answer("Я вас не понимаю /help")


if __name__ == "__main__":
    executor.start_polling(dp)

# weather_token = "1ec034be9236b53611a8abe609f3fb87"
