# Generated by Django 4.0.6 on 2023-04-23 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acoes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcaoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=8)),
                ('descricao', models.TextField()),
                ('data', models.DateField(auto_now_add=True)),
                ('open', models.FloatField()),
                ('closed', models.FloatField()),
                ('high', models.FloatField()),
                ('low', models.FloatField()),
                ('volume', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='Acao',
        ),
    ]
