# Generated by Django 4.0.4 on 2022-06-11 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_alter_cadeira_ranking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadeira',
            name='ranking',
            field=models.IntegerField(choices=[(2, '2 estrelas'), (4, '4 estrelas'), (3, '3 estrelas'), (5, '5 estrelas'), (1, '1 estrela')]),
        ),
        migrations.AlterField(
            model_name='pontuacaoquizz',
            name='pontuacao',
            field=models.IntegerField(),
        ),
    ]
