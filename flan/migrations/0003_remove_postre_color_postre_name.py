# Generated by Django 5.0.6 on 2024-07-02 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flan', '0002_postre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postre',
            name='color',
        ),
        migrations.AddField(
            model_name='postre',
            name='name',
            field=models.CharField(default='name', max_length=60),
        ),
    ]
