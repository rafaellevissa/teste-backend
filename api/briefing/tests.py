from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Briefing
from api.category.models import Category
from api.retailer.models import Retailer

from .serializers import BriefingSerializer
from django.core.management import call_command

class BriefingTests(APITestCase):
    def setUp(self):
        call_command('flush', verbosity=0, interactive=False)

        self.list_create_url = reverse("briefing-list-create")
        self.valid_payload = {
            'name': 'New Briefing',
            'retailer': 1,
            'responsible': 'Responsible Person',
            'category': 1,
            'release_date': '2024-01-01',
            'available': 10,
        }
        self.invalid_payload = {
            'name': '',
            'retailer': 1,
            'responsible': 'Responsible Person',
            'category': 1,
            'release_date': '2024-01-01',
            'available': 10,
        }

    def test_create_briefing(self):
        retailer = Retailer.objects.create(name='Retailer Name')
        category = Category.objects.create(name='Category Name')
        self.valid_payload['retailer'] = retailer.id
        self.valid_payload['category'] = category.id
        response = self.client.post(self.list_create_url, data=self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Briefing.objects.count(), 1)
        self.assertEqual(Briefing.objects.get().name, 'New Briefing')

    def test_create_briefing_invalid(self):
        retailer = Retailer.objects.create(name='Retailer Name')
        category = Category.objects.create(name='Category Name')
        self.invalid_payload['retailer'] = retailer.id
        self.invalid_payload['category'] = category.id
        response = self.client.post(self.list_create_url, data=self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Briefing.objects.count(), 0)

    def test_get_briefings(self):
        retailer = Retailer.objects.create(name='Retailer Name')
        category = Category.objects.create(name='Category Name')
        self.valid_payload['retailer'] = retailer.id
        self.valid_payload['category'] = category.id
        self.client.post(self.list_create_url, data=self.valid_payload, format='json')
        response = self.client.get(self.list_create_url)
        briefings = Briefing.objects.all()
        serializer = BriefingSerializer(briefings, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_briefing(self):
        retailer = Retailer.objects.create(name='Retailer Name')
        category = Category.objects.create(name='Category Name')
        response = self.client.post(self.list_create_url, data=self.valid_payload, format='json')
        briefing_id = response.data['id']
        update_url = reverse('briefing-retrieve-update', kwargs={'pk': briefing_id})
        valid_payload = {
            'name': 'Updated Briefing',
            'retailer': retailer.id,
            'responsible': 'Updated Person',
            'category': category.id,
            'release_date': '2024-01-02',
            'available': 20,
        }
        response = self.client.put(update_url, data=valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Briefing')