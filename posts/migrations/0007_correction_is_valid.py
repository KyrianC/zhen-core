# Generated by Django 3.2.7 on 2021-09-06 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20210721_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='correction',
            name='is_valid',
            field=models.BooleanField(default=False),
        ),
    ]