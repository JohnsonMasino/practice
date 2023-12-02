from django.http import HttpResponseRedirect, HttpResponse
from . models import Question, Choice
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

def first(content):
    content = 'This statement here is actually coming from the app'
    return HttpResponse(content)

class IndexView(generic.ListView):
    template_name = 'myapp/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]
    
class DetailView(generic.DetailView):
    model = Question
    template_name = 'myapp/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'myapp/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplays the question voting form
        return render(request, 'myapp/detail.html', {
            'question': question,
            'error_message': 'You did not select a choice',
        },)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('myapp:results', args=(question_id,)))
