
from django import template
register = template.Library()


@register.filter()
def is_numberic(value):
    return type(value) == int


@register.filter
def index(indexable, i):
    return indexable[i]
