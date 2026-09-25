from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('receitas/', views.receitas, name='receitas'),
    path('calendario/', views.calendario, name='calendario'),
    path('agenda/', views.agenda, name='agenda'),
    path('favoritos/', views.favoritos, name='favoritos'),
    path('favoritos/alternar/', views.alternar_favorito, name='alternar_favorito'),
    path('suporte/', views.suporte, name='suporte'),
    path('entrar/', views.entrar, name='entrar'),
]
