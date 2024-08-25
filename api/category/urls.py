from django.urls import path
from .views import CategoryListCreateView, CategoryRetrieveUpdateView

urlpatterns = [
    path('', CategoryListCreateView.as_view(), name='category-list-create'),
    path('<int:pk>/', CategoryRetrieveUpdateView.as_view(), name='category-retrieve-update'),
]
