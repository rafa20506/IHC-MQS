# Generated by Django 4.2.3 on 2023-08-11 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionVentas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producto',
            options={'verbose_name': 'producto', 'verbose_name_plural': 'productos'},
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(default='default.jpg', upload_to='productos/'),
        ),
    ]