import calendar

from django.shortcuts import render


RECIPE_CARDS = [
    {'name': 'Picolé de kiwi', 'description': 'Refrescante e natural', 'image': 'app/images/kiwi-picole.jpg'},
    {'name': 'Bolinho de banana', 'description': 'Lanche macio para o bebê', 'image': 'app/images/snacks.jpg'},
    {'name': 'Purê de kiwi', 'description': 'Uma opção simples e nutritiva', 'image': 'app/images/kiwi-pure.jpg'},
    {'name': 'Picolé de frutas', 'description': 'Receita fácil para dias quentes', 'image': 'app/images/kiwi-picole.jpg'},
    {'name': 'Biscoitinho caseiro', 'description': 'Textura ideal para explorar', 'image': 'app/images/snacks.jpg'},
    {'name': 'Creme de frutas', 'description': 'Leve, colorido e saboroso', 'image': 'app/images/kiwi-pure.jpg'},
]


def index(request):
    return render(request, 'app/dashboard_home.html', {'active_page': 'inicio'})


def receitas(request):
    return render(request, 'app/recipe_grid.html', {
        'title': 'Receitas', 'heading': 'Receitas', 'active_page': 'receitas', 'recipes': RECIPE_CARDS,
    })


def favoritos(request):
    return render(request, 'app/recipe_grid.html', {
        'title': 'Favoritos', 'heading': 'Favoritos', 'active_page': 'favoritos', 'recipes': RECIPE_CARDS[:3],
    })


def calendario(request):
    month_calendar = calendar.Calendar(firstweekday=6).monthdayscalendar(2026, 8)
    return render(request, 'app/calendar.html', {
        'active_page': 'calendario',
        'weekdays': ('Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb'),
        'weeks': month_calendar,
    })


def agenda(request):
    return render(request, 'app/section_page.html', {
        'title': 'Agenda', 'heading': 'Sua agenda', 'active_page': 'agenda',
        'description': 'Cadastre consultas, retornos e outros compromissos importantes.',
        'items': [
            {'icon': '🩺', 'title': 'Adicionar consulta', 'description': 'Registre consultas com pediatras e nutricionistas.'},
            {'icon': '🔔', 'title': 'Criar lembrete', 'description': 'Não deixe passar nenhum compromisso importante.'},
            {'icon': '📌', 'title': 'Próximos compromissos', 'description': 'Veja sua agenda de forma rápida e organizada.'},
        ],
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
