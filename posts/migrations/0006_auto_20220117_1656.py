# Generated by Django 3.2.8 on 2022-01-17 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20220117_1538'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='correction',
            unique_together=set(),
        ),
    ]
