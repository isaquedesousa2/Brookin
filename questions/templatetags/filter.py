from django import template

register = template.Library()

@register.filter()
def format_float(value):
    return f'{value:,.1f}'

@register.filter()
def set_star(value):
    if value <= 0:
        return 1

    if value > 0 and value <= 1:
        return 2

