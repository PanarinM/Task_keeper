# Generated by Django 2.1.5 on 2019-02-10 13:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='user',
            field=models.ForeignKey(on_delete='CASCADE', related_name='columns', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='user',
            field=models.ForeignKey(on_delete='CASCADE', related_name='tasks', to=settings.AUTH_USER_MODEL),
        ),
    ]