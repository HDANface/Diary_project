from django.db import models
from datetime import datetime

class Diary(models.Model):
    id = models.AutoField(primary_key=True)
    Data = models.DateTimeField(default=datetime.now) #日期
    note = models.TextField(max_length=1500, default='')
    week = models.IntegerField(
        choices = (
            (1, '星期一'),
            (2, '星期二'),
            (3, '星期三'),
            (4, '星期四'),
            (5, '星期五'),
            (6, '星期六'),
            (7, '星期日'),
        )
    )


    class Meta:
        db_table = 'diary'