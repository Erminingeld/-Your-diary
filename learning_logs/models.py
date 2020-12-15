from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """Тема, которую изучает пользователь"""
    text = models.CharField(max_length=200) # атрибут charfield используется для хранения небольшого объёма текста
    date_added = models.DateTimeField(auto_now_add=True) # Блок данных для хранения даты и времени
    owner = models.ForeignKey(User, on_delete=models.CASCADE) # Блок связывает пользователя и созданые им темы

    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.text

class Entry(models.Model):
    """Информация, изученная пользователем по теме"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta: # хранит доп информацию по управлению моделью
        verbose_name_plural = 'entries' # Использует форму множественного числа Entries при обращении более чем к одной записи

        def __str__(self):
            if text >= 50:
                return f"{self.text[:50]}..." # выводит только первые 50 символов
            else:
                return self.text



