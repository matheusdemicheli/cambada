from django.conf import settings
from django.core.management import call_command
from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from frases_historicas.models import FraseHistorica


class DeploymentSettingsTests(SimpleTestCase):
    def test_static_root_and_allowed_hosts_are_configurable(self):
        self.assertTrue(str(settings.STATIC_ROOT).endswith("staticfiles"))
        self.assertIn("localhost", settings.ALLOWED_HOSTS)


class FixtureBootstrapTests(TestCase):
    def test_bootstrap_data_loads_fixture_when_database_is_empty(self):
        FraseHistorica.objects.all().delete()

        call_command("bootstrap_data")

        self.assertGreater(FraseHistorica.objects.count(), 0)


class FrontendTests(TestCase):
    def test_index_page_renders(self):
        response = self.client.get(reverse("frases_historicas:index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Frases Históricas")

    def test_search_matches_author_or_text(self):
        FraseHistorica.objects.create(autor="Matheus", data="Hoje", texto="Uma frase de teste")

        response = self.client.get(reverse("frases_historicas:pesquisar_frases"), {"termo": "matheus"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Uma frase de teste")

    def test_aleatoria_endpoint_without_slash(self):
        FraseHistorica.objects.create(autor="Teste", data="Hoje", texto="Frase test")

        response = self.client.get('/aleatoria')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Frase test")

    def test_aleatoria_returns_404_when_empty(self):
        FraseHistorica.objects.all().delete()

        response = self.client.get('/aleatoria')

        self.assertEqual(response.status_code, 404)
        self.assertJSONEqual(response.content, {'detail': 'Nenhuma frase encontrada.'})

    def test_search_pagination_metadata_is_returned(self):
        FraseHistorica.objects.all().delete()
        for index in range(12):
            FraseHistorica.objects.create(autor=f'Teste {index}', data='Hoje', texto=f'Frase teste {index}')

        response = self.client.get(reverse('frases_historicas:pesquisar_frases'), {'pagina': 2})

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['pagina_atual'], 2)
        self.assertEqual(data['total_paginas'], 2)
        self.assertEqual(data['total_frases'], 12)
        self.assertTrue(data['has_previous'])
        self.assertFalse(data['has_next'])
        self.assertEqual(len(data['frases']), 2)
        self.assertTrue(any(frase['texto'] == 'Frase teste 10' for frase in data['frases']))
        self.assertTrue(any(frase['texto'] == 'Frase teste 11' for frase in data['frases']))
