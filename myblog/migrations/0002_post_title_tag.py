# Generated by Django 3.1.7 on 2021-03-05 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Hello Blog', max_length=255),
        ),
    ]
