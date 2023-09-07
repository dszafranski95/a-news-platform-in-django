from django import template

register = template.Library()

@register.filter
def short_description(value):
    return value.split('.')[0] + '.'
