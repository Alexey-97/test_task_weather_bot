# Телеграм бот погоды

# Задание
Задание 1 - небольшой алгоритм (по желанию)
Дан неотсортированный массив целых чисел
Найти минимальное положительное число, которого нет в массиве.
Примеры:
[10, -3, 5, 0, 1, 5, 3, 2] - ответ 4
[0, 3, 2, 1, 4] - ответ 5

Задание 2
Несколько уровней есть
Написать бота
Бот будет говорить погоду в городе, который указал пользователь
.1) У бота есть есть команды
.а) /help - выводит описание других команд (может быть просто какая-нибудь небольшая строка наполнение неважно)
.b) /cities - выводит список доступных городов (3-5 будет достаточно - города на личное усмотрение)
.c) /start - начало работы. Бот отвечает что-то вроде «Введите ваш город». Если пользователь вводит город, которого нет в списке из пункта выше, бот просит ввести другой город. Регистр ввода не имеет значения - например Berlin = berlin = BeRLiN
Дальше уже по уровням сложности
.1) Сделать простой генератор температуры (random наше все), скорости и направления ветра (С, СЗ, З ЮЗ итд), осадков итп - 3-4 параметров будет достаточно - это будет имитация запроса к стороннему сервису.
.2) Так как мы не хотим превышать теоретический лимит запросов к стороннему сервису есть смысл добавить кэш, достаточно будет будет простого словаря. Время жизни кэша 10 минут
.3) Внезапно мы захотели вести журнал погоды. После каждого запроса мы пишем данные о погоде в SQL базу
.4) Сымитировать запрос к стороннему API (или может быть найти бесплатный погодный сервис или с бесплатным триалом) или даже написать небольшое приложение, которое будет обробатывать GET запрос с параметром города и возвращать простой json - на усмотрение.

Этот бот подскажет вам какая погода по названию города
## Файлы 
.1 database.py - база данных хранит данные о погоде связана с weather_bot.py
.2 weather_bot.py - tg_bot генерирует и отдаёт случайные данные о погоде. Лимите в 10 запросов делает паузу 10 мин.
.3 test_task_algorithm.py - прстой алгоритм из задания
.4 weather_bot_4_task.py - tg_bot обращается к сервису `https:\\openweathermap.org/` за данными о погоде и отдаёт их пользователю
## Устоновка
.1 Копируйте репозиторий с github
.2 Создайте venv и установите зависимости из requirements.txt
.3 Получити API погодного сайта по ссылке `https:\\openweathermap.org/` и запешите такен в 
переменную `open_weather_token` в weather_bot_4_task.py
.4 Зарегестрируйте телеграмм бота в телеграмме 
и запишите токен в переменную `TOKEN` в .env

## Запуск бота
.1 Запустите код в своей IDEA
.2 Войдите в чат в телеграмме и введите команду `/start`
.3 Теперь вводите город и получайте данные о погоде
# При работе с weather_bot.py
.1 кнопка/команда /start - начало работы.
.2 кнопка/команда /cities - выводит список доступных городов
.3 кнопка/команда /help - выводит описание других команд