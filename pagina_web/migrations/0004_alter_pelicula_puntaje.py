# Generated by Django 4.1.7 on 2023-06-02 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina_web', '0003_pelicula_puntaje_alter_critica_usuario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='puntaje',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
