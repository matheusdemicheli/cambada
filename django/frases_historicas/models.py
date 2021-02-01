#-*- coding: utf-8 -*-
import datetime
from random import randint
from django.db import models


class FraseHistoricaManager(models.Manager):
    """
    Manager para o Model FraseHistorica.
    """

    def get_frase_aleatoria(self, queryset=None):
        """
        :param QuerySet queryset:
            Caso informado, usa o queryset passado para buscar uma frase
            aleatória.

        Retorna uma Frase Histórica aleatória.
        """
        queryset = queryset or self.get_queryset()
        indice = randint(0, queryset.count())
        return queryset.all()[indice]

    def get_frase_do_dia(self):
        """
        Retorna a frase do dia.
        """
        hoje = datetime.date.today()
        queryset = self.get_queryset()

        try:
            # Busca a frase do dia de hoje, se existir.
            frase = queryset.get(data_exibicao=hoje)

        except FraseHistorica.DoesNotExist:
            # Caso não exista, busca todas as frases que ainda não tenham sido
            # escolhidas para a frase do dia.
            frases = queryset.filter(data_exibicao__isnull=True)

            if not frases:
                # Caso todas as frases tenham sido escolhidas ao menos uma vez,
                # atualiza o campo da data de exibição para None.
                queryset.all().update(data_exibicao=None)
                frases = queryset.filter(data_exibicao__isnull=True)

            frase = self.get_frase_aleatoria(queryset=frases)
            frase.data_exibicao = hoje
            frase.save()

        return frase


class FraseHistorica(models.Model):
    """
    Model para as Frases Historicas.
    """
    objects = FraseHistoricaManager()

    autor = models.TextField()
    data = models.TextField()
    texto = models.TextField()
    data_exibicao = models.DateField(null=True, blank=True)
