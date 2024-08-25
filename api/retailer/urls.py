from django.urls import path
from .views import RetailerListCreateView, RetailerRetrieveUpdateView

urlpatterns = [
    path('', RetailerListCreateView.as_view(), name='retailer-list-create'),
    path('<int:pk>/', RetailerRetrieveUpdateView.as_view(), name='retailer-retrieve-update'),
]
