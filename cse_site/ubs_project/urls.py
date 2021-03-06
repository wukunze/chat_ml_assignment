from django.urls import path
from .views import event
from .views import registration
from .views import index

urlpatterns = [
    path("", index.index, name="home"),
    path("sign_up/", registration.sign_up, name="sign_up"),

    # story 5 : A student can CRUD events
    # ex: /ubs_project/event_list/
    path('event_list/', event.IndexView.as_view(), name='event_list'), # show all

    # ex: /ubs_project/event_detail/
    path('event_detail/<int:pk>/', event.DetailView.as_view(), name='event_detail'), # show event by pk

    path('event_create/', event.event_create, name='event_create'),  # GET to show the html form
    path('event_create_handler/', event.event_create_handler, name='event_create_handler'),  # POST receive data

    path('event_update/<int:pk>/', event.event_update, name='event_update'), # GET to show the html form
    path('event_update_handler/<int:pk>/', event.event_update_handler, name='event_update_handler'), # POST receive data

    path('event_delete/<int:pk>/', event.event_delete, name='event_delete'),

]

