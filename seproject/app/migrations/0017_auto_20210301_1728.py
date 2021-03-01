# Generated by Django 3.1.3 on 2021-03-01 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20210301_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='forum',
            name='topic',
            field=models.CharField(max_length=300, unique=True),
        ),
    ]
