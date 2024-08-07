# Generated by Django 5.0.7 on 2024-08-02 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoas',
            fields=[
                ('id_pessoa', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField()),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('observacoes', models.TextField(blank=True, null=True)),
                ('nome_mae', models.CharField(blank=True, max_length=100, null=True)),
                ('nome_pai', models.CharField(blank=True, max_length=100, null=True)),
                ('cpf', models.CharField(blank=True, max_length=11, null=True, unique=True)),
            ],
            options={
                'indexes': [models.Index(fields=['nome'], name='api_rest_pe_nome_012d57_idx'), models.Index(fields=['data_nascimento'], name='api_rest_pe_data_na_d4df8e_idx')],
            },
        ),
    ]
