from django.db import models

# Create your models here.

class Art(models.Model):
    title = models.CharField('Название', max_length=50, default='')
    anon = models.CharField('Анонс', max_length=250, default='')
    full = models.TextField('Текст')
    date = models.DateTimeField('Дата')
    vdate = models.DateField('vДата')
    vtime = models.TimeField('vВремя')
    vgost = models.IntegerField('vГости')

    def __str__(self):
        return self.title
    #   return f'Новость: {self.title}'

    def get_absolute_url(self):
        return f'/news/{self.id}'


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'