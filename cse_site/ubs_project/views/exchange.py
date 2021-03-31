from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic,View
from django.utils import timezone

from ..models.exchange import Exchange
from django.contrib.auth.models import User


# story 5 : A student can CRUD exchanges
class IndexView(generic.ListView):
    '''
    show a list of exchange imformation
    '''
    # template_name = 'ubs_project/exchange_list.html' # default : <app name>/<model name>_list.html
    # context_object_name = 'exchange_list'  # default : <model name>_list, the context used in templete

    def get_queryset(self):
        search_query = self.request.GET.get('exchange_search', '')
        """Return the filtered Exchange list."""
        if search_query:
            return Exchange.objects.filter(title__icontains=search_query).order_by('-created_at')[:10]
        else:
            return Exchange.objects.order_by('-created_at')[:10]


class DetailView(generic.DetailView):
    model = Exchange
    # template_name = '' # default : <app name>/<model name>_detail.html



def exchange_update(request, pk):
    exchange = get_object_or_404(Exchange, pk=pk)
    context_object_name = {
        'exchange': exchange
    }
    return render(request, 'ubs_project/exchange_update.html', context_object_name)

def exchange_update_handler(request, pk):
    exchange = get_object_or_404(Exchange, pk=pk)
    try:
        title = request.POST.get('title')
        description = request.POST.get('description')
        exchange.title = title
        exchange.description = description
    except Exception as e:
        return HttpResponse('exchange_update_handler some thing wrong, Exception : %s' % e)
    else:
        exchange.save()
        return redirect(reverse('exchange_detail', args=(exchange.id,)) )   # function reverse() will generate it into  /ubs_project/exchange_detail/<int:pk>/





def exchange_create(request):
    return render(request, 'ubs_project/exchange_create.html')

def exchange_create_handler(request):
    student = get_object_or_404(User, pk=request.user.id)  # default student 1  ,because we dont have registraion
    try:
        exchange = Exchange(title=request.POST['title'],
                      description=request.POST['description'],
                      created_at=timezone.now(),
                      created_by=student)
    except Exception as e:
        return HttpResponse('exchange_create_handler some thing wrong, Exception : %s' % e)
    else:
        exchange.save()
        return HttpResponseRedirect(reverse('exchange_list'))




def exchange_delete(request, pk):
    exchange = get_object_or_404(Exchange, pk=pk)
    try:
        exchange.delete()
    except Exception as e:
        return HttpResponse('exchange_delete some thing wrong, Exception : %s' % e)
    else:
        return HttpResponseRedirect(reverse('exchange_list'))

