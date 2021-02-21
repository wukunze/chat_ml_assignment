from django.urls import path
from .views import event


# function path()  parameter :    route  , view ,  kwargs,  name
# the 'name' value as called by the {% url %} template tag


urlpatterns = [

    # story 5 : A student can CRUD events
    # ex: /ubs_project/event/
    path('event/', event.IndexView.as_view(), name='event_index'),
    # ex: /ubs_project/event/
    path('event/<int:pk>/', event.DetailView.as_view(), name='event_detail'),

    # ex: /ubs_project/event/create/
    path('event/create/', event.CreateEventView.as_view(), name='event_create'),  # will dispatch  GET or POST

    path('event/<int:pk>/update/', event.UpdateEventView.as_view(), name='event_update'),
    path('event/<int:pk>/delete/', event.delete_event, name='event_delete'),

]

