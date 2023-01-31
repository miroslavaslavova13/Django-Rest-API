from django.urls import path

from backend.products.views import ProductDetailAPIView

urlpatterns = [
    path('<int:pk>/', ProductDetailAPIView.as_view())
]
