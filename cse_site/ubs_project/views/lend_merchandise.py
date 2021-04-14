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
from ..models.item import Item
from ..models.lend import Lend
from ..models.card import Card


# lend req page
def lend_req(request, pk):
    student = get_object_or_404(User, pk=request.user.id)
    context_object_name = {}
    user_id = request.user.id
    item_id = pk
    itSets = Item.objects.filter(id=item_id)
    if itSets.count() == 0:
        return render(request, 'ubs_project/lend_req.html', context_object_name)
    it_object = itSets[0]
    name = it_object.name
    description = it_object.description
    price = it_object.price
    owner = it_object.create_by
    image = it_object.image
    owner_id = owner.id

    allow_req = True
    if request.user.id == owner_id:
        allow_req = False

    cursor = connection.cursor()
    select_sql = "select * from ubs_project_card where created_by_id= {0}".format(user_id)
    cursor.execute(select_sql)
    raw = cursor.fetchall()
    cards = []
    for i in range(len(raw)):
        c = raw[i]
        cards.append({'title': c[1], 'card_number': c[5]})

    context_object_name = {
        'item_id': item_id,
        'name': name,
        'description': description,
        'price': price,
        'owner': owner,
        'image': image,
        'owner_id': owner_id,
        'cards': cards,
        'allow_req': allow_req
    }
    return render(request, 'ubs_project/lend_req.html', context_object_name)


def lend_req_handler(request):
    student = get_object_or_404(User, pk=request.user.id)
    context_object_name = {}

    name = request.POST.get('mname')
    description = request.POST.get('mdescription')
    price = request.POST.get('mprice')
    image = request.POST.get('mimage')
    image = image[6:]
    status = 0
    create_at = timezone.now()
    item_id = request.POST.get('mid')
    rent_user_id = request.user.id
    lend_user_id = request.POST.get('lend_user_id')

    # print(name, description, price, image, create_at, item_id, rent_user_id, lend_user_id)
    cursor = connection.cursor()
    insert_sql = "insert into ubs_project_lend(id, name, description, price, image, status, created_at, rent_user_id, lend_user_id, item_id) " \
                 "values ({0}, '{1}', '{2}', {3}, '{4}', {5}, {6}, {7}, {8}, {9})".format('NULL', name, description, price, image, status, 'now()', rent_user_id, lend_user_id, item_id)
    cursor.execute(insert_sql)
    rows_affected = cursor.rowcount
    if rows_affected != 1 :
        return lend_req(request, item_id)

    return lend_list(request)

def lend_list(request):
    student = get_object_or_404(User, pk=request.user.id)
    user_id = request.user.id
    context_object_name = {
        "uid": request.user.id
    }
    search_content = request.POST.get('search_content')
    if search_content is None or search_content == '':
        m_list = Lend.objects.filter(rent_user_id=user_id).filter(status=0).order_by('-created_at')[:10]
    else:
        m_list = Lend.objects.filter(rent_user_id=user_id).filter(name__startswith=search_content).filter(status=0).order_by('-created_at')[:10]
    context_object_name['mlist'] = m_list
    return render(request, 'ubs_project/lend_list.html', context_object_name)


def lend_return_handler(request, pk):
    student = get_object_or_404(User, pk=request.user.id)
    user_id = request.user.id
    context_object_name = {
        "uid": request.user.id
    }
    cursor = connection.cursor()
    update_sql = "update ubs_project_lend set status = 1 where id = {0}".format(pk)
    cursor.execute(update_sql)
    # rows_affected = cursor.rowcount
    # if rows_affected != 1:
    #     return lend_req(request, item_id)
    return lend_list(request)


def lend_detail(request, pk):
    student = get_object_or_404(User, pk=request.user.id)
    user_id = request.user.id
    context_object_name = {
        "uid": request.user.id
    }
    itemSet = Item.objects.filter(id = pk)
    if len(itemSet) > 0:
        context_object_name['item'] = itemSet[0]
    return render(request, 'ubs_project/lend_detail.html', context_object_name)


def lend_history(request):
    student = get_object_or_404(User, pk=request.user.id)
    user_id = request.user.id
    context_object_name = {
        "uid": request.user.id
    }
    search_content = request.POST.get('search_content')
    if search_content is None or search_content == '':
        m_list = Lend.objects.filter(rent_user_id=user_id).order_by('-created_at')[:10]
    else:
        m_list = Lend.objects.filter(rent_user_id=user_id).filter(name__startswith=search_content).order_by('-created_at')[:10]

    context_object_name['lend_history'] = []
    for m in m_list:
        lend_item = {}
        lend_item['name'] = m.name
        lend_item['description'] = m.description
        lend_item['rent_time'] = m.created_at
        if m.status == 0:
            lend_item['returned'] = 'rent'
        else:
            lend_item['returned'] = 'return'
        userSet = User.objects.filter(id=m.lend_user_id)
        if len(userSet) > 0:
            lend_item['owner_name'] = userSet[0].username
        context_object_name['lend_history'].append(lend_item)

    return render(request, 'ubs_project/lend_history.html', context_object_name)
