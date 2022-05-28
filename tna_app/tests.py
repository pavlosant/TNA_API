from django.test import TestCase
from tna_app.views import home_page, get_id
from django.urls import resolve
from .models import Record
import requests

# Create your tests here.


class HomePageTest(TestCase):
    def test_home_page_returns_index_page(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "id.html")


class TNAAPITest(TestCase):
    id = "a147aa58-38c5-45fb-a340-4a348efa01e6"
    url = "http://discovery.nationalarchives.gov.uk/API/records/v1/details/%s" % id

    def test_get_returns_200_for_valid_id(self):
        response = requests.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_get_returns_200_for_valid_id(self):
        id = "MyrandomID"
        url = "http://discovery.nationalarchives.gov.uk/API/records/v1/details/%s" % id
        response = requests.get(url)
        self.assertEqual(response.status_code, 204)


class RecordModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_record = Record()
        first_record.id = "one"
        first_record.title = "The first record"
        first_record.save()

        second_record = Record()
        second_record.id = "two"
        second_record.title = "The second record"
        second_record.save()

        saved_items = Record.objects.all()
        self.assertEqual(saved_items.count(), 2)
