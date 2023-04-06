from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.db.models import DO_NOTHING

class User(AbstractBaseUser):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    numero_cre = models.CharField(max_length=16, null=True, blank=True)

    USERNAME_FIELD = 'name'

    def __str__(self):
        return self.name


class Barraginha(models.Model):

    user = models.ForeignKey(User, on_delete=DO_NOTHING)
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    logitude = models.FloatField()
    note = models.TextField(null=True, blank=True, max_length=2000)

    pluviosidade_max_anual = models.IntegerField()
    area_microbracia_contribuicao = models.IntegerField()
    maior_cota_microbacia = models.IntegerField()
    menor_cota_microbacia = models.IntegerField()
    comprimento_talvegue_principal = models.IntegerField()


    pluviosidade_max_anual_hora = models.FloatField()
    pluviosidade_max_anual_segundo = models.FloatField()
    area_microbacia_contribuicao_ha = models.FloatField()
    declividade_trecho = models.FloatField()
    volume_concentrado_trecho = models.FloatField()
    vazao_escoamento_bruto = models.FloatField()
    vazao_escoamento = models.FloatField()
    tempo_concentracao= models.FloatField()
    tempo_concentracaoo_final = models.FloatField()
    capacidade_infiltracao_a = models.FloatField()
    capacidade_infiltracao_b = models.FloatField()
    velocidadede_infiltracao = models.FloatField()
    quantidade_infiltrar_final = models.FloatField()
    area_total_infiltracao = models.FloatField()
    area_fundo_consider = models.FloatField()

    def set_pluviosidade_max_anual_hora(self):
        self.pluviosidade_max_anual_hora = self.pluviosidade_max_anual

    def set_pluviosidade_max_anual_segundo(self):
        self.pluviosidade_max_anual_segundo = self.pluviosidade_max_anual_hora / 3600

    def set_area_microbacia_contribuicao_ha(self):
        self.area_microbacia_contribuicao_ha = self.area_microbracia_contribuicao / 10000

    def set_declividade_trecho(self):
        self.declividade_trecho = self.maior_cota_microbacia - self.menor_cota_microbacia

    def set_volume_concentrado_trecho(self):
        self.volume_concentrado_trecho = self.pluviosidade_max_anual_hora * self.area_microbracia_contribuicao

    def set_vazao_escoamento_bruto(self):
        self.vazao_escoamento_bruto = self.volume_concentrado_trecho / 3600

    def set_vazao_escoamento(self):
        self.vazao_escoamento = (0.12 * self.pluviosidade_max_anual_hora * self.area_microbracia_contribuicao) / 360

    def set_tempo_concentracao(self):
        self.tempo_concentracao = (0.87 *((self.comprimento_talvegue_principal*self.comprimento_talvegue_principal*self.comprimento_talvegue_principal) / self.declividade_trecho))

    def set_tempo_concentracaoo_final(self):
        self.tempo_concentracaoo_final = self.tempo_concentracao**0.385

    def set_capacidade_infiltracao_a(self):
        self.capacidade_infiltracao_a = 1 + (1-1)

    def set_capacidade_infiltracao_b(self):
        self.capacidade_infiltracao_b= 2.7183 ** -0.04 * self.tempo_concentracaoo_final

    def set_velocidadede_infiltracao(self):
        self.velocidadede_infiltracao = self.capacidade_infiltracao_a *self.capacidade_infiltracao_b

    def set_quantidade_infiltrar_final (self):
        self.quantidade_infiltrar_final = (self.vazao_escoamento_bruto-self.vazao_escoamento) * 3600

    def set_area_total_infiltracao(self):
        self.area_total_infiltracao = self.quantidade_infiltrar_final / self.velocidadede_infiltracao

    def set_area_fundo_consider(self):
        self.area_fundo_consider= self.area_total_infiltracao / 3








