# Generated by Django 5.1.4 on 2025-01-11 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppConsulta', '0002_alter_consulta_fecha_consulta_alter_consulta_medico_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='medico',
            name='rut',
            field=models.CharField(default='SIN-RUT', max_length=12, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='rut',
            field=models.CharField(default='SIN RUT', max_length=12, unique=True),
            preserve_default=False,
        ),
    ]
