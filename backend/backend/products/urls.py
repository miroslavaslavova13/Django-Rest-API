from django.urls import path

from backend.products.views import ProductDetailAPIView, ProductCreateAPIView

urlpatterns = [
    path('<int:pk>/', ProductDetailAPIView.as_view()),
    path('create/', ProductCreateAPIView.as_view())
]
