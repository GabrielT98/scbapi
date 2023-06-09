# Generated by Django 4.1.7 on 2023-03-31 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('numero_cre', models.CharField(blank=True, max_length=16, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Barraginha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('latitude', models.FloatField()),
                ('logitude', models.FloatField()),
                ('note', models.TextField(blank=True, max_length=2000, null=True)),
                ('pluviosidade_max_anual', models.IntegerField()),
                ('area_microbracia_contribuicao', models.IntegerField()),
                ('maior_cota_microbacia', models.IntegerField()),
                ('menor_cota_microbacia', models.IntegerField()),
                ('comprimento_talvegue_principal', models.IntegerField()),
                ('pluviosidade_max_anual_hora', models.FloatField()),
                ('pluviosidade_max_anual_segundo', models.FloatField()),
                ('area_microbacia_contribuicao_ha', models.FloatField()),
                ('declividade_trecho', models.FloatField()),
                ('volume_concentrado_trecho', models.FloatField()),
                ('vazao_escoamento_bruto', models.FloatField()),
                ('vazao_escoamento', models.FloatField()),
                ('tempo_concentracao', models.FloatField()),
                ('tempo_concentracaoo_final', models.FloatField()),
                ('capacidade_infiltracao_a', models.FloatField()),
                ('capacidade_infiltracao_b', models.FloatField()),
                ('velocidadede_infiltracao', models.FloatField()),
                ('quantidade_infiltrar_final', models.FloatField()),
                ('area_total_infiltracao', models.FloatField()),
                ('area_fundo_consider', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='scbapi.user')),
            ],
        ),
    ]
