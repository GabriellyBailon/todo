# Generated by Django 4.0.6 on 2023-04-20 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acoes', '0002_alter_acao_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acao',
            name='closed',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='acao',
            name='data',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='acao',
            name='high',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='acao',
            name='low',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='acao',
            name='open',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='acao',
            name='volume',
            field=models.FloatField(),
        ),
    ]