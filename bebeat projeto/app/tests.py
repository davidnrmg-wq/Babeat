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

        self.assertTemplateUsed(response, 'app/dashboard_home.html')

    def test_index_view_contains_core_content(self):
        """A resposta deve conter os textos principais apresentados ao usuário."""
        response = self.client.get(reverse('index'))

        self.assertContains(response, 'BABEAT')
        self.assertContains(response, 'Uma alimentação saudável')
        self.assertContains(response, 'Atalhos rápidos')

    def test_index_view_loads_static_assets(self):
        """O template deve gerar URLs para o CSS e o JavaScript estáticos."""
        response = self.client.get(reverse('index'))

        self.assertContains(response, '/static/app/css/style.css')
        self.assertContains(response, '/static/app/js/script.js')


class NavigationViewTests(SimpleTestCase):
    """Verifica as páginas acessíveis pelo menu principal."""

    navigation_pages = (
        ('receitas', 'Receitas'),
        ('calendario', 'Calendário'),
        ('agenda', 'Agenda'),
        ('favoritos', 'Favoritos'),
        ('suporte', 'Suporte'),
        ('entrar', 'Entrar'),
    )

    def test_navigation_pages_return_success(self):
        for url_name, expected_title in self.navigation_pages:
            with self.subTest(url_name=url_name):
                response = self.client.get(reverse(url_name))
                self.assertEqual(response.status_code, 200)
                self.assertContains(response, expected_title)

    def test_home_page_contains_named_navigation_links(self):
        response = self.client.get(reverse('index'))

        for url_name, _ in self.navigation_pages:
            with self.subTest(url_name=url_name):
                self.assertContains(response, reverse(url_name))


class DesignedPagesTests(SimpleTestCase):
    """Verifica as telas criadas a partir das referências visuais."""

    def test_login_page_renders_form(self):
        response = self.client.get(reverse('entrar'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/login.html')
        self.assertContains(response, 'BABEAT')
        self.assertContains(response, 'E-mail')
        self.assertContains(response, 'Senha')
        self.assertContains(response, 'ENTRAR')
        self.assertContains(response, reverse('suporte'))

    def test_recipes_page_renders_recipe_cards_and_active_menu(self):
        response = self.client.get(reverse('receitas'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/recipe_grid.html')
        self.assertContains(response, 'Picolé de kiwi')
        self.assertContains(response, 'app/images/kiwi-picole.jpg')
        self.assertContains(response, 'class="active"')

    def test_favorites_page_uses_recipe_grid(self):
        response = self.client.get(reverse('favoritos'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/recipe_grid.html')
        self.assertContains(response, 'Favoritos')
        self.assertContains(response, 'Picolé de kiwi')
        self.assertContains(response, 'app/images/kiwi-picole.jpg')

    def test_agenda_page_renders_weekly_schedule(self):
        response = self.client.get(reverse('agenda'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/agenda.html')
        self.assertContains(response, 'Voltar')
        self.assertContains(response, 'Segunda')
        self.assertContains(response, 'Sexta')
        self.assertContains(response, '07:00')
        self.assertContains(response, 'Refeição')
        self.assertContains(response, 'novo-compromisso')

    def test_agenda_back_button_returns_to_calendar(self):
        response = self.client.get(reverse('agenda'))

        self.assertContains(response, reverse('calendario'))
