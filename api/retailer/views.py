from rest_framework import generics
from .models import Retailer
from .serializers import RetailerSerializer

class RetailerListCreateView(generics.ListCreateAPIView):
    queryset = Retailer.objects.all()
    serializer_class = RetailerSerializer

class RetailerRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Retailer.objects.all()
    serializer_class = RetailerSerializer
