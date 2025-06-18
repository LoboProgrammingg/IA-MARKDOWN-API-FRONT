import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='markdown_to_html')
def markdown_to_html(text):
    html = markdown.markdown(text, extensions=['fenced_code', 'tables'])
    return mark_safe(html)

@register.filter
def get_initials(value):
    if not value:
        return ""

    parts = value.replace('.', ' ').replace('-', ' ').split()

    if len(parts) > 1:
        return (parts[0][0] + parts[-1][0]).upper()
    elif len(parts) == 1 and len(parts[0]) > 0:
        return parts[0][0].upper()
    else:
        return ""