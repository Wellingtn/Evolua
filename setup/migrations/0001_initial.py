# Generated by Django 5.1.3 on 2024-11-21 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sobrenome', models.CharField(max_length=100)),
                ('ra', models.CharField(max_length=20, unique=True)),
                ('curso', models.CharField(max_length=100)),
                ('semestre', models.PositiveIntegerField()),
                ('professor', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('senha', models.CharField(max_length=128)),
            ],
        ),
    ]