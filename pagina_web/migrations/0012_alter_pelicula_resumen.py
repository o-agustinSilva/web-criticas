# Generated by Django 4.1.7 on 2023-07-09 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina_web', '0011_alter_director_resumen_bibliografico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='resumen',
            field=models.CharField(max_length=3000),
        ),
    ]
