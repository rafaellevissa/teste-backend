from django.urls import path
from .views import VendorListCreateView, VendorRetrieveUpdateView

urlpatterns = [
    path('', VendorListCreateView.as_view(), name='vendor-list-create'),
    path('<int:pk>/', VendorRetrieveUpdateView.as_view(), name='vendor-retrieve-update'),
]
