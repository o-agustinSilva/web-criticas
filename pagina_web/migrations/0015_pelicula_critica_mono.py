# Generated by Django 4.1.7 on 2023-07-28 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina_web', '0014_alter_critica_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='critica_mono',
            field=models.CharField(default='', max_length=3000),
        ),
    ]
