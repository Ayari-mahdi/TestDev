# Generated by Django 4.0.1 on 2022-01-19 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackEndAPI', '0007_alter_articles_lastmod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='Image',
            field=models.ImageField(upload_to=''),
        ),
    ]