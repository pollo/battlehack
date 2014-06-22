from django.conf.urls import patterns, url, include

from knowberlin import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'questionspacks', views.QuestionsPackViewSet)
router.register(r'topics', views.TopicViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'challenges', views.ChallengeViewSet, base_name='challenge')

urlpatterns = patterns('knowberlin.views',
    url(r'^', include(router.urls)),

    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),

)
