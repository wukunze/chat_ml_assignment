from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic,View
from django.utils import timezone

from ..models.event import Event
from django.contrib.auth.models import User


# story 5 : A student can CRUD events
class IndexView(generic.ListView):
    '''
    show a list of event imformation
    '''
    # template_name = 'ubs_project/event_list.html' # default : <app name>/<model name>_list.html
    # context_object_name = 'event_list'  # default : <model name>_list, the context used in templete

    def get_queryset(self):
        search_query = self.request.GET.get('event_search', '')
        """Return the filtered event list."""
        if search_query:
            return Event.objects.filter(title__icontains=search_query).order_by('-created_at')[:10]
        else:
            return Event.objects.order_by('-created_at')[:10]


class DetailView(generic.DetailView):
    model = Event
    # template_name = '' # default : <app name>/<model name>_detail.html



def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    context_object_name = {
        'event': event
    }
    return render(request, 'ubs_project/event_update.html', context_object_name)

def event_update_handler(request, pk):
    event = get_object_or_404(Event, pk=pk)
    try:
        title = request.POST.get('title')
        description = request.POST.get('description')
        event.title = title
        event.description = description
    except Exception as e:
        return HttpResponse('event_update_handler some thing wrong, Exception : %s' % e)
    else:
        event.save()
        return redirect(reverse('event_detail', args=(event.id,)) )   # function reverse() will generate it into  /ubs_project/event_detail/<int:pk>/





def event_create(request):
    return render(request, 'ubs_project/event_create.html')

def event_create_handler(request):
    student = get_object_or_404(User, pk=request.user.id)  # default student 1  ,because we dont have registraion
    try:
        event = Event(title=request.POST['title'],
                      description=request.POST['description'],
                      created_at=timezone.now(),
                      created_by=student)
    except Exception as e:
        return HttpResponse('event_create_handler some thing wrong, Exception : %s' % e)
    else:
        event.save()
        return HttpResponseRedirect(reverse('event_list'))




def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    try:
        event.delete()
    except Exception as e:
        return HttpResponse('event_delete some thing wrong, Exception : %s' % e)
    else:
        return HttpResponseRedirect(reverse('event_list'))

