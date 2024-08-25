from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Vendor
from .serializers import VendorSerializer
from django.core.management import call_command


class VendorTests(APITestCase):
    def setUp(self):
        call_command("flush", verbosity=0, interactive=False)

        self.list_create_url = reverse("vendor-list-create")
        self.valid_payload = {
            "name": "New Vendor",
        }
        self.invalid_payload = {
            "name": "",
        }

    def test_create_vendor(self):
        response = self.client.post(
            self.list_create_url, data=self.valid_payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vendor.objects.count(), 1)
        self.assertEqual(Vendor.objects.get().name, "New Vendor")

    def test_create_vendor_invalid(self):
        response = self.client.post(
            self.list_create_url, data=self.invalid_payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Vendor.objects.count(), 0)

    def test_get_vendors(self):
        self.client.post(self.list_create_url, data=self.valid_payload, format="json")
        response = self.client.get(self.list_create_url)
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_vendor(self):
        response = self.client.post(
            self.list_create_url, data=self.valid_payload, format="json"
        )
        vendor_id = response.data["id"]
        update_url = reverse("vendor-retrieve-update", kwargs={"pk": vendor_id})
        valid_payload = {"name": "Updated Vendor"}
        response = self.client.put(update_url, data=valid_payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Updated Vendor")
