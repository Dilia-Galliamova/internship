# Generated by Django 4.1.7 on 2023-02-20 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perevalapi', '0003_alter_images_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to='photo', verbose_name='Фото'),
        ),
    ]
