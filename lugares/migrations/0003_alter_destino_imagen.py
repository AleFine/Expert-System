# Generated by Django 5.1.2 on 2024-10-26 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lugares', '0002_alter_destino_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destino',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes_lugares/'),
        ),
    ]
