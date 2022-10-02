# Generated by Django 3.2.10 on 2022-07-29 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0012_auto_20220729_1033'),
        ('comment', '0006_alter_commentmodel_reply_of'),
        ('blog_it', '0020_bookmarks_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upvotemodel',
            name='blog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog', to='blog_it.blogmodel'),
        ),
        migrations.AlterField(
            model_name='upvotemodel',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_forum', to='comment.commentmodel'),
        ),
        migrations.AlterField(
            model_name='upvotemodel',
            name='forum',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='forum_upvote', to='forum.forummodel'),
        ),
        migrations.AlterField(
            model_name='upvotemodel',
            name='series',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='upvote_series', to='blog_it.seriesmodel'),
        ),
    ]
