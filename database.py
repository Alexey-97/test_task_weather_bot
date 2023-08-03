import sqlite3 as sq


db = sq.connect("weather_bot.db")
cur = db.cursor()


async def db_start():
    cur.execute(
        """CREATE TABLE IF NOT EXISTS weather_log(
        user _id INTEGER,
        name_city TEXT,
        air_temperature INTEGER,
        wind_direction TEXT,
        precipitations TEXT)"""
    )
    db.commit()


async def add_weather_db(data_request):
    cur.execute("INSERT INTO weather_log VALUES(?, ?, ?, ?, ?);", data_request)
    db.commit()
