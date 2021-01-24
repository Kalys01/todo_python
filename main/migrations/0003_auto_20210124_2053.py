# Generated by Django 3.1.3 on 2021-01-24 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210119_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='favorite',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(max_length=10000, verbose_name='Описание'),
        ),
    ]
