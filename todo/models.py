
from django.db import models


class Post(models.Model):
    types = (
    ('H', 'Высокий'),
    ('M', 'Средний'),
    ('L', 'Низкий'),
    )

    status = (
        ('W', 'Ожидает выполнения'),
        ('C', 'Выполнена'),
        ('I', 'В процессе выполнения'),
    )
    pub_date = models.DateTimeField(auto_now_add=True)
    fin_date = models.DateTimeField()
    types = models.CharField(max_length=200, choices=types)
    status = models.CharField(max_length=200, choices=status, default='W')
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        
        ordering = ['-pub_date']
        verbose_name = 'Задачи'
        verbose_name = 'Задача'

    def __str__(self):
        return self.get_status_display()