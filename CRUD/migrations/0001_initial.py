# Generated by Django 2.2.7 on 2019-11-08 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70)),
                ('tipo', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Encargado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70)),
                ('apellido', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='HorarioCuidado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('fecha_cuidado', models.DateField()),
		        ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRUD.Animal')),
                ('encargado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRUD.Encargado')),
            ],
        ),
    ]
