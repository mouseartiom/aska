# Generated by Django 2.2.dev20180612192205 on 2018-06-18 19:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question_list', '0021_auto_20180618_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
