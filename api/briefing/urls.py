from django.urls import path
from .views import BriefingListCreateView, BriefingRetrieveUpdateView

urlpatterns = [
    path('', BriefingListCreateView.as_view(), name='briefing-list-create'),
    path('<int:pk>/', BriefingRetrieveUpdateView.as_view(), name='briefing-retrieve-update'),
]
