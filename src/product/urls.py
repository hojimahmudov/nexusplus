from django.urls import path
from . import views

urlpatterns = [
    path('create', views.product_create, name='product_create'),
    path('<int:product_id>/', views.product_details, name='product_detail')
]
