from django.shortcuts import render


def index(request):
    return render(request, 'app/index.html')


def receitas(request):
    return render(request, 'app/page.html', {
        'title': 'Receitas',
        'heading': 'Receitas para cada fase',
        'description': 'Encontre ideias simples e nutritivas para a introdução alimentar do seu bebê.',
        'items': ['Purê de batata-doce', 'Papinha de abóbora', 'Banana amassada'],
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


def favoritos(request):
    return render(request, 'app/page.html', {
        'title': 'Favoritos',
        'heading': 'Receitas favoritas',
        'description': 'Acesse rapidamente as receitas que você salvou.',
        'items': ['Suas receitas salvas aparecerão aqui.'],
    })


def suporte(request):
    return render(request, 'app/page.html', {
        'title': 'Suporte',
        'heading': 'Como podemos ajudar?',
        'description': 'Encontre orientações para usar o BABEAT e cuidar melhor da rotina alimentar.',
        'items': ['Dúvidas frequentes', 'Falar com o suporte', 'Orientações de segurança'],
    })


def entrar(request):
    return render(request, 'app/page.html', {
        'title': 'Entrar',
        'heading': 'Acesse sua conta',
        'description': 'A área de autenticação estará disponível em breve.',
        'items': ['Entrar', 'Criar uma conta', 'Recuperar senha'],
    })
