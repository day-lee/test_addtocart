# Generated by Django 3.1.5 on 2021-03-13 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='curriculum',
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='thumbnail',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='video',
            field=models.CharField(max_length=500, null=True),
        ),
    ]