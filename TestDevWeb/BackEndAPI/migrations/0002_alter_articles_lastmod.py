# Generated by Django 4.0.1 on 2022-01-19 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackEndAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='LastMod',
            field=models.DateField(default='2022-01-19'),
        ),
    ]
