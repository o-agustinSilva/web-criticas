# Generated by Django 4.1.7 on 2023-07-09 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina_web', '0010_alter_actor_resumen_bibliografico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='resumen_bibliografico',
            field=models.CharField(max_length=3000),
        ),
    ]
