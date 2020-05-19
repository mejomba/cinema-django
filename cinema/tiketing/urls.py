from django.urls import path
from . import views

app_name = 'tiketing'
urlpatterns = [
    path('movie/list/', views.movie_list, name='movie_list'),
    path('movie/detail/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path("cinema/list/", views.cinema_list, name='cinema_list'),
    path('cinema/detail/<int:cinema_id>/', views.cinema_detail, name='cinema_detail'),
    path('', views.home, name='home'),
    path('sanse/<int:sanse_id>/', views.sanse_detail, name='sanse_detail'),
]
