from django import template
import re
register = template.Library()

@register.filter
def remove_url(value):
    removed=re.sub('<iframe.*?><\/iframe>','',value)
    removed=re.sub('<img src=.*?>','',removed)



    return removed