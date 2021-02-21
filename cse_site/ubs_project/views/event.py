from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic,View
from django.utils import timezone

from ..models.event import Event, Student


# story 5 : A student can CRUD events
class IndexView(generic.ListView):
    '''
    show a list of event imformation
    '''
    # template_name = 'ubs_project/event_list.html' # default : <app name>/<model name>_list.html
    # context_object_name = 'event_list'  # default : <model name>_list, the context used in templete

    def get_queryset(self):
        """Return the last five published questions."""
        return Event.objects.order_by('-created_at')[:10]


class DetailView(generic.DetailView):
    model = Event
    # template_name = '' # default : <app name>/<model name>_detail.html


class CreateEventView(View):
    def get(self, request):
        # show create form
        return render(request, 'ubs_project/event_create.html')

    def post(self, request):

        student = get_object_or_404(Student, pk=1) # default student 1  ,because we dont have registraion
        try:
            event = Event(title=request.POST['title'],
                          description=request.POST['description'],
                          created_at=timezone.now(),
                          created_by=student)
        except Exception as e:
            print('Exception is : ',e)
            return HttpResponse('some thing wrong')
        else:
            event.save()
            return HttpResponseRedirect(reverse('event_index'))


# class UpdateEventView(View):
#     event = get_object_or_404(Event, pk=pk)
#     def get(self, request):
#         context = {
#
#         }
#         return render(request, 'ubs_project/event_update.html', context)


def delete_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    try:
        event.delete()
    except Exception as e:
        print('Exception is : ', e)
        return HttpResponse('some thing wrong')
    else:
        return HttpResponseRedirect(reverse('event_index'))

