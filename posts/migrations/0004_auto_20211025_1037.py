# Generated by Django 3.2.8 on 2021-10-25 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20211024_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='correction',
            name='slug',
            field=models.SlugField(max_length=30),
        ),
        migrations.AlterField(
            model_name='correction',
            name='title',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]