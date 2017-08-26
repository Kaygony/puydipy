import peewee

db = peewee.SqliteDatabase('snake.db')


class Snake(peewee.Model):
    name = peewee.CharField()
    length = peewee.CharField()
    is_relative = peewee.BooleanField()

    class Meta:
        database = db  # модель будет использовать базу данных 'snake.db'