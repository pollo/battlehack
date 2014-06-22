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
        read_only_fields = ('user1',
                            'user1_current_round',
                            'user2_current_round')


