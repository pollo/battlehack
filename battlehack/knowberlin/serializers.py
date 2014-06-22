from rest_framework import serializers

from django.contrib.auth.models import User
from knowberlin.models import QuestionsPack, Topic, Challenge, Round

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


class RoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Round

class ChallengeSerializer(serializers.ModelSerializer):
    rounds = RoundSerializer(many=True, read_only=True)

    class Meta:
        model = Challenge
        read_only_fields = ('user1',
                            'user1_current_round',
                            'user2_current_round')
