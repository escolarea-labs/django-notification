from django import template
register = template.Library()
from notification.models import Notice

@register.filter
def unread_notifications(user, context):
    from django.contrib.contenttypes.models import ContentType
    if context:
        return Notice.objects.unseen_count_for(user, context=context)
    else:
        return Notice.objects.unseen_count_for(user)