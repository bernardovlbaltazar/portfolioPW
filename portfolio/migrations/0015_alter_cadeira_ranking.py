# Generated by Django 4.0.4 on 2022-06-11 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0014_alter_cadeira_ranking_alter_pontuacaoquizz_pontuacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadeira',
            name='ranking',
            field=models.IntegerField(choices=[(5, '5 estrelas'), (2, '2 estrelas'), (1, '1 estrela'), (4, '4 estrelas'), (3, '3 estrelas')]),
        ),
    ]
