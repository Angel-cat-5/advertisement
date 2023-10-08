from django.contrib import admin
from django.db import models
from django.utils.html import format_html

class Advertisement(models.Model):
    title = models.CharField('заголовок', max_length=128)
    description = models.TextField('описание')
    price = models.DecimalField('цена', max_length=10, decimal_places=2, max_digits=20)
    auction = models.BooleanField('торг', help_text='Хотите ли Вы торговаться?')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'advertisements'

    def __str__(self):
        return f'<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})>'