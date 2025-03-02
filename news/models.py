from django.db import models

class Articles(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    title = models.CharField('Название', max_length=50, default='Нет названия')
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата/Время публикации')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
    
    def get_absolute_url(self):
        return f'/news/{self.id}'
    