# Generated by Django 3.2.10 on 2022-07-15 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentmodel',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='commentmodel',
            name='body',
            field=models.TextField(default='2020-2-2'),
            preserve_default=False,
        ),
    ]
