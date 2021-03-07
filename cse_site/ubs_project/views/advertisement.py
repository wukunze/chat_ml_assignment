from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic,View
from django.utils import timezone

from ..models.advertisement import Advertisement
from django.contrib.auth.models import User


# story 5 : A student can CRUD advertisements
class IndexView(generic.ListView):
    '''
    show a list of advertisement imformation
    '''
    # template_name = 'ubs_project/advertisement_list.html' # default : <app name>/<model name>_list.html
    # context_object_name = 'advertisement_list'  # default : <model name>_list, the context used in templete

    def get_queryset(self):
        """Return the last five published questions."""
        return Advertisement.objects.order_by('-created_at')[:10]


class DetailView(generic.DetailView):
    model = Advertisement
    # template_name = '' # default : <app name>/<model name>_detail.html



def advertisement_update(request, pk):
    advertisement = get_object_or_404(Advertisement, pk=pk)
    context_object_name = {
        'advertisement': advertisement
    }
    return render(request, 'ubs_project/advertisement_update.html', context_object_name)

def advertisement_update_handler(request, pk):
    advertisement = get_object_or_404(Advertisement, pk=pk)
    try:
        title = request.POST.get('title')
        description = request.POST.get('description')
        advertisement.title = title
        advertisement.description = description
    except Exception as e:
        return HttpResponse('advertisement_update_handler some thing wrong, Exception : %s' % e)
    else:
        advertisement.save()
        return redirect(reverse('advertisement_detail', args=(advertisement.id,)) )   # function reverse() will generate it into  /ubs_project/advertisement_detail/<int:pk>/





def advertisement_create(request):
    return render(request, 'ubs_project/advertisement_create.html')

def advertisement_create_handler(request):
    student = get_object_or_404(User, pk=request.user.id)  # default student 1  ,because we dont have registraion
    try:
        advertisement = Advertisement(title=request.POST['title'],
                      description=request.POST['description'],
                      created_at=timezone.now(),
                      created_by=student)
    except Exception as e:
        return HttpResponse('advertisement_create_handler some thing wrong, Exception : %s' % e)
    else:
        advertisement.save()
        return HttpResponseRedirect(reverse('advertisement_list'))




def advertisement_delete(request, pk):
    advertisement = get_object_or_404(Advertisement, pk=pk)
    try:
        advertisement.delete()
    except Exception as e:
        return HttpResponse('advertisement_delete some thing wrong, Exception : %s' % e)
    else:
        return HttpResponseRedirect(reverse('advertisement_list'))

