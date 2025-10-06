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
        ),
        default=1  # 默认值，会在save方法中被覆盖
    )

    def save(self, *args, **kwargs):
        # 根据Data字段自动设置星期几
        # weekday()返回0-6，对应星期一到星期日
        # 我们需要将其转换为1-7
        self.week = self.Data.weekday() + 1
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'diary'