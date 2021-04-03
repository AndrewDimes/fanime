from django.urls import path 
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('next/<int:page>', views.next, name='next'),
    path('previous/<int:page>', views.previous, name ='previous'),
    path('first/', views.first, name ='first'),
    path('last/', views.last, name ='last'),
    path('detail/<int:api_anime_id>', views.detail, name='detail'),
    path('detail/<int:api_anime_id>', views.add_comment, name ='add_comment'), 
    path('profile/', views.profile, name='profile'),
    path('accounts/signup/', views.signup, name='signup'),
]