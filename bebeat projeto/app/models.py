from django.db import models
from django.contrib.auth.models import User


class Bebe(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='bebes'
    )
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome


class Alimento(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    idade_recomendada = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Receita(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    idade_recomendada = models.CharField(max_length=50)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    imagem = models.ImageField(
        upload_to='receitas/',
        blank=True,
        null=True
    )

    alimentos = models.ManyToManyField(
        Alimento,
        related_name='receitas',
        blank=True
    )

    def __str__(self):
        return self.nome


class Favorito(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favoritos'
    )

    receita = models.ForeignKey(
        Receita,
        on_delete=models.CASCADE,
        related_name='favoritada_por'
    )

    data_adicionado = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = ('usuario', 'receita')

    def __str__(self):
        return f'{self.usuario.username} - {self.receita.nome}'


class Agenda(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='agendas'
    )

    titulo = models.CharField(max_length=150)
    data = models.DateField()
    horario = models.TimeField(
        blank=True,
        null=True
    )
    descricao = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.titulo} - {self.data}'