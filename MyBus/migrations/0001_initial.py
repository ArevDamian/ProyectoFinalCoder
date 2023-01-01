# Generated by Django 4.1.3 on 2022-12-29 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colectivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linea_colectivo', models.CharField(max_length=40)),
                ('numero_colectivo', models.IntegerField()),
                ('ramal_colectivo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Recorrido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linea_colectivo', models.CharField(max_length=40)),
                ('inicio', models.CharField(max_length=50)),
                ('destino', models.CharField(max_length=50)),
                ('minutos_viaje', models.IntegerField()),
                ('ramal_colectivo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tarifa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linea_colectivo', models.CharField(max_length=40)),
                ('valor_pasaje', models.IntegerField()),
                ('ramal_colectivo', models.IntegerField()),
            ],
        ),
    ]