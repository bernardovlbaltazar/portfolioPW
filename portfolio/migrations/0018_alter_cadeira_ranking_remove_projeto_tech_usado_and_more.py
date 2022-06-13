# Generated by Django 4.0.4 on 2022-06-12 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0017_alter_cadeira_ranking_alter_projeto_tech_usado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadeira',
            name='ranking',
            field=models.IntegerField(choices=[(5, '5 estrelas'), (2, '2 estrelas'), (4, '4 estrelas'), (3, '3 estrelas'), (1, '1 estrela')]),
        ),
        migrations.RemoveField(
            model_name='projeto',
            name='tech_usado',
        ),
        migrations.AddField(
            model_name='projeto',
            name='tech_usado',
            field=models.ManyToManyField(related_name='tecnologia', to='portfolio.tecnologia'),
        ),
    ]