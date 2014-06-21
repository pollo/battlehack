from rest_framework import serializers

from knowberlin.models import QuestionsPack, Topic

class QuestionsPackSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionsPack
        fields = ('id', 'name')

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id', 'name')
