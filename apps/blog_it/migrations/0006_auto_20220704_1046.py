# Generated by Django 3.2.10 on 2022-07-04 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_it', '0005_blogmodel_time_update'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upvotemodel',
            name='view_upvote',
        ),
        migrations.AddField(
            model_name='upvotemodel',
            name='value',
            field=models.IntegerField(default=1),
        ),
    ]
