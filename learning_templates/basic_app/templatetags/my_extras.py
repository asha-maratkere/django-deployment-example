{% load my_templates %}
from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """ cutsout all arg from string """
    return value.replace(arg,'')


#register.filter('cut',cut)
