# Generated by Django 5.0.4 on 2024-05-13 02:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_remove_todolist_done_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='done_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
