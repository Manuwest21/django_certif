
# ppale/tests/test_views.py

import unittest
from unittest.mock import patch
from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User
from ppale.forms import aliments
from ppale.models import UserSelection
import openai
import django
from django.contrib.auth import get_user_model
django.setup()

import os
import django

# Définir la variable d'environnement pour les paramètres Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()




User = get_user_model()




class AlimentsViewTests(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.url = reverse('aliments_view')
        self.client.login(username='testuser', password='12345')

    def test_get_aliments_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ppale/aliments.html')
        self.assertIsInstance(response.context['form'], aliments)

    @patch('openai.ChatCompletion.create')
    def test_post_valid_aliments_view(self, mock_create):
        mock_response = {'choices': [{'message': {'content': 'Test recipe response'}}]}
        mock_create.return_value = mock_response
        
        data = {
            'legume': 'carrot',
            'viande': 'chicken',
            'feculent': 'rice',
            'poisson': 'salmon',
            'temps_souhaite': '30',
            'repas_souhaite': 'dinner',
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ppale/response.html')
        self.assertIn('Test recipe response', response.context['response'])

    def test_post_invalid_aliments_view(self):
        data = {}  # Empty data, which should be invalid
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ppale/aliments.html')
        self.assertFalse(response.context['form'].is_valid())

    def assertTemplateUsed(self, response, template_name):
        """ Helper function to check the template used in a response """
        self.assertIn(template_name, [t.name for t in response.templates])

if __name__ == '__main__':
    unittest.main()