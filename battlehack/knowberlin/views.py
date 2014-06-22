import os, random, string

from settings import ROUNDS_NUMBER, QUESTIONS_NUMBER

from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

from django.db.models import Q


from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status

from rest_framework import viewsets

from knowberlin.models import QuestionsPack, Topic, Challenge, Round, Question,\
    RoundQuestion
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

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

def my_login_required(original_view):
    def new_view(request, *args, **kwargs):
        if request.user.is_authenticated():
            return original_view(request, *args, **kwargs)
        return JSONResponse({'error': 'Login required'},
                            status=status.HTTP_403_FORBIDDEN)
    return new_view

def select_questions(topic, number):
    #NOT EFFICIENT IMPLEMENTATION, TO BE IMPROVED
    questions = list(Question.objects.filter(topic=topic))
    random.shuffle(questions)
    return questions[0:number]

def create_round(challenge, topic, number, questions):
    #create round
    round = Round(
        challenge=challenge,
        topic=topic,
        number=number,
        user1_current_question=1,
        user2_current_question=1
    )
    round.save()
    #assign questions to round
    for i,question in enumerate(questions):
        round_question = RoundQuestion(round=round,
                                       question=question,
                                       number=i+1)
        round_question.save()

@csrf_exempt
@my_login_required
@require_http_methods(["GET","POST"])
def handle_challenges(request):
    """
    List all challenges of the logged in user, or create new challenge
    """
    if request.method == 'GET':
        challenges = Challenge.objects.filter(user1=request.user)
        serializer = ChallengeSerializer(challenges, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = request.POST
        data['user1'] = request.user.id
        data['user1_current_round'] = 1
        data['user2_current_round'] = 1
        serializer = ChallengeSerializer(data=data)
        if serializer.is_valid():
            #save challenge
            serializer.user1 = request.user.id
            serializer.save()
            try:
                questionspacks = QuestionsPack.objects.get(
                    id=data['questionspack'])
                topic = Topic.objects.get(id=data['topic'])
            except (KeyError, ValueError,
                    Topic.DoesNotExist, QuestionsPack.DoesNotExist):
                return JSONResponse({'error':
                                     'Provide questionspack and topic'},
                                    status=status.HTTP_400_BAD_REQUEST)
            #create and save rounds for newly created challenge
            questions_set = select_questions(topic,
                                             ROUNDS_NUMBER*QUESTIONS_NUMBER)
            for i in range(ROUNDS_NUMBER):
                create_round(Challenge.objects.get(id=serializer.data['id']),
                             topic,
                             i+1,
                             questions_set[i*QUESTIONS_NUMBER:
                                           (i+1)*QUESTIONS_NUMBER])
            return JSONResponse({},
                                status=status.HTTP_201_CREATED)
        return JSONResponse(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
