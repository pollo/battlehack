import os, random, string

from django.db.models import Q

from rest_framework import status, viewsets

from knowberlin.models import QuestionsPack, Topic, Challenge
from django.contrib.auth.models import User

from knowberlin.serializers import QuestionsPackSerializer, TopicSerializer, \
    ChallengeSerializer, UserSerializer

class QuestionsPackViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Endpoint for questionspack.
    """
    queryset = QuestionsPack.objects.all()
    serializer_class = QuestionsPackSerializer

class TopicViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Endpoint for topics.
    """
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

def _generate_random_password():
    length = 13
    chars = string.ascii_letters + string.digits + '!@#$%^&*()'
    random.seed = (os.urandom(16))
    return ''.join(random.choice(chars) for i in range(length))

class UserViewSet(viewsets.ModelViewSet):
    """
    Endpoint for users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = ()

    def create(self, request, *args, **kwargs):
        response = super(UserViewSet, self).create(request, args, kwargs)
        if response.status_code==status.HTTP_201_CREATED:
            user = self.object
            password = _generate_random_password()
            user.set_password(password)
            user.save()
            response.data = {'password': password}
            return response
        return response

class ChallengeViewSet(viewsets.ModelViewSet):
    """
    Endpoint for challenges.
    """
    serializer_class = ChallengeSerializer

    def get_queryset(self):
        user = self.request.user
        return Challenge.objects.filter(Q(user1=user) |
                                        Q(user2=user))

    def pre_save(self, obj):
        obj.user1 = self.request.user
        obj.user1_current_round = 1
        obj.user2_current_round = 1
