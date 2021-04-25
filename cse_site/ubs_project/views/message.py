from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic,View
from django.utils import timezone

from ..models.message import Message
from django.contrib.auth.models import User
from ..models.club import Club


# story 16 : A student can send messages
class SentView(generic.ListView):
    '''
    show a list of sent messages
    '''
    # template_name = 'ubs_project/message_list.html' # default : <app name>/<model name>_list.html
    # context_object_name = 'message_list'  # default : <model name>_list, the context used in templete

    def get_queryset(self):
        search_query = self.request.GET.get('msg_search', '')
        """Return the filtered event list."""
        if search_query:
            return Message.objects.filter(created_by=self.request.user,title__icontains=search_query).order_by('-created_at')[:10]
        else:
            return Message.objects.filter(created_by=self.request.user).order_by('-created_at')[:10]



# story 17 : A student can view messages
class RecvView(generic.ListView):
    '''
    show a list of sent messages
    '''
    # template_name = 'ubs_project/message_list.html' # default : <app name>/<model name>_list.html
    # context_object_name = 'message_list'  # default : <model name>_list, the context used in templete

    def get_queryset(self):
        search_query = self.request.GET.get('msg_search', '')
        """Return the filtered event list."""
        if search_query:
            return Message.objects.filter(student=self.request.user,title__icontains=search_query).order_by('-created_at')[:10]
        else:
            return Message.objects.filter(student=self.request.user).order_by('-created_at')[:10]


class DetailView(generic.DetailView):
    model = Message


def msg_create(request):
    rec_list = User.objects.order_by('username')[:10]
    context_object_name = {
        "rec_single": True,
        "rec_list": rec_list
    }
    return render(request, 'ubs_project/message_create.html', context_object_name)


def msg_group(request):
    rec_list = Club.objects.order_by('title')[:10]
    context_object_name = {
        "rec_single": False,
        "rec_list": rec_list
    }
    return render(request, 'ubs_project/message_create.html', context_object_name)


def msg_create_handler(request):
    sender = get_object_or_404(User, pk=request.user.id)  # default student 1  ,because we dont have registraion
    recipient = get_object_or_404(User, pk=request.POST['recipient'])

    try:
        msg = Message(title=request.POST['title'],
                      content=request.POST['content'],
                      created_at=timezone.now(),
                      created_by=sender)
    except Exception as e:
        return HttpResponse('msg_create_handler some thing wrong, Exception : %s' % e)
    else:
        msg.save()
        msg.student.add(recipient)
        return HttpResponseRedirect(reverse('msg_sent'))


def msg_group_handler(request):
    sender = get_object_or_404(User, pk=request.user.id)  # default student 1  ,because we dont have registraion
    club_rec = get_object_or_404(Club, pk=request.POST['recipient'])

    try:
        msg = Message(title=request.POST['title'],
                      content=request.POST['content'],
                      created_at=timezone.now(),
                      created_by=sender)
    except Exception as e:
        return HttpResponse('msg_group_handler some thing wrong, Exception : %s' % e)
    else:
        msg.save()
        for recipient in club_rec.student.all():
            msg.student.add(recipient)
        return HttpResponseRedirect(reverse('msg_sent'))


def msg_delete(request, pk):
    msg = get_object_or_404(Message, pk=pk)
    try:
        msg.delete()
    except Exception as e:
        return HttpResponse('msg_delete some thing wrong, Exception : %s' % e)
    else:
        return HttpResponseRedirect(reverse('msg_home'))

