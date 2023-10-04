from django.urls import path
from . import views

urlpatterns = [
    path('menu/<str:menu_name>/', views.display_menu, name='display_menu'),
]