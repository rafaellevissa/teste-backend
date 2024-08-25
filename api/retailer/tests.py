from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Retailer
from .serializers import RetailerSerializer
from django.core.management import call_command


class RetailerTests(APITestCase):
    def setUp(self):
        call_command("flush", verbosity=0, interactive=False)

        self.list_create_url = reverse("retailer-list-create")
        self.valid_payload = {
            "name": "New Retailer",
        }
        self.invalid_payload = {
            "name": "",
        }

    def test_create_retailer(self):
        response = self.client.post(
            self.list_create_url, data=self.valid_payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Retailer.objects.count(), 1)
        self.assertEqual(Retailer.objects.get().name, "New Retailer")

    def test_create_retailer_invalid(self):
        response = self.client.post(
            self.list_create_url, data=self.invalid_payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Retailer.objects.count(), 0)

    def test_get_retailers(self):
        self.client.post(self.list_create_url, data=self.valid_payload, format="json")
        response = self.client.get(self.list_create_url)
        retailers = Retailer.objects.all()
        serializer = RetailerSerializer(retailers, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_retailer(self):
        response = self.client.post(
            self.list_create_url, data=self.valid_payload, format="json"
        )
        retailer_id = response.data["id"]
        update_url = reverse("retailer-retrieve-update", kwargs={"pk": retailer_id})
        valid_payload = {"name": "Updated Name"}
        response = self.client.put(update_url, data=valid_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Updated Name")
