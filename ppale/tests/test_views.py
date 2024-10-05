
# ppale/tests/test_views.py

import unittest
from unittest.mock import patch
from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import CustomUser
from ppale.forms import aliments
from ppale.models import UserSelection
import openai
import django
from django.contrib.auth import get_user_model
django.setup()
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'abstract_ideas.settings')  # Remplacez 'nom_de_votre_projet' par le nom de votre projet

import os
import django

# Définir la variable d'environnement pour les paramètres Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'abstract_ideas.settings')
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






#     from django.test import TestCase, Client
# from django.urls import reverse
# from unittest.mock import patch
# import openai

# class AlimentsViewTestCase(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.user = self.client.force_login(user=self._create_test_user())

#     def _create_test_user(self):
#         from django.contrib.auth.models import User
#         return User.objects.create_user(username='testuser', password='testpassword')

#     @patch('openai.ChatCompletion.create')
#     def test_recipe_generation(self, mock_openai):
#         mock_openai.return_value = {
#             "choices": [
#                 {
#                     "message": {
#                         "role": "assistant",
#                         "content": "Recette : \n1. Faites bouillir les pâtes. \n2. Ajoutez les tomates et le basilic..."
#                     }
#                 }
#             ]
#         }

#         data = {
#             'legume': 'Tomate',
#             'viande': 'Poulet',
#             'feculent': 'Pâtes',
#             'poisson': '',
#             'temps_souhaite': 30,
#             'repas_souhaite': 'Déjeuner',
#         }

#         response = self.client.post(reverse('aliments_view'), data)
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'Recette')
#         self.assertIn('1. Faites bouillir les pâtes.', response.content.decode())

#     def tearDown(self):
#         from django.contrib.auth.models import User
#         User.objects.all().delete()
        
        
       ######test en plus non testé

# from django.test import TestCase, Client
# from django.urls import reverse
# from unittest.mock import patch
# from .models import Aliments  # Replace with your actual model import
# from django.contrib.auth.models import User


# class AlimentsViewTests(TestCase):

#     def setUp(self):
#         self.client = Client()
#         # Create a user to simulate a logged-in user
#         self.user = User.objects.create_user(username='testuser', password='testpassword')
#         self.client.login(username='testuser', password='testpassword')  # Log in the user

#     @patch('requests.post')  # Mock the requests.post method
#     def test_aliments_view_success(self, mock_post):
#         # Mock the response from OpenAI API
#         mock_post.return_value.status_code = 200
#         mock_post.return_value.json.return_value = {
#             'choices': [{'text': 'Voici une recette délicieuse!'}]
#         }

#         # Prepare the data to be sent in the POST request
#         data = {
#             'legume': 'Carottes',
#             'viande': 'Poulet',
#             'feculent': 'Riz',
#             'poisson': 'Saumon',
#             'temps_souhaite': 30,
#             'repas_souhaite': 'Dîner',
#         }

#         # Send POST request to the aliments_view
#         response = self.client.post(reverse('aliments_view'), data)

#         # Assert the response status code
#         self.assertEqual(response.status_code, 200)

#         # Assert the response template used
#         self.assertTemplateUsed(response, 'ppale/response.html')

#         # Assert the content of the response
#         self.assertContains(response, 'Voici une recette délicieuse!')

#     @patch('requests.post')  # Mock the requests.post method
#     def test_aliments_view_failure(self, mock_post):
#         # Mock a failed response from the OpenAI API
#         mock_post.return_value.status_code = 500  # Simulate an error from the API

#         # Prepare the data to be sent in the POST request
#         data = {
#             'legume': 'Carottes',
#             'viande': 'Poulet',
#             'feculent': 'Riz',
#             'poisson': 'Saumon',
#             'temps_souhaite': 30,
#             'repas_souhaite': 'Dîner',
#         }

#         # Send POST request to the aliments_view
#         response = self.client.post(reverse('aliments_view'), data)

#         # Assert the response status code
#         self.assertEqual(response.status_code, 200)

#         # Assert the response template used for errors
#         self.assertTemplateUsed(response, 'ppale/error.html')

#         # Assert the content of the response
        self.assertContains(response, 'Failed to get response from API.')

if __name__ == '__main__':
    unittest.main()