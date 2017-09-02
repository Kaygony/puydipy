import peewee

db = peewee.SqliteDatabase('score.sqlite')


class Snake(peewee.Model):
    name = peewee.CharField(unique=True)
    score = peewee.IntegerField(default=0)
    head_coords = peewee.CharField(default=(0, 0))
    body_coords = peewee.CharField(default=[(0, 0), (0, 0)])
    direction = peewee.IntegerField(default=0)

    class Meta:
        database = db
