from django.conf.urls import patterns, url

urlpatterns = patterns('knowberlin.views',
    url(r'^users/$', 'handle_users'),
    url(r'^login/$', 'mylogin'),
    url(r'^logout/$', 'mylogout'),

    url(r'^questionspacks/$', 'questionspack_list'),
    url(r'^topics/(?P<pack_id>[0-9]+)/$', 'topic_list'),

    url(r'^challenges/$', 'handle_challenges')
)
