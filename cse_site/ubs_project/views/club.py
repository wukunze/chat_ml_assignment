from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic, View
from django.utils import timezone

from ..models.advertisement import Advertisement
from ..models.club import Club
from django.contrib.auth.models import User
from django.db import connection


# story 8

# club page
def club_list(request):
    student = get_object_or_404(User, pk=request.user.id)
    user_id = request.user.id
    context_object_name = {
        "club_list": [],
        "uid": request.user.id
    }
    cursor = connection.cursor()
    select_sql = "select * from ubs_project_club_student where user_id = {0}".format(user_id)
    cursor.execute(select_sql)
    raw = cursor.fetchall()
    if len(raw) >= 1:
        for content in raw:
            cid = content[1]
            uid = content[2]
            clubs = Club.objects.filter(id=cid)
            context_object_name['club_list'].append(clubs[0])
    print(context_object_name)
    return render(request, 'ubs_project/club_list.html', context_object_name)


# club create
def club_create(request):
    context_object_name = {
    }
    return render(request, 'ubs_project/club_create.html', context_object_name)


def club_create_handler(request):
    student = get_object_or_404(User, pk=request.user.id)
    oldClub = Club.objects.filter(title=request.POST['title'])
    if oldClub.count() != 0:
        return render(request, 'ubs_project/club_create.html', {"SameTitle": True})
    try:
        club = Club(title=request.POST['title'],
                    description=request.POST['description'],
                    created_at=timezone.now(),
                    created_by=student)
    except Exception as e:
        return HttpResponse('club_create_handler some thing wrong, Exception : %s' % e)
    else:
        club.save()
        cursor = connection.cursor()
        insert_sql = "insert into ubs_project_club_student(club_id, user_id) values({0}, {1})".format(club.id,
                                                                                                      request.user.id)
        cursor.execute(insert_sql)
        return HttpResponseRedirect(reverse('club_list'))


# club search
def club_search(request):
    clubSets = {}

    search_content = request.POST.get('search_content')
    if search_content is None or search_content == '':
        clubSets = Club.objects.order_by('-created_at')[:10]
    else:
        clubSets = Club.objects.filter(title__startswith=search_content)

    context_object_name = {
        "clubList": clubSets
    }

    return render(request, 'ubs_project/club_search.html', context_object_name)


def club_search_handler_by_name(request):
    context_object_name = {
    }
    return render(request, 'ubs_project/club_search.html', context_object_name)


# club join
def club_join_handler(request, pk):
    # join
    context_object_name = {}
    cursor = connection.cursor()
    select_sql = "select * from ubs_project_club_student where club_id= {0} and user_id = {1}".format(pk,
                                                                                                      request.user.id)
    cursor.execute(select_sql)
    raw = cursor.fetchall()
    if len(raw) >= 1:
        search_content = request.POST.get('search_content')
        if search_content is None or search_content == '':
            clubSets = Club.objects.order_by('-created_at')[:10]
        else:
            clubSets = Club.objects.filter(title__startswith=search_content)

        context_object_name = {
            "clubList": clubSets,
            "Joined": True,
            "NewJoin": False
        }
        return render(request, 'ubs_project/club_search.html', context_object_name)

    # insert
    insert_sql = "insert into ubs_project_club_student(club_id, user_id) values({0}, {1})".format(pk,
                                                                                                  request.user.id)
    cursor.execute(insert_sql)

    search_content = request.POST.get('search_content')
    if search_content is None or search_content == '':
        clubSets = Club.objects.order_by('-created_at')[:10]
    else:
        clubSets = Club.objects.filter(title__startswith=search_content)

    context_object_name = {
        "clubList": clubSets,
        "Joined": False,
        "NewJoin": True
    }

    return render(request, 'ubs_project/club_search.html', context_object_name)


# club update
def club_update(request, pk):
    context_object_name = {}
    clubs = Club.objects.filter(id=pk)
    if clubs.count() > 0:
        context_object_name = {
            "club": clubs[0]
        }
    return render(request, 'ubs_project/club_update.html', context_object_name)


def club_update_handler(request):
    context_object_name = {}
    pk = request.POST.get('fakeid')
    clubs = Club.objects.filter(id=pk)
    if clubs.count() > 0:
        club = clubs[0]
        club.description = request.POST.get('description')
        club.save()
    return club_list(request)


def club_detail(request, pk):
    clubs = Club.objects.filter(id=pk)

    if clubs.count() > 0:
        context_object_name = {
            "club": clubs[0]
        }

    return render(request, 'ubs_project/club_detail.html', context_object_name)


def club_exit(request, pk):
    clubs = Club.objects.filter(id=pk)

    if clubs.count() > 0:
        context_object_name = {
            "club": clubs[0]
        }

    from django.db import connection
    cursor = connection.cursor()
    delete_sql = "delete from ubs_project_club_student where club_id= {0} and user_id = {1}".format(pk, request.user.id)
    cursor.execute(delete_sql)

    return club_list(request)


def club_dismiss(request, pk):
    clubs = Club.objects.filter(id=pk)

    if clubs.count() > 0:
        context_object_name = {
            "club": clubs[0]
        }

    from django.db import connection
    cursor = connection.cursor()
    delete_sql1 = "delete from ubs_project_club_student where club_id= {0}".format(pk)
    delete_sql2 = "delete from ubs_project_club where id= {0}".format(pk)
    cursor.execute(delete_sql1)
    cursor.execute(delete_sql2)

    return club_list(request)
