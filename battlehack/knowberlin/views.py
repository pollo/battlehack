import os, random, string

from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from rest_framework.renderers import JSONRenderer
from rest_framework import status

from knowberlin.models import QuestionsPack
from django.contrib.auth.models import User
from knowberlin.serializers import QuestionsPackSerializer, TopicSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

def _generate_random_password():
    length = 13
    chars = string.ascii_letters + string.digits + '!@#$%^&*()'
    random.seed = (os.urandom(16))
    return ''.join(random.choice(chars) for i in range(length))

@csrf_exempt
@require_http_methods(["POST"])
def create_user(request):
    try:
        username = request.POST['username']
    except (KeyError):
        return JSONResponse({'error': 'No username provided'},
                            status=status.HTTP_400_BAD_REQUEST)
    if User.objects.filter(username=username):
        #username already taken
        return JSONResponse({'error': 'Username already used'},
                            status=status.HTTP_400_BAD_REQUEST)
    #generate random password
    password = _generate_random_password()
    user = User.objects.create_user(username=username,
                                    password=password)
    user.save()
    return JSONResponse({'password': password})

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
