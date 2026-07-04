#-*- coding: utf-8 -*-
from django.core.paginator import Paginator, EmptyPage
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from frases_historicas.models import FraseHistorica


def index(request):
    return render(request, "frases_historicas/index.html")


def get_frase_aleatoria(request):
    """
    Retorna uma frase aleatória.
    """
    try:
        frase = FraseHistorica.objects.get_frase_aleatoria()
    except FraseHistorica.DoesNotExist:
        return JsonResponse({'detail': 'Nenhuma frase encontrada.'}, status=404)
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
    termo = (request.GET.get('termo') or '').strip()

    try:
        numero_pagina = int(request.GET.get('pagina') or 1)
    except ValueError:
        numero_pagina = 1

    if termo:
        frases = FraseHistorica.objects.filter(texto__icontains=termo) | FraseHistorica.objects.filter(autor__icontains=termo)
    else:
        frases = FraseHistorica.objects.all()

    paginacao = Paginator(frases.distinct().order_by('id'), 10)

    try:
        pagina = paginacao.page(numero_pagina)
    except (EmptyPage, ValueError):
        pagina = None
        frase_list = []
        pagina_atual = max(1, min(numero_pagina, paginacao.num_pages or 1))
        total_paginas = paginacao.num_pages
        total_frases = paginacao.count
        has_previous = False
        has_next = False
    else:
        frase_list = pagina.object_list
        pagina_atual = pagina.number
        total_paginas = paginacao.num_pages
        total_frases = paginacao.count
        has_previous = pagina.has_previous()
        has_next = pagina.has_next()

    dados = [model_to_dict(frase) for frase in frase_list]
    return JsonResponse({
        'frases': dados,
        'pagina_atual': pagina_atual,
        'total_paginas': total_paginas,
        'total_frases': total_frases,
        'has_previous': has_previous,
        'has_next': has_next,
    })
