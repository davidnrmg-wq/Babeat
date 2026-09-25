import calendar

from django.contrib import messages
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST


RECIPE_CARDS = [
    {'id': 'kiwi-picole', 'name': 'Picolé de kiwi', 'description': 'Refrescante e natural', 'image': 'app/images/kiwi-picole.jpg'},
    {'id': 'banana-bolinho', 'name': 'Bolinho de banana', 'description': 'Lanche macio para o bebê', 'image': 'app/images/snacks.jpg'},
    {'id': 'kiwi-pure', 'name': 'Purê de kiwi', 'description': 'Uma opção simples e nutritiva', 'image': 'app/images/kiwi-pure.jpg'},
    {'id': 'frutas-picole', 'name': 'Picolé de frutas', 'description': 'Receita fácil para dias quentes', 'image': 'app/images/kiwi-picole.jpg'},
    {'id': 'biscoitinho-caseiro', 'name': 'Biscoitinho caseiro', 'description': 'Textura ideal para explorar', 'image': 'app/images/snacks.jpg'},
    {'id': 'creme-de-frutas', 'name': 'Creme de frutas', 'description': 'Leve, colorido e saboroso', 'image': 'app/images/kiwi-pure.jpg'},
]
FAVORITES_SESSION_KEY = 'babeat_favorite_recipes'


def _favorite_ids(request):
    return set(request.session.get(FAVORITES_SESSION_KEY, []))


def _recipes_with_favorites(request, recipes):
    favorite_ids = _favorite_ids(request)
    return [
        {**recipe, 'is_favorite': recipe['id'] in favorite_ids}
        for recipe in recipes
    ]


def index(request):
    return render(request, 'app/dashboard_home.html', {'active_page': 'inicio'})


def receitas(request):
    return render(request, 'app/recipe_grid.html', {
        'title': 'Receitas', 'heading': 'Receitas', 'active_page': 'receitas',
        'recipes': _recipes_with_favorites(request, RECIPE_CARDS),
    })


def favoritos(request):
    favorite_ids = _favorite_ids(request)
    recipes = [recipe for recipe in RECIPE_CARDS if recipe['id'] in favorite_ids]
    return render(request, 'app/recipe_grid.html', {
        'title': 'Favoritos', 'heading': 'Favoritos', 'active_page': 'favoritos',
        'recipes': _recipes_with_favorites(request, recipes),
        'empty_favorites': not recipes,
    })


@require_POST
def alternar_favorito(request):
    recipe_id = request.POST.get('recipe_id', '')
    recipe = next((item for item in RECIPE_CARDS if item['id'] == recipe_id), None)
    if recipe is None:
        return HttpResponseBadRequest('Receita inválida.')

    favorite_ids = _favorite_ids(request)
    if recipe_id in favorite_ids:
        favorite_ids.remove(recipe_id)
        messages.info(request, f'{recipe["name"]} foi removida dos favoritos.')
    else:
        favorite_ids.add(recipe_id)
        messages.success(request, f'{recipe["name"]} foi adicionada aos favoritos.')

    request.session[FAVORITES_SESSION_KEY] = sorted(favorite_ids)
    request.session.modified = True
    next_url = request.POST.get('next', '')
    if not next_url.startswith('/') or next_url.startswith('//'):
        next_url = '/receitas/'
    return redirect(next_url)


def calendario(request):
    month_calendar = calendar.Calendar(firstweekday=6).monthdayscalendar(2026, 8)
    return render(request, 'app/calendar.html', {
        'active_page': 'calendario',
        'weekdays': ('Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb'),
        'weeks': month_calendar,
    })


def agenda(request):
    return render(request, 'app/agenda.html', {
        'active_page': 'agenda',
        'days': ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'),
        'times': ('07:00', '12:00', '17:00'),
        'rows': range(3),
        'events': (
            {'column': 1, 'row': 1, 'title': 'Refeição', 'description': 'Café da manhã'},
            {'column': 2, 'row': 2, 'title': 'Refeição', 'description': 'Almoço'},
            {'column': 4, 'row': 1, 'title': 'Refeição', 'description': 'Lanche'},
        ),
    })


def suporte(request):
    return render(request, 'app/section_page.html', {
        'title': 'Suporte', 'heading': 'Como podemos ajudar?', 'active_page': 'suporte',
        'description': 'Encontre orientações para usar o BABEAT com mais tranquilidade.',
        'items': [
            {'icon': '❔', 'title': 'Dúvidas frequentes', 'description': 'Respostas para as perguntas mais comuns.'},
            {'icon': '💬', 'title': 'Falar com o suporte', 'description': 'Entre em contato quando precisar de ajuda.'},
            {'icon': '🛡️', 'title': 'Orientações de segurança', 'description': 'Informações para uma introdução alimentar segura.'},
        ],
    })


def entrar(request):
    return render(request, 'app/login.html')
