from django import template
register = template.Library()
from notification.models import Notice

@register.filter
def unread_notifications(user, context_path, context_id):
    if context_path and context_id is not None:     
        splt = context_path.split('.')   
        return Notice.objects.unseen_count_for(user, context__content_type__app_label=splt[0],
                                                context__content_type__model=splt[1])
        
    else:
        return Notice.objects.unseen_count_for(user)