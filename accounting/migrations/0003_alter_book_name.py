# Generated by Django 4.0.5 on 2022-06-15 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0002_book_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(default='', max_length=250, verbose_name='Название'),
        ),
    ]
