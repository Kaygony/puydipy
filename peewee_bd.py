import peewee

db = peewee.SqliteDatabase('score.sqlite')


class Snake(peewee.Model):
    name = peewee.CharField()
    score = peewee.IntegerField()
    head_coords = peewee.IntegerField()
    teil_coords = peewee.IntegerField()
    direction = peewee.IntegerField()

    class Meta:
        database = db
