from rest_framework import generics
from .models import Briefing
from .serializers import BriefingSerializer

class BriefingListCreateView(generics.ListCreateAPIView):
    queryset = Briefing.objects.all()
    serializer_class = BriefingSerializer

class BriefingRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Briefing.objects.all()
    serializer_class = BriefingSerializer
