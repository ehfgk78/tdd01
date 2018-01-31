import time
import re
from django.http import HttpRequest
from django.test import TestCase
from django.template.loader import render_to_string
from django.urls import resolve

from lists.views import home_page



# Create your tests here.


class HomePageTest(TestCase):
    pattern_input_csrf = re.compile(r'<input[^>]*csrfmiddlewaretoken[^>]*>')

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        expected_html = render_to_string('home.html')
        self.assertEqual(
            re.sub(self.pattern_input_csrf, '', response.content.decode()),
            re.sub(self.pattern_input_csrf, '', expected_html)
        )


    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
        # self.assertTemplateUsed(response, 'wrong.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
