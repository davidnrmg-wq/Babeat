from django.shortcuts import render


RECIPE_CARDS = [
    {
        'name': 'Picolé de kiwi',
        'description': 'Refrescante e natural',
        'image': 'app/images/kiwi-picole.jpg',
    },
    {
        'name': 'Bolinho de banana',
        'description': 'Lanche macio para o bebê',
        'image': 'app/images/snacks.jpg',
    },
    {
        'name': 'Purê de kiwi',
        'description': 'Uma opção simples e nutritiva',
        'image': 'app/images/kiwi-pure.jpg',
    },
    {
        'name': 'Picolé de frutas',
        'description': 'Receita fácil para dias quentes',
        'image': 'app/images/kiwi-picole.jpg',
    },
    {
        'name': 'Biscoitinho caseiro',
        'description': 'Textura ideal para explorar',
        'image': 'app/images/snacks.jpg',
    },
    {
        'name': 'Creme de frutas',
        'description': 'Leve, colorido e saboroso',
        'image': 'app/images/kiwi-pure.jpg',
    },
]


def index(request):
    return render(request, 'app/index.html')


def receitas(request):
    return render(request, 'app/recipe_grid.html', {
        'title': 'Receitas',
        'heading': 'Receitas',
        'active_page': 'receitas',
        'recipes': RECIPE_CARDS,
    })


def favoritos(request):
    return render(request, 'app/recipe_grid.html', {
        'title': 'Favoritos',
        'heading': 'Favoritos',
        'active_page': 'favoritos',
        'recipes': RECIPE_CARDS[:3],
    })


def calendario(request):
    return render(request, 'app/page.html', {
        'title': 'Calendário',
        'heading': 'Calendário alimentar',
        'description': 'Organize a rotina de refeições e acompanhe novas experiências alimentares.',
        'items': ['Planejar refeições da semana', 'Registrar alimentos experimentados', 'Acompanhar a evolução'],
    })


def agenda(request):
    return render(request, 'app/page.html', {
        'title': 'Agenda',
        'heading': 'Sua agenda',
        'description': 'Cadastre consultas, retornos e outros compromissos importantes.',
        'items': ['Adicionar consulta', 'Criar lembrete', 'Ver próximos compromissos'],
    })


def suporte(request):
    return render(request, 'app/page.html', {
        'title': 'Suporte',
        'heading': 'Como podemos ajudar?',
        'description': 'Encontre orientações para usar o BABEAT e cuidar melhor da rotina alimentar.',
        'items': ['Dúvidas frequentes', 'Falar com o suporte', 'Orientações de segurança'],
    })


def entrar(request):
    return render(request, 'app/login.html')
