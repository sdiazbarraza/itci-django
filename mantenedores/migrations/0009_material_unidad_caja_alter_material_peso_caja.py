# Generated by Django 4.2.17 on 2025-02-10 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mantenedores', '0008_material'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='unidad_caja',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='material',
            name='peso_caja',
            field=models.IntegerField(default=0),
        ),
    ]
