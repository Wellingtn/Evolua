# Generated by Django 5.1.3 on 2024-11-24 17:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0003_turma_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turma',
            name='nome',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='turma',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='turmas', to='setup.professor'),
        ),
    ]
