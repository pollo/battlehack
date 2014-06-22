from rest_framework import serializers

from django.contrib.auth.models import User
from knowberlin.models import QuestionsPack, Topic, Challenge

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic

class QuestionsPackSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True)

    class Meta:
        model = QuestionsPack

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge


