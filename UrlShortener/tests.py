from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from UrlShortener.models import URLS


# Create your tests here.
class UrlShortenerTestCase(TestCase):
    original_url = 'https://gist.github.com/ahmad-amaniai/19d8f7e5c12cc2c4a3164b7c8da7c224'
    short_url = 'https://tinyurl.com/ywqgzlmq'

    def setUp(self):
        # Create a test URL in the database for testing
        URLS.objects.create(
            original_url="https://gist.github.com/ahmad-amaniai/19d8f7e5c12cc2c4a3164b7c8da7c224",
            shorten_url="https://tinyurl.com/ywqgzlmq"
        )

    def test_create_short_url_valid(self):
        """
        Test creating a new shortened URL with a valid original URL.
        """
        response = self.client.post(reverse('shorten_url'), data={"url": self.original_url}, content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"url": self.short_url})
        self.assertEqual(URLS.objects.count(), 1)  # Ensure a new record is added to the database

    def test_create_short_url_existing_url(self):
        """
        Test creating a shortened URL for an existing original URL.
        """
        response = self.client.post(reverse('shorten_url'), data={"url": self.original_url}, content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"url": self.short_url})
        self.assertEqual(URLS.objects.count(), 1)  # Ensure the database remains unchanged


    def test_get_original_url_existing_url(self):
        """
        Test retrieving the original URL for an existing shortened URL.
        """
        response = self.client.get(reverse('original_url', kwargs={'url': 'https://tinyurl.com/ywqgzlmq'}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"url": "https://gist.github.com/ahmad-amaniai/19d8f7e5c12cc2c4a3164b7c8da7c224"})

    def test_get_original_url_non_existing_url(self):
        """
        Test retrieving the original URL for a non-existing shortened URL.
        """
        response = self.client.get(reverse('original_url', kwargs={'url': 'nonexistent'}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"message": "URL Does Not Exist"})
