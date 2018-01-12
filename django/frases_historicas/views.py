#-*- coding: utf-8 -*-
from django.http import JsonResponse
from frases_historicas.models import FraseHistorica


def get_frase_aleatoria(request):
    """
    Retorna uma frase aleatória.
    """
    frase = FraseHistorica.objects.get_frase_aleatoria()
    dados = {
        'autor': frase.autor,
        'data': frase.data,
        'texto': frase.texto
    }
    return JsonResponse(dados)


def get_frase_do_dia(request):
    """
    Retorna a frase do dia.
    """
    frase = FraseHistorica.objects.get_frase_do_dia()
    dados = {
        'autor': frase.autor,
        'data': frase.data,
        'texto': frase.texto
    }
    return JsonResponse(dados)


# def filter_pesquisa_frases(request):
#     """
#     Retorna as frases que contém o termo pesquisado.
#     """
#     frases = FraseHistorica.objects.filter(texto__icontains=termo)
