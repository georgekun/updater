# Create your views here.
from django.shortcuts import render
from .models import MenuItem

def display_menu(request, menu_name):
    try:
        menu = MenuItem.objects.get(title=menu_name)
    except MenuItem.DoesNotExist:
        menu = None
    context = {
        'menu': menu,
        'current_menu_name': menu_name,  # Добавляем имя меню в контекст
    }

    print(context['menu'])
    return render(request, 'menu_app/index.html', context)
