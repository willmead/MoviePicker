# Generated by Django 3.1.4 on 2021-01-24 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='name',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='movie',
            name='plot',
            field=models.TextField(max_length=256),
        ),
    ]
