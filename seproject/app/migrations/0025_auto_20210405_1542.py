# Generated by Django 3.1.3 on 2021-04-05 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_forum_forumlikes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likes',
            name='forum',
        ),
        migrations.DeleteModel(
            name='Dislikes',
        ),
        migrations.DeleteModel(
            name='Likes',
        ),
    ]
