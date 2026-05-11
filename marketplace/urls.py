from django.urls import path
from . import views

urlpatterns = [
    path('', views.artwork_list, name='artwork_list'),
    path('art/<int:pk>/', views.artwork_detail, name='artwork_detail'),
    path('create/', views.create_artwork, name='create_artwork'),
    path('my-artworks/', views.my_artworks, name='my_artworks'),
]
