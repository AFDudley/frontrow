from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from runway import views as rw_views

urlpatterns = patterns('',
    url(r'^$', rw_views.index, name='rw_index'),
    url(r'^login_user', rw_views.login_user, name='login_user'),
    url(r'^add_comment/$', rw_views.add_comment, name='add_comment'),
    url(r'^sample_presentation/(?P<workspace_index>\d+)/(?P<preso_index>\d+)/$', rw_views.sample_preso, name='sample_preso'),
    url(r'^media_item/(?P<workspace_index>\d+)/(?P<mi_index>\d+)/$', rw_views.media_item, name='media_item'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,})
)