from django.contrib.auth.models import User
from django.db import models
from django.utils.datetime_safe import datetime


class Task(models.Model):
    """Тема, которую изучает пользователь"""
    PRIORITIES = {
        ("Низкий(3)", "Низкий"),
        ("Средний(2)", "Средний"),
        ("Высокий(1)", "Высокий"),
    }
    text = models.CharField(max_length=200)
    priority = models.CharField(max_length=10, choices=PRIORITIES)
    deadline = models.DateField(default=datetime.now)
    isitdone = models.BooleanField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.text[:50]
