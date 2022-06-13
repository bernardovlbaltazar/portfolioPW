# Generated by Django 4.0.4 on 2022-06-04 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_alter_cadeira_ranking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tecnica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='cadeira',
            name='ranking',
            field=models.IntegerField(choices=[(5, '5 estrelas'), (1, '1 estrela'), (2, '2 estrelas'), (4, '4 estrelas'), (3, '3 estrelas')]),
        ),
    ]