# Generated by Django 3.2.10 on 2022-07-14 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_it', '0014_alter_upvotemodel_forum'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upvotemodel',
            name='forum',
        ),
    ]
