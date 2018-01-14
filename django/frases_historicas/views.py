#-*- coding: utf-8 -*-
from django.core.paginator import Paginator, EmptyPage
from django.forms.models import model_to_dict
from django.http import JsonResponse
from frases_historicas.models import FraseHistorica


def get_frase_aleatoria(request):
    """
    Retorna uma frase aleatória.
    """
    frase = FraseHistorica.objects.get_frase_aleatoria()
    return JsonResponse(model_to_dict(frase))


def get_frase_do_dia(request):
    """
    Retorna a frase do dia.
    """
    frase = FraseHistorica.objects.get_frase_do_dia()
    return JsonResponse(model_to_dict(frase))


def pesquisar_frases(request):
    """
    Retorna as frases que contém o termo pesquisado.
    """
    termo = request.GET.get('termo')
    numero_pagina = request.GET.get('pagina')

    frases = FraseHistorica.objects.filter(texto__icontains=termo)
    paginacao = Paginator(frases, 10)

    try:
        pagina = paginacao.page(numero_pagina)
    except EmptyPage:
        frases = []
    else:
        frases = pagina.object_list

    dados = [model_to_dict(frase) for frase in frases]
    return JsonResponse({'frases': dados})
