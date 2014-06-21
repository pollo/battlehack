from rest_framework import serializers

from django.contrib.auth.models import User
from knowberlin.models import QuestionsPack, Topic, Challenge


class QuestionsPackSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionsPack
        fields = ('id', 'name')

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id', 'name')

class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ('id', 'user1', 'user2', 'user1_current_round',
                  'user2_current_round')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')
