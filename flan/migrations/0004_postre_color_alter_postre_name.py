# Generated by Django 5.0.6 on 2024-07-02 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flan', '0003_remove_postre_color_postre_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='postre',
            name='color',
            field=models.CharField(default='color_default', max_length=20),
        ),
        migrations.AlterField(
            model_name='postre',
            name='name',
            field=models.CharField(default='name_default', max_length=60),
        ),
    ]