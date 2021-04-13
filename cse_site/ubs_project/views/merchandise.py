from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.urls import reverse_lazy

from django.views import generic as views

from ..forms import FilterForm, ItemCreateForm
from ..models.item import Item
from django.contrib.auth.models import User
from ..models.order import Cart, Order


def extract_filter_values(params):
    order = params['order'] if 'order' in params else FilterForm.ORDER_ASC
    text = params['text'] if 'text' in params else ''

    return {
        'order': order,
        'text': text,
    }


def item_display(request):
    params = extract_filter_values(request.GET)
    order_by = 'name' if params['order'] == FilterForm.ORDER_ASC else '-name'
    items = Item.objects.filter(name__icontains=params['text'], status='l').order_by(order_by)

    context = {
        'items': items,
        'current_page': 'home',
        'filter_form': FilterForm(initial=params),
    }

    return render(request, 'ubs_project/merchandise/item_display.html', context)


#Exchange Merchandise
def item_exchange(request, item_id):
    params = extract_filter_values(request.GET)
    student = get_object_or_404(User, pk=request.user.id)
    lItem = get_object_or_404(Item, pk=item_id)
    lItems = Item.objects.filter(name__icontains=params['text'], create_by=student)
    numItems = len(lItems)
    for oneItem in lItems:
        if oneItem.status == "c":
            numItems = numItems - 1

    #Handle error cases
    if numItems == 0:
        return render(request, "ubs_project/merchandise/error.html",
                      {"message": "You have no items to exchange!"},
                      status=404)
    if student.username == lItem.create_by.username:
        return render(request, "ubs_project/merchandise/error.html",
                      {"message": "You cannot exchange your own item!"},
                      status=404)

    #Show exchange options
    context = {
        'lItems': lItems,
        'lItem': lItem,
        'current_page': 'home',
        'filter_form': FilterForm(initial=params),
    }
    return render(request, 'ubs_project/merchandise/item_trade.html', context)

#Finish Exchange Merchandise
def item_exchange_finish(request, buy_id, sell_id):
    bItem = get_object_or_404(Item, pk=buy_id)
    sItem = get_object_or_404(Item, pk=sell_id)
    bUser = get_object_or_404(User, pk=sItem.create_by.id)
    sUser = get_object_or_404(User, pk=bItem.create_by.id)
    
    #Create order for buyer
    bCart = Cart(user=bUser)
    bCart.save()
    bCart.add(bItem.id, 1)
    bOrder = Order(cart=bCart)
    bCart.is_ordered = True
    bCart.save()
    bOrder.save()
    bItem.sales_type = "e"
    bItem.status = "c"
    bItem.save()

    #Create order for seller
    sCart = Cart(user=sUser)
    sCart.save()
    sCart.add(sItem.id, 1)
    sOrder = Order(cart=sCart)
    sCart.is_ordered = True
    sCart.save()
    sOrder.save()
    sItem.sales_type = "e"
    sItem.status = "c"
    sItem.save()

    return item_display(request)


class ItemDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    model = Item
    template_name = 'ubs_project/merchandise/item_details.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item = context[self.context_object_name]

        return context


# @group_required(groups=['Regular User'])
@login_required
def item_create(request):
    if request.method == 'GET':
        context = {
            'form': ItemCreateForm(),
            'current_page': 'item_create',
        }

        return render(request, 'ubs_project/merchandise/item_create.html', context)
    else:
        form = ItemCreateForm(request.POST, request.FILES)
        form.instance.create_by = request.user
        form.instance.created_at = datetime.now()
        if form.is_valid():
            form.save()
            return redirect('display item')

        context = {
            'form': form,
            'current_page': 'item_create',
        }

        return render(request, 'ubs_project/merchandise/item_create.html', context)


class DeleteItemView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    model = Item
    template_name = 'ubs_project/merchandise/item_delete.html'
    success_url = reverse_lazy('display item')

    def dispatch(self, request, *args, **kwargs):
        item = self.get_object()
        # if item.user_id != request.user.userprofile.id:
        #     return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class UpdateItemView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    template_name = 'ubs_project/merchandise/item_edit.html'
    model = Item
    form_class = ItemCreateForm

    def get_success_url(self):
        url = reverse_lazy('item details', kwargs={'pk': self.object.id})
        return url
