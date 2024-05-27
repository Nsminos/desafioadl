# Generated by Django 4.2 on 2024-05-27 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField(default='')),
                ('eliminada', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SubTarea',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField(default='')),
                ('eliminada', models.BooleanField(default=False)),
                ('tarea_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='desafioadl.tarea')),
            ],
        ),
    ]
