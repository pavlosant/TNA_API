from django.test import TestCase
from tna_app.views import home_page, get_id
from django.urls import resolve

# Create your tests here.


class HomePageTest(TestCase):
    def test_home_page_returns_index_page(self):
        found = resolve("/")
        self.assertEqual(found.func, get_id)
