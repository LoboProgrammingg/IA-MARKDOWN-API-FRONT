import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='markdown_to_html')
def markdown_to_html(text):
    if not text:
        return ""
    if not isinstance(text, str):
        text = str(text)
    try:
        html = markdown.markdown(
            text,
            extensions=['fenced_code', 'tables'],
            output_format="html5",
        )
        return mark_safe(html)
    except Exception:
        from django.utils.html import escape
        return mark_safe(escape(text))

@register.filter
def get_initials(value):
    if not value or not isinstance(value, str):
        return ""
    parts = value.replace('.', ' ').replace('-', ' ').split()
    if len(parts) > 1:
        return (parts[0][0] + parts[-1][0]).upper()
    elif len(parts) == 1 and len(parts[0]) > 0:
        return parts[0][0].upper()
    else:
        return ""