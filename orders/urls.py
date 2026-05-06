from django.urls import path
from . import views

urlpatterns = [
    path('buy/<int:pk>/', views.create_order, name='create_order'),
    path('<int:pk>/', views.order_detail, name='order_detail'),
    path('', views.order_list, name='order_list'),
]
