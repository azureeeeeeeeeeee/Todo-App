# Generated by Django 5.0.4 on 2024-05-09 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_todolist_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='done',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
