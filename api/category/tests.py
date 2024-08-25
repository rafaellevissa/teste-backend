from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Category
from .serializers import CategorySerializer
from django.core.management import call_command

class CategoryTests(APITestCase):
    def setUp(self):
        call_command('flush', verbosity=0, interactive=False)

        self.list_create_url = reverse("category-list-create")
        self.valid_payload = {
            "name": "New Category",
            "description": "Description of the new category",
        }
        self.invalid_payload = {
            "name": "",
            "description": "Description with empty name",
        }

    def test_create_category(self):
        response = self.client.post(
            self.list_create_url, data=self.valid_payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.get().name, "New Category")

    def test_create_category_invalid(self):
        response = self.client.post(
            self.list_create_url, data=self.invalid_payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Category.objects.count(), 0)

    def test_get_categories(self):
        self.client.post(self.list_create_url, data=self.valid_payload, format="json")
        response = self.client.get(self.list_create_url)
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_category(self):
        response = self.client.post(
            self.list_create_url, data=self.valid_payload, format="json"
        )
        category_id = response.data["id"]
        update_url = reverse("category-retrieve-update", kwargs={"pk": category_id})
        valid_payload = {"name": "Updated Name", "description": "Updated Description"}
        response = self.client.put(update_url, data=valid_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Updated Name")
