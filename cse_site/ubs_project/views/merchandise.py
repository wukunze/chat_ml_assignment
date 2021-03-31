from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views import generic as views

from ..forms import FilterForm, ItemCreateForm
from ..models.item import Item


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
    items = Item.objects.filter(name__icontains=params['text']).order_by(order_by)

    context = {
        'items': items,
        'current_page': 'home',
        'filter_form': FilterForm(initial=params),
    }

    return render(request, 'ubs_project/merchandise/item_display.html', context)


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
