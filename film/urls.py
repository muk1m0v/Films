from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create-film/', views.create_product, name='create-film'),
    path('detail/<int:pk>', views.detail_film, name='detail_film'),
    path('delete/<int:pk>', views.delete_film, name='delete_film'),
    path('update/<int:pk>', views.update_film, name='update_film'),
    path('create-genre/', views.create_genre, name='create-genre'),
    path('contacts/', views.contacts, name='contacts'),
    path('feedbacks/', views.feedbacks, name='feedbacks'),
    path('genres/', views.genres, name='genres'),
]