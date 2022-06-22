from django.db import models

class Author(models.Model):
    name = models.CharField('Имя', max_length=250)
    surname = models.CharField('Фамилия', max_length=250)

    def __str__(self):
        return '%s, %s' % (self.name, Book.objects.filter(author=self).count())

class Book(models.Model):
    name = models.CharField('Название', max_length=250, default="")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField('Дата издания', blank=True, null=True)
    number_of_pages = models.IntegerField('Количество страниц', blank=True, null=True)

    def __str__(self):
        return self.name

