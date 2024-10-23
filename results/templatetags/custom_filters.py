from django import template

register = template.Library()

@register.filter
def percentage(value, total):
    """Returns the percentage of a value relative to the total."""
    try:
        return (value / total) * 100
    except ZeroDivisionError:
        return 0
