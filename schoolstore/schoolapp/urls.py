from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('computer_science/', views.computer_science_view, name='computer_science'),
    path('commerce/', views.commerce_view, name='commerce'),
    path('humanities/', views.humanities_view, name='humanities'),
    path('art_literature/', views.art_literature_view, name='art_literature'),
    path('economics/', views.economics_view, name='economics'),
    path('new_page/', views.new_page, name='new_page'),

    # path('login/', views.login, name='login'),
    # path('register/', views.register, name='register'),
    # path('new_page/', views.new_page, name='new_page'),
]
