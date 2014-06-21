import os, random, string

from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status

from knowberlin.models import QuestionsPack, Challenge
from django.contrib.auth.models import User
from knowberlin.serializers import QuestionsPackSerializer, TopicSerializer, \
    ChallengeSerializer, UserSerializer

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

def _generate_random_password():
    length = 13
    chars = string.ascii_letters + string.digits + '!@#$%^&*()'
    random.seed = (os.urandom(16))
    return ''.join(random.choice(chars) for i in range(length))

@csrf_exempt
@require_http_methods(["POST", "GET"])
def handle_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        try:
            username = request.POST['username']
        except (KeyError):
            return JSONResponse({'error': 'No username provided'},
                                status=status.HTTP_400_BAD_REQUEST)
        if not username:
            return JSONResponse({'error': 'Username cannot be empty'},
                                status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=username):
            #username already taken
            return JSONResponse({'error': 'Username already used'},
                                status=status.HTTP_400_BAD_REQUEST)
        #generate random password
        password = _generate_random_password()
        #create user
        user = User.objects.create_user(username=username,
                                        password=password)
        user.save()
        return JSONResponse({'password': password})

@csrf_exempt
@require_http_methods(["POST"])
def mylogin(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
    except (KeyError):
        return JSONResponse({'error': 'Provide username and password'},
                            status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return JSONResponse({})
        else:
            return JSONResponse({'error': 'User is not active'},
                                status=status.HTTP_400_BAD_REQUEST)
    else:
        return JSONResponse({'error': 'Invalid username or password'},
                            status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@require_http_methods(["POST"])
def mylogout(request):
    logout(request)
    return JSONResponse({})

@require_http_methods(["GET"])
def questionspack_list(request):
    """
    List all questions packs available
    """
    questionspacks = QuestionsPack.objects.all()
    serializer = QuestionsPackSerializer(questionspacks, many=True)
    return JSONResponse(serializer.data)

@require_http_methods(["GET"])
def topic_list(request, pack_id):
    """
    List all topics available in given questions pack
    """
    try:
        questionspack = QuestionsPack.objects.get(id=pack_id)
    except QuestionsPack.DoesNotExist:
        return JSONResponse({'error': 'Specified question pack does not exist'},
                            status=status.HTTP_404_NOT_FOUND)
    topics = questionspack.topic_set.all()
    serializer = TopicSerializer(topics, many=True)
    return JSONResponse(serializer.data)

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
            serializer.user1 = request.user.id
            serializer.save()
            return JSONResponse(serializer.data,
                                status=status.HTTP_201_CREATED)
        return JSONResponse(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
