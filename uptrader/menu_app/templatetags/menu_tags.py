from django import template
from django.utils.safestring import mark_safe
from menu_app.models import MenuItem


register = template.Library()

@register.simple_tag()
def draw_menu(menu_name):
    try:
        menu = MenuItem.objects.get(title=menu_name)
        return mark_safe(render_menu(menu))
    except MenuItem.DoesNotExist:
        return ""


def render_menu(menu):
    html = f'<ul>'
    
    for item in menu.children.all():
        html += f'<li><a href="/menu_app/menu{item.url}">{item.title}</a>{render_menu(item)}</li>'
    html += '</ul>'
    
    return html
