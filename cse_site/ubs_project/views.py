from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Question, Choice


# Create your views here.


# three things that VIEW going to do:
#  load a template,   fill a context,   return an HttpResponse object
#  django.shortcuts.render() acturally done:
'''
def index(request):
    question_list = Question.objects.order_by('-pub_date')[:5]
    # load a template:
    templete = loader.get_template('ubs_project/index.html')
    # fill a context,  give parameter used in templete file:
    context = {
        'latest_question_list': question_list,
    }
    # return an HttpResponse object
    return HttpResponse(templete.render(context, request))
'''

def index(request):
    question_list = Question.objects.order_by('-pub_date')[:5]
    # fill a context:
    context = {
        'latest_question_list': question_list,
    }
    return render(request, 'ubs_project/index.html', context)


def index2(request):
    return HttpResponse("Hello, world. You're at the polls index 22 .")




def detail(request, question_id):

    # if we want to use get(pk=id) function to fetch a data ,we can use get_object_or_404 (if fetch data by .filter()  use get_list_or_404()  )
    '''
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    '''
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'ubs_project/detail.html', {'question': question})



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'ubs_project/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('ubs:results', args=(question.id,)))



def results(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'ubs_project/results.html', {'question': question})