from django.conf.urls.defaults import *

from notification.views import notices, mark_all_seen, feed_for_user, \
    json_feed_for_user, single, context_notices, context_feed_for_user, context_json_feed_for_user, notice_settings
#TODO: syndication for contexts http://michaeltrier.com/2007/8/5/digging-into-django-syndication-framework
urlpatterns = patterns('',
    url(r'^$', notices, name="notification_notices"),
    url(r'^settings$', notice_settings, name="notification_notice_settings"),
    url(r'^(\d+)/$', single, name="notification_notice"),
    url(r'^feed/$', feed_for_user, name="notification_feed_for_user"),
    url(r'^feed.json$', json_feed_for_user, name="notification_json_feed_for_user"),
    url(r'^mark_all_seen/$', mark_all_seen, name="notification_mark_all_seen"),
    url(r'^(?P<context>[-\w\d]+)/(?P<object_id>\d+)$', context_notices, name="notification_context_notices"),
    url(r'^(?P<context>[-\w\d]+)/(?P<object_id>\d+)/feed$', context_feed_for_user, name="notification_context_feed_for_user"),
    url(r'^(?P<context>[-\w\d]+)/(?P<object_id>\d+)/feed.json$', context_json_feed_for_user, name="notification_context_json_feed_for_user"),    
)
