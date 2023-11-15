from django.http import HttpResponse
from . models import Question
from django.shortcuts import render, get_object_or_404
from django.http import Http404

def first(request):
    return HttpResponse('This statement here '
                        'is coming from the app')

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'myapp/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'myapp/detail.html', {'question':question})

def results(request, question_id):
    response = "You are looking at results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)
