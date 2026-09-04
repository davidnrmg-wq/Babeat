from django.test import SimpleTestCase
from django.urls import resolve, reverse

from .views import index


class IndexViewTests(SimpleTestCase):
    """Testes automatizados da página inicial do Babeat."""

    def test_index_url_uses_expected_name(self):
        """A URL nomeada index deve apontar para a raiz do site."""
        self.assertEqual(reverse('index'), '/')

    def test_index_url_resolves_to_index_view(self):
        """A rota raiz deve resolver para a view index do aplicativo."""
        self.assertEqual(resolve('/').func, index)

    def test_index_view_returns_success(self):
        """A página inicial deve responder com HTTP 200."""
        response = self.client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)

    def test_index_view_uses_expected_template(self):
        """A view deve renderizar o template principal do aplicativo."""
        response = self.client.get(reverse('index'))

        self.assertTemplateUsed(response, 'app/index.html')

    def test_index_view_contains_core_content(self):
        """A resposta deve conter os textos principais apresentados ao usuário."""
        response = self.client.get(reverse('index'))

        self.assertContains(response, 'BABEAT')
        self.assertContains(response, 'Uma alimentação saudável')
        self.assertContains(response, 'O que você encontra no BABEAT?')

    def test_index_view_loads_static_assets(self):
        """O template deve gerar URLs para o CSS e o JavaScript estáticos."""
        response = self.client.get(reverse('index'))

        self.assertContains(response, '/static/app/css/style.css')
        self.assertContains(response, '/static/app/js/script.js')
