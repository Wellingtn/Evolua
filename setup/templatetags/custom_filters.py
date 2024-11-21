from django import template

register = template.Library()

@register.filter
def range(value, arg=0):
    """
    Gera um range de números. Por exemplo:
    {% for i in 1|range:9 %}...
    """
    return range(value, arg)
